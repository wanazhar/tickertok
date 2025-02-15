from fastapi import FastAPI, UploadFile, File, Request, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, StreamingResponse
import pandas as pd
import numpy as np
import yfinance as yf
import io
import json
from datetime import datetime
import pandas_ta as ta
from pypfopt import EfficientFrontier
from reportlab.pdfgen import canvas
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = FastAPI()
router = APIRouter(prefix="/api")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"Request path: {request.url.path}")
    response = await call_next(request)
    print(f"Response status: {response.status_code}")
    return response

@app.get("/")
async def root():
    return {"message": "API is running"}

@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.post("/process")
async def process_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        df = pd.read_csv(io.StringIO(contents.decode('utf-8')))
        
        if "Ticker" not in df.columns:
            return JSONResponse(
                status_code=400,
                content={"error": "CSV must contain a 'Ticker' column"},
                headers={"Access-Control-Allow-Origin": "*"}
            )

        result = []

        for ticker in df["Ticker"]:
            try:
                stock = yf.Ticker(ticker)
                history = stock.history(period="1mo")
                latest_price = history["Close"].iloc[-1] if not history.empty else "N/A"
                result.append({"Ticker": ticker, "Latest Price": latest_price})
            except Exception as e:
                result.append({"Ticker": ticker, "Latest Price": "Error"})

        output_df = pd.DataFrame(result)
        output_csv = io.StringIO()
        output_df.to_csv(output_csv, index=False)
        
        return JSONResponse(
            content=output_csv.getvalue(),
            media_type="text/csv",
            headers={"Access-Control-Allow-Origin": "*"}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)},
            headers={"Access-Control-Allow-Origin": "*"}
        )

@router.post('/technical-analysis')
async def technical_analysis(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    df.ta.strategy('All')
    return JSONResponse(content=df.to_json(), headers={'Access-Control-Allow-Origin': '*'})

@router.post('/optimize-portfolio')
async def optimize_portfolio(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    returns = df.pct_change().dropna()
    ef = EfficientFrontier(returns.mean(), returns.cov())
    weights = ef.max_sharpe()
    return JSONResponse(content=json.dumps(weights), headers={"Access-Control-Allow-Origin": "*"})


@router.post('/market-sentiment')
async def market_sentiment():
    news = yf.Ticker('^GSPC').news
    analyzer = SentimentIntensityAnalyzer()
    sentiments = [analyzer.polarity_scores(n['title']) for n in news]
    return JSONResponse(content=json.dumps(sentiments), headers={"Access-Control-Allow-Origin": "*"})


app.include_router(router)
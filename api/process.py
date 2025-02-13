from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import yfinance as yf
import io

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
async def health_check():
    return {"status": "ok"}

@app.post("/api/process")
async def process_file(file: UploadFile = File(...)):
    try:
        # Read the file content into memory first
        contents = await file.read()
        df = pd.read_csv(io.StringIO(contents.decode('utf-8')))
        
        if "Ticker" not in df.columns:
            return {"error": "CSV must contain a 'Ticker' column"}

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
        
        return output_csv.getvalue()
    except Exception as e:
        return {"error": str(e)} 
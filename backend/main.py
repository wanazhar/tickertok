from fastapi import FastAPI, UploadFile, File import pandas as pd import yfinance as yf import io

app = FastAPI()

@app.post("/process")
async def process_file(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    
    if "Ticker" not in df.columns:
        return {"error": "CSV must contain a 'Ticker' column"}

    result = []

    for ticker in df["Ticker"]:
        try:
            stock = yf.Ticker(ticker)
            history = stock.history(period="1mo")  # Fetch last month's prices
            latest_price = history["Close"].iloc[-1] if not history.empty else "N/A"
            result.append({"Ticker": ticker, "Latest Price": latest_price})
        except Exception as e:
            result.append({"Ticker": ticker, "Latest Price": "Error"})

    output_df = pd.DataFrame(result)
    output_csv = io.StringIO()
    output_df.to_csv(output_csv, index=False)

    return output_csv.getvalue()
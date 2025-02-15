# api/main.py
from fastapi import FastAPI, HTTPException
from datetime import datetime
from market_data import MarketDataService
import uvicorn

app = FastAPI(title="TickerTok Pro", version="1.0.0")

@app.get("/api/market/{symbol}")
async def get_market_data(symbol: str):
    service = MarketDataService()
    try:
        data = await service.get_real_time_price(symbol)
        if 'error' in data:
            raise HTTPException(status_code=400, detail=data['error'])
        return {
            "symbol": symbol,
            "price": data['price'],
            "currency": data.get('currency', 'USD'),
            "timestamp": datetime.utcnow().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
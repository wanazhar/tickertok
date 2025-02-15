# api/market_data.py
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockLatestQuoteRequest
from binance import AsyncClient
import oandapyV20
import os

class MarketDataService:
    def __init__(self):
        # Initialize with environment variables
        self.stock_client = StockHistoricalDataClient(
            os.getenv('ALPACA_KEY'),
            os.getenv('ALPACA_SECRET')
        )
        self.crypto_client = AsyncClient(
            os.getenv('BINANCE_KEY'),
            os.getenv('BINANCE_SECRET')
        )
        self.fx_client = oandapyV20.API(
            access_token=os.getenv('OANDA_TOKEN'),
            environment="practice"
        )

    async def get_real_time_price(self, symbol: str):
        """Get real-time price with error handling"""
        try:
            if '/' in symbol:  # Forex pair
                return await self._get_fx_rate(symbol)
            elif symbol.endswith('=X'):  # Crypto
                clean_symbol = symbol.replace('=X', '')
                return await self._get_crypto_price(clean_symbol)
            else:  # Stock
                return await self._get_stock_price(symbol)
        except Exception as e:
            return {"error": str(e)}

    async def _get_stock_price(self, symbol):
        request = StockLatestQuoteRequest(symbol_or_symbols=[symbol])
        quote = self.stock_client.get_stock_latest_quote(request)
        return {
            "symbol": symbol,
            "price": quote.data[symbol].ask_price,
            "currency": "USD"
        }

    async def _get_crypto_price(self, symbol):
        ticker = await self.crypto_client.get_symbol_ticker(symbol=symbol)
        return {
            "symbol": symbol,
            "price": float(ticker['price']),
            "currency": "USD"
        }

    async def _get_fx_rate(self, pair):
        params = {"count": 1, "granularity": "M1"}
        response = self.fx_client.instrument.candles(pair, params=params)
        return {
            "symbol": pair,
            "price": float(response['candles'][0]['mid']['c']),
            "currency": "FX"
        }
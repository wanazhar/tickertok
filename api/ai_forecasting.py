# api/ai_forecasting.py
class AlphaGenerator:
    def __init__(self):
        self.model = TimeSeriesTransformer(
            num_layers=12, 
            d_model=512,
            nhead=8
        )
    
    def train_on_historical(self, data):
        self.model.fit(data, epochs=100, batch_size=32)
    
    def predict_next_24h(self, symbol):
        return self.model.predict(symbol)[-24:]
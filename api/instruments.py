# api/instruments.py
SUPPORTED_MARKETS = [
    "Equities",
    "Futures",
    "Options",
    "FX",
    "Fixed Income",
    "Cryptocurrencies",
    "Commodities",
    "Structured Products",
    "Derivatives"
]

class UniversalSecurity:
    def __init__(self, identifier):
        self.bloomberg = BloombergSecurity(identifier)
        self.refinitiv = RefinitivSecurity(identifier)
        self.cryptocompare = CryptoCompareFeed(identifier)
    
    def consolidated_data(self):
        return {
            "bloomberg": self.bloomberg.snap(),
            "refinitiv": self.refinitiv.get_snapshot(),
            "crypto": self.cryptocompare.price()
        }
# api/news.py
class BloombergNewsParser:
    def latest_headlines(self):
        return requests.get(
            "https://www.bloomberg.com/markets2/api/history/",
            headers={"User-Agent": "Mozilla/5.0"}
        ).json()

@router.get("/news/{source}")
async def financial_news(source: str):
    if source == "bloomberg":
        return BloombergNewsParser().latest_headlines()
    elif source == "reuters":
        return ReutersScraper().get_articles()
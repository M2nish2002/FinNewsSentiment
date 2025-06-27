# app/services/news_scraper.py

import feedparser
from datetime import datetime
import hashlib

def fetch_rss_articles(feed_urls):
    articles = []

    for url in feed_urls:
        feed = feedparser.parse(url)

        for entry in feed.entries:
            article = {
                "id": hashlib.md5(entry.title.encode()).hexdigest(),
                "title": entry.title,
                "link": entry.link,
                "published": entry.get("published", str(datetime.utcnow())),
                "source": feed.feed.get("title", "Unknown")
            }
            articles.append(article)

    return articles


# Example RSS feed URLs
DEFAULT_FEEDS = [
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=AAPL,MSFT,GOOG,TSLA&region=US&lang=en-US",
    "https://www.investing.com/rss/news_285.rss",  # Markets
    "https://www.reutersagency.com/feed/?best-topics=business-finance&post_type=best",
]

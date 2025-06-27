# app/services/news_processor.py

from app.services.news_scraper import fetch_rss_articles, DEFAULT_FEEDS
from app.ml.model import SentimentModel
from app.db.session import SessionLocal
from app.db.models import NewsArticle
from sqlalchemy.exc import IntegrityError

model = SentimentModel()

def analyze_and_save_articles():
    articles = fetch_rss_articles(DEFAULT_FEEDS)
    db = SessionLocal()

    for article in articles:
        sentiment = model.predict(article["title"])

        news_entry = NewsArticle(
            id=article["id"],
            title=article["title"],
            link=article["link"],
            published=article["published"],
            source=article["source"],
            sentiment=sentiment["label"],
            confidence=sentiment["confidence"],
        )

        try:
            db.add(news_entry)
            db.commit()
        except IntegrityError:
            db.rollback()  # Ignore duplicates
        except Exception as e:
            print(f"❌ Failed to save article: {e}")
            db.rollback()
    db.close()


from sqlalchemy import Column, String, Float, DateTime
from datetime import datetime
from app.db.base import Base  # use your existing Base

class NewsArticle(Base):
    __tablename__ = "news_articles"

    id = Column(String, primary_key=True, index=True)
    title = Column(String, nullable=False)
    link = Column(String)
    published = Column(DateTime, default=datetime.utcnow)
    source = Column(String)
    sentiment = Column(String)
    confidence = Column(Float)

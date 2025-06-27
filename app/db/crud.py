
from sqlalchemy.orm import Session
from app.db.models import NewsArticle

def save_article(db: Session, article: dict):
    if db.query(NewsArticle).filter(NewsArticle.id == article["id"]).first():
        return  # Already exists
    db_article = NewsArticle(**article)
    db.add(db_article)
    db.commit()
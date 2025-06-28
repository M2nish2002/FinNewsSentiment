from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.ml.model import SentimentModel
from app.db.session import SessionLocal
from app.db.models import NewsArticle

router = APIRouter()
model = SentimentModel()

class NewsItem(BaseModel):
    text: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/sentiment")
async def analyze_sentiment(item: NewsItem):
    result = model.predict(item.text)
    return {"sentiment": result}

@router.get("/news")
def get_all_news(db: Session = Depends(get_db)):
    return db.query(NewsArticle).order_by(NewsArticle.published.desc()).all()

from fastapi import APIRouter
from pydantic import BaseModel
from app.ml.model import SentimentModel

router = APIRouter()
model = SentimentModel()

class NewsItem(BaseModel):
    text: str

@router.post("/sentiment")
async def analyze_sentiment(item: NewsItem):
    result = model.predict(item.text)
    return {"sentiment": result}
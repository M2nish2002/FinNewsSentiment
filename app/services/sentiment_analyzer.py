from app.ml.model import SentimentModel

# Initialize once and reuse
sentiment_model = SentimentModel()

def analyze_article_sentiment(article):
    sentiment = sentiment_model.predict(article["title"])
    return {
        **article,
        "sentiment": sentiment["label"],
        "confidence": round(sentiment["confidence"], 4)
    }
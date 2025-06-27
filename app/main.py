from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import redis
from app.config import settings
from app.db.init_db import init_db
from app.api.routes import router as api_router
from threading import Timer
from app.services.news_processor import analyze_and_save_articles
app = FastAPI(title=settings.app_name)
app.include_router(api_router, prefix="/api")
@app.on_event("startup")
def on_startup():
    init_db()

    # Start recurring news analysis every 5 minutes
    def run_job():
        try:
            analyze_and_save_articles()
        except Exception as e:
            print(f"[Scheduler Error] {e}")
        Timer(300, run_job).start()  # 300 seconds = 5 minutes

    run_job()


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Redis client
redis_client = redis.Redis(host=settings.redis_host, port=settings.redis_port)

@app.get("/")
def root():
    return {"message": "Welcome to the Real-Time FinNews Sentiment API 🚀"}

@app.get("/health")
def health_check():
    redis_status = redis_client.ping()
    return {
        "status": "ok",
        "redis": redis_status,
        "env": settings.env
    }



from app.services.news_processor import analyze_and_save_articles

@app.get("/analyze-news")
def run_news_pipeline():
    analyze_and_save_articles()
    return {"status": "News processed and saved"}
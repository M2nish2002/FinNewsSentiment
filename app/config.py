from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env

class Settings(BaseSettings):
    app_name: str = os.getenv("APP_NAME")
    env: str = os.getenv("ENV")
    debug: bool = os.getenv("DEBUG") == "True"
    
    # PostgreSQL
    db_host: str = os.getenv("POSTGRES_HOST")
    db_port: int = int(os.getenv("POSTGRES_PORT"))
    db_user: str = os.getenv("POSTGRES_USER")
    db_password: str = os.getenv("POSTGRES_PASSWORD")
    db_name: str = os.getenv("POSTGRES_DB")

    # Redis
    redis_host: str = os.getenv("REDIS_HOST")
    redis_port: int = int(os.getenv("REDIS_PORT"))

settings = Settings()
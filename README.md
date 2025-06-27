# FinNewsSentiment



**Real-Time Financial News Sentiment Analysis API**

This project fetches financial news from various RSS feeds, analyzes their sentiment using a FinBERT model, and stores the results in a PostgreSQL database. Redis is used for caching or messaging. The backend is built with FastAPI and fully containerized with Docker.

---

## Features

- Fetches financial news from multiple RSS feeds
- Performs sentiment analysis using a pretrained FinBERT model
- Stores articles and sentiment results in PostgreSQL
- Provides API endpoints for health checks and triggering news analysis
- Uses Redis for caching or message brokering
- Dockerized for easy setup and deployment

---

## Tech Stack

- Python 3.10
- FastAPI
- PostgreSQL (via Docker)
- Redis (via Docker)
- Hugging Face Transformers (FinBERT)
- Docker & Docker Compose

---

## Getting Started

### Prerequisites

- Docker & Docker Compose installed

### Setup

1. Create a `.env` file in the root directory with the following content:

    ```env
    APP_NAME=FinNewsSentiment
    ENV=development
    DEBUG=True

    POSTGRES_DB=finnewsdb
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=yourpassword
    POSTGRES_HOST=db
    POSTGRES_PORT=5432

    REDIS_HOST=redis
    REDIS_PORT=6379

    SECRET_KEY=your_secret_key
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```

2. Build and start the services using Docker Compose:

    ```bash
    docker-compose up --build
    ```

3. The API will be available at:

    ```
    http://localhost:8000
    ```

---

## API Endpoints

- `GET /`  
  Returns a welcome message.

- `GET /health`  
  Returns health status including Redis connectivity.

- `GET /analyze-news`  
  Triggers the news fetching and sentiment analysis pipeline.

---

## Running Locally (Without Docker)

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Make sure you have PostgreSQL and Redis running locally, or update your `.env` file accordingly.

3. Run the FastAPI app:

    ```bash
    uvicorn app.main:app --reload
    ```

---

## Project Structure
        app/
    ├── api/ # API route definitions
    ├── db/ # Database models and session management
    ├── ml/ # Sentiment analysis model code
    ├── services/ # News fetching and processing logic
    ├── main.py # FastAPI app entry point
    └── config.py # Configuration and environment variables
    docker-compose.yml # Docker Compose setup
    Dockerfile # FastAPI Docker image setup
    requirements.txt # Python dependencies
    README.md # This file


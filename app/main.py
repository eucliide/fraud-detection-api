from fastapi import FastAPI
from app.core.config import settings


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Real-Time Fraud Detection Platform"
)


@app.get("/")
def root():
    return {
        "message": "Fraud Detection API is running."
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
import logging
from fastapi import FastAPI
from app.core.config import settings
from app.core.logging import setup_logging


logger = logging.getLogger(__name__)

setup_logging()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Real-Time Fraud Detection Platform"
)


@app.get("/")
def home():

    logger.info("Root endpoint accessed")

    return {
        "message": "Fraud Detection API is running."
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
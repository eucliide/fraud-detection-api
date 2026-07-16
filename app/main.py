import logging

from fastapi import FastAPI

from app.api.v1.router import router
from app.core.config import settings
from app.core.logging import setup_logging


setup_logging()

logger = logging.getLogger(__name__)


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Real-Time Fraud Detection API"
)


app.include_router(
    router,
    prefix="/api/v1"
)


@app.get("/")
def root():

    logger.info("Root endpoint accessed")

    return {
        "message": "Fraud Detection API is running"
    }
import logging

from fastapi import APIRouter

from app.schemas.transaction import TransactionRequest
from app.services.fraud_service import FraudDetectionService


router = APIRouter()

logger = logging.getLogger(__name__)

fraud_service = FraudDetectionService()


@router.post("/transactions")
def analyze_transaction(
        transaction: TransactionRequest
):

    logger.info(
        "Transaction received"
    )


    result = fraud_service.analyze_transaction(
        transaction
    )


    return result
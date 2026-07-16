import logging

from fastapi import APIRouter

from app.schemas.transaction import TransactionRequest


router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/transactions")
def analyze_transaction(
        transaction: TransactionRequest
):

    logger.info(
        "Transaction received for analysis"
    )

    return {
        "message": "Transaction accepted",
        "transaction": transaction
    }
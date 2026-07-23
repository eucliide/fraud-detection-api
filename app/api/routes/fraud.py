from fastapi import APIRouter

from app.schemas.transaction import TransactionRequest
from app.schemas.prediction import PredictionResponse
from app.services.fraud_service import FraudDetectionService


router = APIRouter(
    prefix="/fraud",
    tags=["Fraud Detection"]
)


fraud_service = FraudDetectionService()


@router.post(
    "/predict",
    response_model=PredictionResponse
)
def predict_transaction(
        transaction: TransactionRequest
):

    result = fraud_service.analyze_transaction(
        transaction.model_dump()
    )

    return result
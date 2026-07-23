from fastapi import APIRouter
import traceback

from app.schemas.transaction import TransactionRequest
from app.services.fraud_service import FraudDetectionService


router = APIRouter(
    prefix="/fraud",
    tags=["Fraud Detection"]
)


fraud_service = FraudDetectionService()


@router.post("/predict")
def predict_transaction(
        transaction: TransactionRequest
):

    print("ROUTE REACHED")

    try:

        result = fraud_service.analyze_transaction(
            transaction.model_dump()
        )

        return result

    except Exception:

        print("PREDICTION ERROR:")
        traceback.print_exc()

        raise
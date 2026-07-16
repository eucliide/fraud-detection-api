from app.services.fraud_service import FraudDetectionService
from app.schemas.transaction import TransactionRequest


def test_high_risk_transaction():

    service = FraudDetectionService()


    transaction = TransactionRequest(
        amount=5000,
        merchant="Unknown",
        country="RW",
        transaction_type="online"
    )


    result = service.analyze_transaction(
        transaction
    )


    assert result["decision"] == "high_risk"
import logging

from app.schemas.transaction import TransactionRequest


logger = logging.getLogger(__name__)


class FraudDetectionService:


    def analyze_transaction(
            self,
            transaction: TransactionRequest
    ):

        logger.info(
            "Analyzing transaction"
        )

        # Temporary logic
        # ML model will replace this later

        risk_score = 0.10

        if transaction.amount > 1000:
            risk_score = 0.80


        return {
            "risk_score": risk_score,
            "decision": self._make_decision(
                risk_score
            )
        }


    def _make_decision(
            self,
            risk_score: float
    ):

        if risk_score >= 0.7:
            return "high_risk"

        return "low_risk"
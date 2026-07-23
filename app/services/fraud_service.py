from app.services.ml_service import MLService


class FraudDetectionService:

    def __init__(self):
        self.ml_service = MLService()


    def analyze_transaction(self, transaction):

        print("FRAUD SERVICE RECEIVED:")
        print(transaction)

        ml_transaction = transaction.copy()

        ml_transaction["Amount"] = ml_transaction.pop("amount")

        print("ML TRANSACTION:")
        print(ml_transaction)

        prediction = self.ml_service.predict(
            ml_transaction
        )

        is_fraud = bool(prediction == -1)

        return {
            "is_fraud": is_fraud,
            "risk_level": "HIGH" if is_fraud else "LOW"
        }
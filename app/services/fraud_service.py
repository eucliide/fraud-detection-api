from app.services.ml_service import MLService


class FraudDetectionService:

    def __init__(self):
        self.ml_service = MLService()


    def analyze_transaction(self, transaction):

        prediction = self.ml_service.predict(
            transaction
        )

        is_fraud = prediction == -1

        return {
            "is_fraud": is_fraud,
            "risk_level": "HIGH" if is_fraud else "LOW",
            "model_prediction": prediction
        }
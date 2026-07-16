from pydantic import BaseModel


class FraudPredictionResponse(BaseModel):

    transaction_id: str

    risk_score: float

    decision: str
from pydantic import BaseModel


class PredictionResponse(BaseModel):

    is_fraud: bool
    risk_level: str
    prediction: int
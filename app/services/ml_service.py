import joblib
import pandas as pd

from pathlib import Path


MODEL_PATH = Path(
    "ml/models/fraud_detection_pipeline.pkl"
)


class MLService:

    def __init__(self):
        self.model = joblib.load(MODEL_PATH)


    def predict(self, transaction):

        data = pd.DataFrame(
            [transaction]
        )

        prediction = self.model.predict(data)

        return prediction[0]
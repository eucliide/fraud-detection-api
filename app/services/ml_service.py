import joblib
import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = BASE_DIR / "ml" / "models" / "fraud_detection_pipeline.pkl"


FEATURE_COLUMNS = [
    "V1", "V2", "V3", "V4", "V5", "V6", "V7",
    "V8", "V9", "V10", "V11", "V12", "V13", "V14",
    "V15", "V16", "V17", "V18", "V19", "V20", "V21",
    "V22", "V23", "V24", "V25", "V26", "V27", "V28",
    "Amount"
]


class MLService:

    def __init__(self):

        self.model = joblib.load(MODEL_PATH)

        print("MODEL LOADED:")
        print(type(self.model))

        if hasattr(self.model, "feature_names_in_"):
            print("MODEL FEATURES:")
            print(self.model.feature_names_in_)


    def predict(self, transaction):

        print("TRANSACTION KEYS:")
        print(transaction.keys())

        data = pd.DataFrame([transaction])

        print("DATAFRAME COLUMNS:")
        print(data.columns.tolist())

        data = data[FEATURE_COLUMNS]

        prediction = self.model.predict(data)

        return prediction[0]
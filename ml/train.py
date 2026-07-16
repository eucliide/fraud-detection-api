from sklearn.metrics import (
    classification_report,
    confusion_matrix
)

import logging
from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATA_PATH = "ml/data/creditcard.csv"
MODEL_PATH = Path("ml/models/isolation_forest.pkl")


def load_data():
    logger.info("Loading dataset...")
    df = pd.read_csv(DATA_PATH)
    logger.info(f"Dataset shape: {df.shape}")
    return df


def train_model(df):
    X = df.drop(columns=["Class"])
    y = df["Class"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    logger.info("Training Isolation Forest...")

    model = IsolationForest(
        contamination=0.002,
        random_state=42
    )

    model.fit(X_train)

    logger.info("Training completed.")

    return model, X_test, y_test

def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)

    predictions = (predictions == -1).astype(int)

    print(classification_report(y_test, predictions))
    print(confusion_matrix(y_test, predictions))

def save_model(model):
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)

    joblib.dump(model, MODEL_PATH)

    logger.info(f"Model saved to {MODEL_PATH}")


def main():

    df = load_data()

    model, X_test, y_test = train_model(df)

    evaluate_model(
        model,
        X_test,
        y_test
    )

    save_model(model)



if __name__ == "__main__":
    main()
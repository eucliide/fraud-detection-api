from fastapi import FastAPI

app = FastAPI(
    title="Fraud Detection API",
    version="1.0.0",
    description="Real-time fraud detection service using machine learning."
)


@app.get("/")
def root():
    return {
        "message": "Fraud Detection API is running."
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
from pathlib import Path

import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Smart Expense Analyzer API")

MODELS_DIR = Path(__file__).resolve().parent / "models"
vectorizer = joblib.load(MODELS_DIR / "vectorizer.joblib")
model = joblib.load(MODELS_DIR / "model.joblib")

CONFIDENCE_THRESHOLD = 0.6


class Transaction(BaseModel):
    description: str


def categorize(text: str):
    numbers = vectorizer.transform([text])
    probs = model.predict_proba(numbers)[0]
    confidence = float(probs.max())
    if confidence < CONFIDENCE_THRESHOLD:
        return "Uncategorized", confidence
    return str(model.classes_[probs.argmax()]), confidence


@app.get("/")
def home():
    return {"message": "Smart Expense Analyzer API is running! 🚀"}


@app.post("/predict")
def predict(transaction: Transaction):
    category, confidence = categorize(transaction.description)
    return {
        "description": transaction.description,
        "category": category,
        "confidence": round(confidence, 2),
    }
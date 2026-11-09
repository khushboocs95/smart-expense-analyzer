from pathlib import Path
import io
import joblib
from fastapi import FastAPI , File, HTTPException, UploadFile
from pydantic import BaseModel
import pandas as pd

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

@app.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="Please upload a .csv file")

    content = await file.read()
    try:
        df = pd.read_csv(io.BytesIO(content))
    # except Exception:
    #     raise HTTPException(status_code=400, detail="Could not read this CSV file")
    except Exception as e:
        print("CSV ERROR:", repr(e))
        raise HTTPException(status_code=400, detail="Could not read this CSV file")

    if "description" not in df.columns or "amount" not in df.columns:
        raise HTTPException(
            status_code=400,
            detail="CSV must have 'description' and 'amount' columns",
        )

    df["description"] = df["description"].astype(str).str.strip().str.upper()
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0)

    results = df["description"].apply(categorize)
    df["category"] = [r[0] for r in results]
    df["confidence"] = [round(r[1], 2) for r in results]

    summary = df.groupby("category")["amount"].sum().round(0).to_dict()

    return {
        "total_transactions": len(df),
        "uncategorized": int((df["category"] == "Uncategorized").sum()),
        "spending_by_category": summary,
        "transactions": df.to_dict(orient="records"),
    }
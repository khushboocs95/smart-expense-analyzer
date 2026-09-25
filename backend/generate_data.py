import numpy as np
import pandas as pd
from pathlib import Path
np.random.seed(42)

merchants = {
    "Food": ["SWIGGY ORDER", "ZOMATO", "DOMINOS PIZZA", "CHAI POINT", "STARBUCKS"],
    "Travel": ["UBER TRIP", "OLA CABS", "IRCTC TICKET", "INDIGO AIRLINES", "METRO RECHARGE"],
    "Shopping": ["AMAZON PAY", "FLIPKART", "MYNTRA", "DMART", "RELIANCE TRENDS"],
    "Bills": ["JIO RECHARGE", "TORRENT POWER", "AIRTEL BROADBAND", "GAS BILL", "LIC PREMIUM"],
    "Entertainment": ["NETFLIX", "BOOKMYSHOW", "SPOTIFY", "PVR CINEMAS", "HOTSTAR"],
}
amount_range = {
    "Food": (60, 800), "Travel": (40, 6000), "Shopping": (200, 5000),
    "Bills": (150, 3000), "Entertainment": (99, 900),
}
dates = pd.date_range("2025-10-01", "2026-09-24", freq="D")

rows = []
for _ in range(2000):
    category = np.random.choice(list(merchants))
    merchant = np.random.choice(merchants[category])
    low, high = amount_range[category]
    rows.append({
        "date": dates[np.random.randint(len(dates))].strftime("%Y-%m-%d"),
        "description": f"{merchant} *{np.random.randint(1000, 9999)}",
        "amount": np.random.randint(low, high),
        "payment_mode": np.random.choice(["UPI", "Card", "NetBanking"]),
        "category": category,
    })

df = pd.DataFrame(rows)

# Add realistic mess
df.loc[np.random.choice(len(df), 30, replace=False), "amount"] = np.nan
messy = np.random.choice(len(df), 200, replace=False)
df.loc[messy, "description"] = df.loc[messy, "description"].str.lower() + "   "
df = pd.concat([df, df.sample(20, random_state=1)])            # duplicates
df = df.sample(frac=1, random_state=2).reset_index(drop=True)  # shuffle
DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)

df.to_csv(DATA_DIR / "transactions.csv", index=False)
print("Saved", len(df), "rows to", DATA_DIR)
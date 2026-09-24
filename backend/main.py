import numpy as np
import pandas as pd

expenses = np.array([250, 1200, 80, 560])
print("Total spent:", expenses.sum())

df = pd.DataFrame({"item": ["Chai", "Rent share", "Bus", "Groceries"], "amount": expenses})
print(df)
transactions = [
    {"item": "Chai", "amount": 250, "category": "Small"},
    {"item": "Lunch", "amount": 500, "category": "Food"},
    {"item": "Bus", "amount": 80, "category": "Travel"},
    {"item": "Coffee", "amount": 60, "category": "Food"},
    {"item": "Movie", "amount": 300, "category": "Entertainment"}
]

def total_spent(txsn):
    total = 0
    for t in txsn:
        total += t["amount"]
    return total
print ("Total Spent",total_spent(transactions))


# 3. Function to filter transactions by category

def by_category(txsn, category):
    return [txsn for txsn in txsn if txsn["category"] == category]
print(by_category(transactions,"Food"))
    
# 4. Print transactions in "Chai - 250 - Small" style

def label(txn):
    return f'{txn["item"]} - {txn["amount"]} - {txn["category"]}'


for txn in transactions:
    print(label(txn))


# 5. Build totals per category

category_totals = {}

for txn in transactions:
    category = txn["category"]
    amount = txn["amount"]

    if category not in category_totals:
        category_totals[category] = 0

    category_totals[category] += amount


print("Totals per category:")
print(category_totals)

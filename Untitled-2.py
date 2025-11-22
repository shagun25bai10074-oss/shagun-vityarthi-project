import random

# Function to create a fake transaction
def create_transaction():
    amount = round(random.uniform(1, 1000), 2)
    place = random.choice(["Shop", "Online", "Abroad"])
    period = random.choice(["Day", "Night"])
    return {"amount": amount, "place": place, "period": period}

# Simple logic to detect fraud
def detect_fraud(trx):
    if trx["amount"] > 750 and trx["place"] == "Abroad" and trx["period"] == "Night":
        return True
    else:
        return False

# Simulate 8 transactions
for number in range(8):
    tx = create_transaction()
    print(f"Transaction {number+1}: {tx}")
    if detect_fraud(tx):
        print("Status: Fraud Detected\n")
    else:
        print("Status: Safe\n")

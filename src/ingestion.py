import csv
import os

def ingest_data():
    os.makedirs("data", exist_ok=True)

    file_path = "data/raw_transactions.csv"

    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["transaction_id", "amount"])

        writer.writerow([1, 100])
        writer.writerow([2, -50])
        writer.writerow([3, 200])

    print(f"Raw data written to {file_path}")
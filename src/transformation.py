import csv

def transform_data():
    input_path = "data/clean_transactions.csv"
    total = 0

    with open(input_path, mode="r") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            total += int(row["amount"])

    print(f"Total transaction amount: {total}")
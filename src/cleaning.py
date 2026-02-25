import csv

def clean_data():
    input_path = "data/raw_transactions.csv"
    output_path = "data/clean_transactions.csv"

    with open(input_path, mode="r") as infile, open(output_path, mode="w", newline="") as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=["transaction_id", "amount"])

        writer.writeheader()

        for row in reader:
            amount = int(row["amount"])
            if amount > 0:  # remove negative transactions
                writer.writerow(row)

    print(f"Clean data written to {output_path}")
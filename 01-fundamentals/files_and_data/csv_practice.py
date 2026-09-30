import csv
from pathlib import Path

path = Path(__file__).parent / "evals.csv"

with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["prompt", "expected","score"])
        writer.writeheader()
        writer.writerow({"prompt": "2+2?", "expected": "4", "score": "1"})

with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
                print(row["prompt"], int(row["score"]))
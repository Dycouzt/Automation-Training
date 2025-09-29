"""
File Handling and Logs
Write a script to parse a log file (.log) and extract all lines with the word ERROR.
Count the number of errors per day and save results to a CSV.
"""

import re
import sys
import csv
from pathlib import Path
from collections import defaultdict

def log_search():
    directory = Path(__file__).resolve().parent
    return [f for f in directory.iterdir() if f.is_file() and f.suffix == ".log"]

def log_parsing(log_files):
    pattern = re.compile(r"\bERROR\b")
    error_counts = defaultdict(int)

    for log_file in log_files:
        with log_file.open("r") as f:
            for line in f:
                if pattern.search(line):
                    # Assuming log format starts with YYYY-MM-DD
                    date = line.split()[0]
                    error_counts[date] += 1
    return error_counts

def save_to_csv(error_counts, output_file="errors_report.csv"):
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Date", "Error_Count"])
        for date, count in sorted(error_counts.items()):
            writer.writerow([date, count])

if __name__ == "__main__":
    logs = log_search()
    if not logs:
        print("No .log files found.")
        sys.exit(1)
    errors = log_parsing(logs)
    save_to_csv(errors)
    print("Report saved to errors_report.csv")

    

import csv
import argparse
import os

def extract_data(filepath):
    with open(filepath, 'r') as file:
        print(f"Extracting data from {filepath}...")
        reader = csv.DictReader(file)
        for row in reader:
            if float(row['a13']) - float(row['f12']) > 0:
                print(row)

def process_directory(directory):
    for filename in os.listdir(directory):
        print(f"Processing {filename}...")
        if filename.endswith('.csv'):
            extract_data(os.path.join(directory, filename))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process CSV files in a directory")
    parser.add_argument("--fp", required=True, help="The directory containing the CSV files to process")
    args = parser.parse_args()

    process_directory(args.fp)
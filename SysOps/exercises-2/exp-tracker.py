"""
Experiment Tracker JSONL Parser
Parse a .jsonl file of ML experiment metrics and print best run sorted by accuracy.
"""

import jsonlines
import argparse

parser = argparse.ArgumentParser(description='Parse a .jsonl file of ML experiment metrics and print best run sorted by accuracy.')
parser.add_argument('file', help='Path to the .jsonl file')

args = parser.parse_args()

def main():
    try:
        runs = []
        with jsonlines.open(args.file) as reader:
            for obj in reader:
                runs.append(obj)
        
        # Filter runs with accuracy and sort them
        valid_runs = [r for r in runs if 'accuracy' in r]
        
        if not valid_runs:
            print("No runs with 'accuracy' field found.")
            return
            
        # Sort by accuracy descending
        valid_runs.sort(key=lambda x: x['accuracy'], reverse=True)
        
        best_run = valid_runs[0]
        print(best_run)
        
    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")



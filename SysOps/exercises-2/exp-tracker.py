"""
Experiment Tracker JSONL Parser
Parse a .jsonl file of ML experiment metrics and print best run sorted by accuracy.
"""

import jsonlines
import argparse

parser = argparse.ArgumentParser(description='Parse a .jsonl file of ML experiment metrics and print best run sorted by accuracy.')


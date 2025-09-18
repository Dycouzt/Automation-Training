# sys module practice exercises.

import sys
from pathlib import Path

"""
1. Argument Parser: Write a script using sys.argv that accepts a filename 
and prints whether it exists. Exit with 0 if found, 1 otherwise.
"""
arg = str(sys.argv([1]))
home_dir = Path.home().resolve()
found = False

for item in home_dir.rglob("*{arg}"):
    if item.is_file and item == arg:
        print(f"{arg} STATUS: EXISTS. ")
        found = True

if found != True:
    print(f"{arg} STATUS: NOT FOUND. ")

"""
2. Cross-Platform Script: Use sys.platform to print OS-specific commands 
(e.g., ls for Linux, dir for Windows).
"""

""" 3. Version Checker: Create a script that exits with an error if Python version < 3.10."""

"""Custom Logger: Redirect sys.stdout to a file and log messages there."""

"""
4. Memory Tracker: Write a script that calculates 
and prints the memory size of a list of integers from 1-1000.
"""

# sys module practice exercises.

import sys
from pathlib import Path

"""
1. Argument Parser: Write a script using sys.argv that accepts a filename 
and prints whether it exists. Exit with 0 if found, 1 otherwise.
"""
if len(sys.argv) < 2:
    print("Usage: python script.py <filename>")
    sys.exit(1)

arg = sys.argv[1]
home_dir = Path.home().resolve()
found = False

for item in home_dir.rglob("*"):
    if item.is_file() and item.name == arg:
        print(f"{arg} STATUS: EXISTS at {item}")
        found = True
        break  # Stop after first match

if not found:
    print(f"{arg} STATUS: NOT FOUND.")

"""
2. Cross-Platform Script: Use sys.platform to print OS-specific commands 
(e.g., ls for Linux, dir for Windows).
"""
def cross_platform():
    window_cmds = ["dir", "where <program>", "whoami", "cd", "type nul > filename.txt"]
    linux_cmds = ["ls", "which", "whoami", "cd", "touch"]

    if sys.platform() == "win32":
        for cmd in window_cmds:
            print(cmd)
    else:
        for cmd in linux_cmds:
            print(cmd)
        
""" 3. Version Checker: Create a script that exits with an error if Python version < 3.10."""

""" 4. Custom Logger: Redirect sys.stdout to a file and log messages there."""

"""
5. Memory Tracker: Write a script that calculates 
and prints the memory size of a list of integers from 1-1000.
"""

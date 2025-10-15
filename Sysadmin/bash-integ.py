"""
Run shell commands from Python (subprocess module).
Automate package installation using Python to execute system commands.
Parse grep/awk output with Python for report generation.
Schedule tasks via Python to call Bash scripts (simulate cron jobs).
"""

import subprocess
import sys

# Run shell commands from python using subprocess module.
def run_commands():
    choice = input("What command would you like to run today?")

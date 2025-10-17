"""
Run shell commands from Python (subprocess module).
Automate package installation using Python to execute system commands.
Parse grep/awk output with Python for report generation.
Schedule tasks via Python to call Bash scripts (simulate cron jobs).
"""

import subprocess
import sys
import argparse
import platform

# Run shell commands from python using subprocess module.
def run_commands():
    linux_cmds = ["ls", "cd", "pwd", "who"] # command options if platform == linux
    window_cmds = ["dir", "where <program>", "whoami", "cd"] # command options if platform == windows

    # create argument parser to parse user input
    parser = argparse.ArgumentParser(description="Provide command to run.")

    if platform.system().lower() == "windows":
        parser.add_argument("command", nargs="+", choices=window_cmds, type=str, help="Provide one or more arguments, must be strings. ")
    else:
        parser.add_argument("command", nargs="+", choice=linux_cmds, type=str, help="Provide one or more arguments, must be strings. ")
    
    parser.add_argument("path", type=str, help="Pathname to complement commands.")
    args = parser.parse_args()

    if args in linux_cmds:
        print(f"running {args} in linux...")
        cmd = str(args.strip())
        try:
            exe = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            check=True, 
            timeout=5
            )
            print(f"{exe.stdout}")
        except subprocess.CalledProcessError as e:
            print(e.stderr.strip() if e.stderr else "Unknown error")
            
    if args in window_cmds:
        print(f"running {args} in windows...")
        try:
            exe = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            check=True, 
            timeout=5
            )
            print(f"{exe.stdout}")
        except subprocess.CalledProcessError as e:
            print(e.stderr.strip() if e.stderr else "Unknown error")






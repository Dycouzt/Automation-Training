"""
Run shell commands from Python (subprocess module).
Automate package installation using Python to execute system commands.
Parse grep/awk output with Python for report generation.
Schedule tasks via Python to call Bash scripts (simulate cron jobs).
"""

import subprocess
import argparse
import platform
from pathlib import Path
import random


def run_commands():
    linux_cmds = ["ls", "pwd", "who"]
    windows_cmds = ["dir", "where", "whoami"]

    parser = argparse.ArgumentParser(description="Run a shell command.")
    system = platform.system().lower()

    if system == "windows":
        parser.add_argument("command", choices=windows_cmds, help="Command to run on Windows")
    else:
        parser.add_argument("command", choices=linux_cmds, help="Command to run on Linux/macOS")

    parser.add_argument("--path", default=".", help="Optional path argument")
    args = parser.parse_args()

    print(f"Running '{args.command}' on {system}...")

    try:
        # If command supports path argument, include it
        cmd = [args.command]
        if args.path:
            cmd.append(args.path)

        result = subprocess.run(cmd, capture_output=True, text=True, check=True, timeout=5)
        print(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(e.stderr.strip() if e.stderr else "Unknown error")
    except FileNotFoundError:
        print("Command not found on this system.")
    except subprocess.TimeoutExpired:
        print("Command timed out.")

def pkg_inst():
    parser = argparse.ArgumentParser(description="Automate package installation.")
    parser.add_argument(
        "installer",
        choices=["brew", "pip", "apt"],
        help="The package manager to use (brew, pip, apt)."
    )
    parser.add_argument(
        "package",
        type=str,
        help="The package to install."
    )
    args = parser.parse_args()

    print(f"Installing '{args.package}' using {args.installer}...")

    try:
        cmd = [args.installer, "install", args.package]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True, timeout=30)
        print(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(e.stderr.strip() if e.stderr else "Installation failed.")
    except FileNotFoundError:
        print(f"{args.installer} not found on this system.")
    except subprocess.TimeoutExpired:
        print("Installation command timed out.")

def grep_awk():
    parser = argparse.ArgumentParser(description="Command to execute")
    parser.add_argument(
        "command", 
        required=True, 
        choices=["grep", "awk"], 
        type=str, 
        help="Input one of the available choices..."
        )
    parser.add_argument(
        "filename",
        type=str,
        required=True,
        help="filename to execute command on...")
    args = parser.parse_args()

    try:
        cmd = [args.command, args.filename]
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            check=True,
            )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(e.stderr if e else f"Unknown error")

base_dir = Path(__file__).resolve().parent

def log_reports(log_files):
    p = Path(log_files)

    if p.exists() and p.suffix("\**log"):
        for file in log_files:
            grep_awk(file)

if __name__ == "__main__":
    
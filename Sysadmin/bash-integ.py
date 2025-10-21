"""
Run shell commands from Python (subprocess module).
Automate package installation using Python to execute system commands.
Parse grep/awk output with Python for report generation.
Schedule tasks via Python to call Bash scripts (simulate cron jobs).
"""

#!/usr/bin/env python3
"""
DevOps Python Automation — Group 4: Bash Integration
Demonstrates subprocess + argparse usage for shell integration.
"""

import argparse
import platform
import subprocess
import shutil
from pathlib import Path
import time


# ------------------------------------------------------------
# 1. Run shell commands from Python
# ------------------------------------------------------------
def run_commands():
    parser = argparse.ArgumentParser(description="Run basic shell commands.")
    system = platform.system().lower()

    linux_cmds = ["ls", "pwd", "who"]
    windows_cmds = ["dir", "where", "whoami"]

    if system == "windows":
        parser.add_argument("command", choices=windows_cmds, help="Command to run on Windows")
    else:
        parser.add_argument("command", choices=linux_cmds, help="Command to run on Linux/macOS")

    parser.add_argument("--path", default=".", help="Optional path argument for listing commands")
    args = parser.parse_args()

    print(f"Running '{args.command}' on {system}...")

    try:
        if system == "windows":
            # built-ins require shell=True
            result = subprocess.run(args.command, shell=True, capture_output=True, text=True, check=True)
        else:
            cmd = [args.command]
            if args.command == "ls":
                cmd.append(args.path)
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)

        print(result.stdout.strip())

    except subprocess.CalledProcessError as e:
        print(e.stderr.strip() if e.stderr else "Command failed.")
    except FileNotFoundError:
        print("Command not found on this system.")
    except subprocess.TimeoutExpired:
        print("Command timed out.")


# ------------------------------------------------------------
# 2. Automate package installation (brew / pip / apt)
# ------------------------------------------------------------
def pkg_inst():
    parser = argparse.ArgumentParser(description="Automate package installation.")
    parser.add_argument("installer", choices=["brew", "pip", "apt"], help="Package manager")
    parser.add_argument("package", help="Package to install")
    args = parser.parse_args()

    if not shutil.which(args.installer):
        print(f"{args.installer} not found on this system.")
        return

    print(f"Installing '{args.package}' using {args.installer}...")

    try:
        if args.installer == "pip":
            cmd = ["python3", "-m", "pip", "install", args.package]
        else:
            cmd = [args.installer, "install", args.package]

        result = subprocess.run(cmd, capture_output=True, text=True, check=True, timeout=60)
        print(result.stdout.strip() or "Installation completed.")
    except subprocess.CalledProcessError as e:
        print(e.stderr.strip() if e.stderr else "Installation failed.")
    except subprocess.TimeoutExpired:
        print("Installation timed out.")


# ------------------------------------------------------------
# 3. Parse grep/awk output for simple reporting
# ------------------------------------------------------------
def grep_awk():
    parser = argparse.ArgumentParser(description="Run grep or awk on a file.")
    parser.add_argument("command", choices=["grep", "awk"], help="Utility to run")
    parser.add_argument("pattern", help="Pattern or program for grep/awk")
    parser.add_argument("filename", help="Target file")
    args = parser.parse_args()

    if not Path(args.filename).exists():
        print("File not found.")
        return

    cmd = [args.command, args.pattern, args.filename]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(result.stdout.strip() or "No matches found.")
    except subprocess.CalledProcessError as e:
        print(e.stderr.strip() if e.stderr else "Command failed.")


# ------------------------------------------------------------
# 4. Simulate log report generation using grep
# ------------------------------------------------------------
def log_reports():
    parser = argparse.ArgumentParser(description="Generate simple log reports.")
    parser.add_argument("log_dir", help="Directory containing .log files")
    parser.add_argument("--pattern", default="ERROR", help="Pattern to search for (default: ERROR)")
    args = parser.parse_args()

    log_path = Path(args.log_dir)
    if not log_path.exists():
        print("Directory not found.")
        return

    for file in log_path.glob("*.log"):
        cmd = ["grep", args.pattern, str(file)]
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"\n--- {file.name} ---")
        print(result.stdout.strip() or f"No '{args.pattern}' found.")


# ------------------------------------------------------------
# 5. Cron-like job scheduler simulation
# ------------------------------------------------------------
def cron_jobs():
    parser = argparse.ArgumentParser(description="Simulate cron job scheduling.")
    parser.add_argument("script", help="Bash script to run")
    parser.add_argument("--interval", type=int, default=30, help="Interval in seconds between runs")
    args = parser.parse_args()

    script = Path(args.script)
    if not (script.exists() and script.suffix == ".sh"):
        print("Invalid script path or not a .sh file.")
        return

    print(f"Scheduling '{script.name}' every {args.interval} seconds. Press Ctrl+C to stop.")
    try:
        while True:
            subprocess.run(["bash", str(script)], check=False)
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("\nCron simulation stopped.")


# ------------------------------------------------------------
# Entry point selector
# ------------------------------------------------------------
if __name__ == "__main__":
    # Example selector for testing one function at a time.
    # Comment/uncomment as needed when running manually.
    # run_commands()
    # pkg_inst()
    # grep_awk()
    # log_reports()
    # cron_jobs()
    pass

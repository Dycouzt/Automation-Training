# Beginner DevOps Scripting Exercises.

import sys
import os
import platform

"""
1. System Information Script (sys, os, platform)
Print Python version, OS name, current working directory, and environment variables.
Key Focus: Using sys.argv, os.getcwd(), os.environ.
"""
"""
def system_info():
    platform = platform.system()
    python_v = sys.version()
"""
def system_info():
    python_version = platform.python_version()
    os_name = platform.system()
    os_version = platform.release()
    cwd = os.getcwd()

    print(f"OS Name: {os_name} {os_version}")
    print(f"Python Version: {python_version}")
    print(f"Current Working Directory: {cwd}")

system_info()

"""
2. Disk Usage Monitor (shutil, os)
Display total, used, and free space for a given mount point.
Alert (print/warn) if usage exceeds a threshold (e.g., 80%).
"""

"""
3. Process Lister (psutil)
List all running processes with PID, name, and memory usage.
Add filtering (e.g., only processes consuming > 100MB RAM).
"""

"""
4. Directory Tree Walker (os, pathlib)
Recursively walk a directory and print its structure like the tree command.
Highlight directories vs files.
"""

"""
5. Log File Analyzer (pathlib, sys)
Read a log file path passed via sys.argv.
Count error/warning entries and print a summary report.
"""
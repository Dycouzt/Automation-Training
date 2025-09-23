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
    version_info = sys.version.split()
    info_splitted = version_info[0]
    operating_sys = platform.version
    cwd = os.getcwd()

    print(f"OS Name: ", operating_sys)
    print(f"Python Version: {info_splitted[0]}")
    print(f"Current Working Directory: ", cwd)

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
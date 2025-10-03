"""
List files recursively in a directory and filter by extension.
Monitor a directory for changes (creation/modification/deletion).
Automate backups: Copy files from one directory to another with timestamped folders.
Parse log files: Count error/warning lines from system/application logs.
"""

from pathlib import Path
import re

base_dir = Path(__file__).resolve().parent

def filter_extension():
    files = [item for item in base_dir.iterdir() if item.is_file()]

    for files in files:
        file_ext = re.compile(r'/./w+')
        print(file_ext)

filter_extension()

def monitor_dir():
    baseline = [item for item in ]
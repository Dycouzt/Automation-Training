"""
Use psutil to:
Get CPU and memory usage.
List all running processes.
Alert if usage exceeds a threshold (print message or write to file).
"""

import psutil, time
import sys

CPU_THRESHOLD = 75
MEM_THRESHOLD = 70

try:
    cpu = psutil.cpu_count(interval=1)
    time.sleep(1)

except (psutil.NoSuchProcess, psutil.AccessDenied, PermissionError):
    continue

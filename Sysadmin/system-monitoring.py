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

threshold_alert = []

# Initialize CPU measurement
cpu_usage = psutil.cpu_percent(interval=1)
mem_usage = psutil.virtual_memory()

ten_percent = []

    # Initialize CPU measurement
for process in psutil.process_iter():
    try:
        process.cpu_percent(interval=None)
    except (psutil.NoSuchProcess, psutil.AccessDenied, PermissionError):
        continue

time.sleep(1)

for process in psutil.process_iter(['pid', 'name']):
    try:
        cpu_usage = process.cpu_percent(interval=None)
        if cpu_usage > 10:
            ten_percent.append({
                "pid": process.pid,
                "name": process.name(),
                "cpu_percent": cpu_usage
            })
    except (psutil.NoSuchProcess, psutil.AccessDenied, PermissionError):
        continue
    
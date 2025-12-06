"""
Simple Resource Monitor
Using psutil, print CPU, memory, and disk metrics every second for 30 seconds.
"""

import psutil
import time

for i in range(30):
    print(f"CPU Usage: {psutil.cpu_percent()}%")
    print(f"Memory Usage: {psutil.virtual_memory().percent}%")
    print(f"Disk Usage: {psutil.disk_usage('/').percent}%")
    time.sleep(1)

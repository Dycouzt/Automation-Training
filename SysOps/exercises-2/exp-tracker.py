"""
Simple Resource Monitor
Using psutil, print CPU, memory, and disk metrics every second for 30 seconds.
"""

import psutil
import time

def resource_monitor():
    for i in range(30):
        print(f"CPU Usage: {psutil.cpu_percent()}%")
        print(f"Memory Usage: {psutil.virtual_memory().percent}%")
        print(f"Disk Usage: {psutil.disk_usage('/').percent}%")
        time.sleep(1)

threshold = 80

if psutil.cpu_percent() > threshold:
    print("CPU usage is above threshold")

if psutil.virtual_memory().percent > threshold:
    print("Memory usage is above threshold")

if psutil.disk_usage('/').percent > threshold:
    print("Disk usage is above threshold")

if __name__ == "__main__":
    resource_monitor()

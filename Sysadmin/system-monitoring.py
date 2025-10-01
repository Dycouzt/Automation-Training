"""
Use psutil to:
Get CPU and memory usage.
List all running processes.
Alert if usage exceeds a threshold (print message or write to file).
"""

import psutil, time
import sys


def running_processes():
    # List all running processes
    active_processes = [f"PID: {p.pid}, Name: {p.name}" for p in psutil.process_iter()]
    print(active_processes)
running_processes()

def threshold_check():
    CPU_THRESHOLD = 75
    MEM_THRESHOLD = 70

    # Initialize CPU measurement
    cpu_usage = psutil.cpu_percent(interval=1)
    mem_usage = psutil.virtual_memory()

    print(f"Overall CPU Usage: {cpu_usage}")
    print(f"Overall Memory Usage: {mem_usage}")

    if cpu_usage >= CPU_THRESHOLD:
        print("WARNING! CPU Usage has surpassed the system threshold!")
    elif mem_usage >= MEM_THRESHOLD:
        print("WARNING! Memory usage has surpasses the system threshold!")
    else:
        print("CPU and Memory usage are within the system healthy baseline! ")

threshold_check()
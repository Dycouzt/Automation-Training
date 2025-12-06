"""
Use psutil to:
Get CPU and memory usage.
List all running processes.
Alert if usage exceeds a threshold (print message or write to file).
"""

import psutil


def running_processes():
    processes = []
    for p in psutil.process_iter(['pid', 'name']):
        try:
            processes.append(f"PID: {p.info['pid']}, Name: {p.info['name']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return processes

def threshold_check(cpu_limit=75, mem_limit=70):
    cpu_usage = psutil.cpu_percent(interval=1)
    mem_usage = psutil.virtual_memory().percent

    alerts = []
    if cpu_usage >= cpu_limit:
        alerts.append("WARNING: CPU usage exceeded threshold")
    if mem_usage >= mem_limit:
        alerts.append("WARNING: Memory usage exceeded threshold")
    if not alerts:
        alerts.append("System healthy")

    return cpu_usage, mem_usage, alerts
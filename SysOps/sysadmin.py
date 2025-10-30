"""
Check disk usage and alert if above threshold.
List running processes and terminate processes by name.
Automate system updates (simulate with file operations if not on root).
CPU/memory monitoring script that logs usage every X seconds.
"""
from datetime import datetime
import shutil, psutil
from pathlib import Path
import time

base_dir = Path(__file__).resolve().parent

def disk_usage(directory):
    print("Getting disk usage...")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    if directory.exists():
        try:
            disk = shutil.disk_usage(directory)

            total, used, free = disk.total, disk.used, disk.free
            gb = 1024 ** 3
            total_gb, used_gb, free_gb = total / gb, used / gb, free / gb

            print(f"Total Disk: {total_gb:.2f} GB | "
                  f"Used: {used_gb:.2f} GB | "
                  f"Free: {free_gb:.2f} GB | "
                  f"As of {timestamp}")

            if free / total < 0.10:
                print("WARNING: Free space is below 10%!")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"{directory} not found.")

def running_ps():
    processes = [(p.pid, p.name()) for p in psutil.process_iter()]
    return processes

def kill_ps(process_list, target_name=None):
    for pid, name in process_list:
        if target_name and target_name.lower() in name.lower():
            try:
                psutil.Process(pid).terminate()
                print(f"Terminated {name} (PID {pid})")
            except psutil.NoSuchProcess:
                print(f"Process {pid} already exited.")
            except psutil.AccessDenied:
                print(f"Permission denied to terminate {name}.")

def log_memory_cpu(duration=15, interval=5):
    log_file = base_dir / "mem_cpu_logs.txt"
    start_time = time.time()

    with log_file.open("a") as log:
        while time.time() - start_time < duration:
            cpu = psutil.cpu_percent(interval=1)
            mem = psutil.virtual_memory()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log.write(f"{timestamp} | CPU: {cpu}% | Memory: {mem.percent}%\n")
            time.sleep(interval)

if __name__ == "__main__":
    disk_usage(base_dir)
    kill_ps(running_ps())


"""
Check disk usage and alert if above threshold.
List running processes and terminate processes by name.
Automate system updates (simulate with file operations if not on root).
CPU/memory monitoring script that logs usage every X seconds.
"""
from datetime import datetime
import shutil, psutil, subprocess
from pathlib import Path
import time

base_dir = Path(__file__).resolve().parent

def disk_usage(directory):
    print(f"Getting disk usage...")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    if directory.exists():
        try:
            disk = shutil.disk_usage(base_dir)

            # Extract values in bytes
            total = disk.total
            used = disk.free
            free = disk.free

            # Convert to GB for readability
            gb = 1024 ** 3
            total_gb = total / gb
            used_gb = used / gb
            free_gb = free / gb

            print(f"Total Memory: {total_gb:.2f} GB",
                  f"Used Memory: {used_gb:.2f} GB",
                  f"Free Memory: {free_gb:.2f} GB"
                  f"as of {timestamp}")
            
            if free / total < 0.10:
                print("WARNING: Free space is below 10%!")
        except Exception as e:
            print("Something went wrong:", e)
    else:
        print(f"{directory} not found")

def running_ps():
    active_ps = [ps.pid for ps in psutil.process_iter()]
    return active_ps

def kill_ps(processes):
    terminal_output = []

    for pid in processes:
        try:
            subprocess.run(f"kill {pid}", capture_output=True, text=True, check=True)
            terminal_output.append(pid.stdout)
        except subprocess.SubprocessError as e:
             print(e.stderr.strip() if e.stderr else "Unknown error")
    return terminal_output

def log_memory_cpu(duration=15):
    log_file = base_dir / "mem_cpu_logs.txt"
    start_time = time.time()

    while time.time() - start_time < duration:
        with log_file.open("a") as l:
            l.write(f"{psutil.cpu_percent(interval=1)}\n")
            l.write(f"{psutil.virtual_memory()}")
        time.sleep(5)

if __name__ == "__main__":
    disk_usage(base_dir)
    kill_ps(running_ps())


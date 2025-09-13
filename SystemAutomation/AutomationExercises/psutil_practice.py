# psutil practice exercises.

import psutil, time

"""
1. Write a script that lists all running processes and prints only those using more than 10% CPU.
"""
def running_processes():
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

    return ten_percent

print(running_processes())

"""
2. Create a function that prints all established network connections. 
Flag any connection not using port 80 or 443.
"""
def port_security():
    active_connections = []

    try:
        for conn in psutil.net_connections(kind='inet'):
            # Ensure it has a local address
            if conn.laddr: # laddr = ip:port → 192.168.1.5:22
                port = conn.laddr.port
                if port not in (80, 443):
                    active_connections.append({
                        "pid": conn.pid,
                        "local_address": f"{conn.laddr.ip}:{port}",
                        "remote_address": f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else None, # raddr = ip:port → 192.168.1.10:51123

                        "status": conn.status
                    })
    except (psutil.AccessDenied, psutil.NoSuchProcess, ValueError):
        pass

    return active_connections

# Example run
for threat in port_security():
    print(threat)
    
"""
3. Write a loop that prints CPU and memory usage every 2 seconds for 20 seconds 
while running another script in parallel.
"""
def cpu_loop(duration=20):
    start_time = time.time()
    
    while time.time() - start_time < duration:
        print(f"CPU usage: {psutil.cpu_percent(interval=1)}%")
        print(f"Disk usage: {psutil.disk_usage('/').percent}%")
        time.sleep(1)

cpu_loop()

"""
4. Monitor disk write bytes over time and print a warning if write activity exceeds a threshold.
"""
# Threshold in bytes per second (adjust based on your system load)
THRESHOLD = 50_000_000   # 50 MB/sec

print("Monitoring disk write activity... (Ctrl+C to stop)")

# Get initial I/O counters
prev_counters = psutil.disk_io_counters()
prev_write_bytes = prev_counters.write_bytes
prev_time = time.time()

try:
    while True:
        time.sleep(2)  # interval (seconds)
        current_counters = psutil.disk_io_counters()
        current_time = time.time()

        # Calculate delta
        bytes_written = current_counters.write_bytes - prev_write_bytes
        elapsed_time = current_time - prev_time
        write_rate = bytes_written / elapsed_time  # bytes per second

        print(f"Write rate: {write_rate:.2f} bytes/sec")

        if write_rate > THRESHOLD:
            print(f"WARNING: High disk write activity detected! ({write_rate:.2f} B/s)")

        # Update counters
        prev_write_bytes = current_counters.write_bytes
        prev_time = current_time

except KeyboardInterrupt:
    print("\nMonitoring stopped.")

"""
5. Build a script that outputs:
- CPU count and utilization.
- Total and available memory.
- Disk usage of /.
- Number of active network connections.
"""

import psutil

# CPU count and utilization
cpu_count = psutil.cpu_count()
cpu_usage = psutil.cpu_percent(interval=1)

# Memory info
mem = psutil.virtual_memory()

# Disk usage for "/"
disk_usage = psutil.disk_usage("/")

# Active network connections
active_conn = psutil.net_connections(kind='inet')

print("Outputting System and Process Info... (Ctrl+C to stop)")
print(f"CPU Count: {cpu_count} | CPU Usage: {cpu_usage}%")
print(f"Total memory: {mem.total / (1024**3):.2f} GB")
print(f"Available memory: {mem.available / (1024**3):.2f} GB")
print(f"Disk Total: {disk_usage.total / (1024**3):.2f} GB")
print(f"Disk Used: {disk_usage.used / (1024**3):.2f} GB")
print(f"Disk Free: {disk_usage.free / (1024**3):.2f} GB")
print(f"Active network connections: {len(active_conn)}")

"""
6. Write a script that finds the top 5 processes by memory usage 
and prints their PID, name, and memory consumed.
"""
import psutil

running_processes = []

for process in psutil.process_iter(['pid', 'name', 'memory_info', 'status']):
    try:
        running_processes.append({
            "PID": process.pid,
            "Name": process.name(),
            "Memory (MB)": process.memory_info().rss / (1024 * 1024),  # convert bytes → MB
            "Status": process.status()
        })
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        continue  # skip processes you can't access

# Sort by memory usage in descending order
top_processes = sorted(running_processes, key=lambda p: p["Memory (MB)"], reverse=True) # By default Sorted() sorts in an ascending order.
                                                                                        # Use reverse=True to use descending order.
# Print top 5
for proc in top_processes[:5]:
    print(proc)

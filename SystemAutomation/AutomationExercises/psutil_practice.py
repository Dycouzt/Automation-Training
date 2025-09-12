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

"""
5. Build a script that outputs:
- CPU count and utilization.
- Total and available memory.
- Disk usage of /.
- Number of active network connections.
"""

"""
6. Write a script that finds the top 5 processes by memory usage 
and prints their PID, name, and memory consumed.
"""
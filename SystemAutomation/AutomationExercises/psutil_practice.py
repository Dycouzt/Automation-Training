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

    # Active connections list
    active_connections = []

    # Print all current active connections
    try:
        for conn in psutil.net_connections(kind='inet'):
            print("Active connection: ", conn)
            if conn != 80 & conn != 443:
                active_connections.append({
                    "Threat Port": {conn}
                })
    except (psutil.AccessDenied, psutil.NoSuchProcess, ValueError):
        return active_connections
    
print(port_security())
    
"""
3. Write a loop that prints CPU and memory usage every 2 seconds for 20 seconds 
while running another script in parallel.
"""

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
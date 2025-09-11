# psutil practice exercises.

import psutil

"""
1. Write a script that lists all running processes and prints only those using more than 10% CPU.
"""
def running_processes():
    ten_percent = []

    for process in psutil.process_iter(['pid','name']):
        if process.psutil.cpu_percent(interval=1):
            ten_percent.append(process)
    return ten_percent

running_processes()
            
        

"""
2. Create a function that prints all established network connections. 
Flag any connection not using port 80 or 443.
"""

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
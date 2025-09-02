"""
 Topic Review psutil module. it is a cross-platform library for retrieving information about:
System resources (CPU, memory, disks, network).
Running processes (start time, PID, memory/cpu usage, etc.).
 """

import psutil

# Process enumeration and inspection

for proc in psutil.process_iter(['pid', 'name', 'username']): # Iterate over running processes.
    print(proc.info)
# example output: {'pid': 1, 'name': 'systemd', 'username': 'root'}
#                 {'pid': 2345, 'name': 'python', 'username': 'diego'}

pid = 91283
psutil.Process(pid) # Inspect a specific process. (process ID)

# Process Details

p = psutil.Process(2345)
print(p.pid)         # 2345
print(p.name())      # 'python'
print(p.exe())       # '/usr/bin/python3.10'
print(p.cwd())       # Current working directory
print(p.cmdline())   # ['python', 'script.py']
print(p.username())  # 'diego'
print(p.status())    # 'running'
print(p.create_time())
print(p.cpu_percent(interval=1.0))
print(p.memory_info())
      
# CPU usage monitoring and information

psutil.cpu_percent(interval=1) # CPU utilization over 1 second.
psutil.cpu_count() # Number of cores.
psutil.cpu_times() # Breakdown of CPU time (user, system, idle).
""" example output: 
            12.5
            8
            scputimes(user=1200.1, system=500.3, idle=30000.0, ...)
"""

print(psutil.cpu_count(logical=True))   # counts hyper-threaded cores. e.g., 8
print(psutil.cpu_count(logical=False))  # physical cores only. e.g., 4

print(psutil.cpu_percent(interval=1))  # e.g., 12.5 (interval=1) -> waits 1 second before measuring.

print(psutil.cpu_times()) # Returns time spent by CPU in different modes (user, system, idle).
 # example output: scputimes(user=1234.56, system=789.01, idle=45678.9, ...)

# memory usage monitoring and information

mem = psutil.virtual_memory() # returns system memory stats
print(mem.total, mem.available, mem.used, mem.percent)
# Example output: 17179869184  1023456789  7890123456  45.8

print(psutil.swap_memory()) # Returns swap (paging) memory stats.
# Example output: sswap(total=2147483648, used=0, free=2147483648, percent=0.0, ...)

# Disk usage and I/O

print(psutil.disk_usage('/')) # (path) Storage usage.
print(psutil.disk_io_counters()) # read/write statistics.
""" expected output: 
        sdiskusage(total=500GB, used=300GB, free=200GB, percent=60)
        sdiskio(read_count=100000, write_count=50000, read_bytes=12345678, write_bytes=98765432)
"""

# Network connection and traffic

print(psutil.net_io_counters()) # Network I/O stats.
for conn in psutil.net_connections(kind='inet'): # List active network connections.
    print(conn.laddr, "->", conn.raddr, conn.status)
""" expected output: 
        snetio(bytes_sent=123456, bytes_recv=654321, packets_sent=1000, packets_recv=2000)
        127.0.0.1:54321 -> 93.184.216.34:80 ESTABLISHED
"""

psutil.net_if_addrs() # IP addresses per network interface.

# System uptime

import datetime

print(datetime.datetime.fromtimestamp(psutil.boot_time())) # System boot time.
# expected output: 2025-08-24 08:00:00
# Use case: forensic timeline (e.g., was the machine rebooted after compromise?).
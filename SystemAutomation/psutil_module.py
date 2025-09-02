"""
 Topic Review psutil module. it is a cross-platform library for retrieving information about:
System resources (CPU, memory, disks, network).
Running processes (start time, PID, memory/cpu usage, etc.).
 """

import psutil

# CPU Information

print(psutil.cpu_count(logical=True))   # counts hyper-threaded cores. e.g., 8
print(psutil.cpu_count(logical=False))  # physical cores only. e.g., 4

print(psutil.cpu_percent(interval=1))  # e.g., 12.5 (interval=1) -> waits 1 second before measuring.

print(psutil.cpu_times()) # Returns time spent by CPU in different modes (user, system, idle).
 # Example output: scputimes(user=1234.56, system=789.01, idle=45678.9, ...)

# Memory Information

mem = psutil.virtual_memory() # returns system memory stats
print(mem.total, mem.available, mem.used, mem.percent)
# Example output: 17179869184  1023456789  7890123456  45.8

print(psutil.swap_memory()) # Returns swap (paging) memory stats.


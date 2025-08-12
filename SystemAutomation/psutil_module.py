import psutil
import datetime

# CPU usage percentage
print(psutil.cpu_percent(interval=1))

# CPU usage per core
print(psutil.cpu_percent(interval=1, percpu=True))

# Number of physical cores and logical CPUs
print(psutil.cpu_count(logical=False))  # Physical cores
print(psutil.cpu_count(logical=True))   # Logical CPUs (includes hyperthreading)

# Virtual memory (RAM)
mem = psutil.virtual_memory()
print(mem.total)      # Total RAM in bytes
print(mem.available)  # Available RAM
print(mem.used)       # Used RAM
print(mem.percent)    # Usage percentage

# Swap memory
swap = psutil.swap_memory()
print(swap.total, swap.used, swap.percent)

# Disk partitions
print(psutil.disk_partitions())

# Disk usage
usage = psutil.disk_usage('/')
print(usage.total, usage.used, usage.percent)

# Disk I/O statistics
print(psutil.disk_io_counters())

# Network interface addresses
print(psutil.net_if_addrs())

# Network I/O statistics
print(psutil.net_io_counters())

# Per-interface network stats
print(psutil.net_io_counters(pernic=True)) 

# List all processes with their PID and name
for proc in psutil.process_iter(['pid', 'name']):
    print(proc.info)

boot_time = psutil.boot_time()
print(datetime.datetime.fromtimestamp(boot_time))

p = psutil.Process(1)  # Process with PID 1
print(p.name())        # Process name
print(p.status())      # Running, sleeping, etc.
print(p.cpu_percent(interval=1))
print(p.memory_info()) # Memory usage

import psutil

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
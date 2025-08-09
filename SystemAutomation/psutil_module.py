import psutil

# CPU usage percentage
print(psutil.cpu_percent(interval=1))

# CPU usage per core
print(psutil.cpu_percent(interval=1, percpu=True))

# Number of physical cores and logical CPUs
print(psutil.cpu_count(logical=False))  # Physical cores
print(psutil.cpu_count(logical=True))   # Logical CPUs (includes hyperthreading)
# subprocess practice exercises.

import subprocess

"""Use subprocess.run() to execute whoami and print the current user."""
def whoami():
    p = subprocess.run(["whoami"], capture_output=True, text=True)
    print(p.stdout.strip())  # strip() removes trailing newline

"""
Use ps (Linux/Mac) to list active processes. 
Capture and print only the first 5 lines of output.
"""
ps = subprocess.run(["ps", "aux"], capture_output=True, text=True)

# Split into lines and take the first 5
lines = ps.stdout.splitlines()[:5]

for line in lines:
    print(line)

"""
Write a script that takes a hostname (e.g., google.com) 
and pings it 3 times, displaying the result."""
import platform

def ping(hostname):
    # Determine the correct flag for the platform
    count_flag = "-n" if platform.system().lower() == "windows" else "-c"

    try:
        result = subprocess.run(
            ["ping", count_flag, "3", hostname],
            capture_output=True,
            text=True,
            check=True
        )
        print(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        print("Ping failed:")
        print(e.stderr.strip() if e.stderr else "Unknown error")
        
"""
Run netstat -an (Linux/Mac) or netstat -ano (Windows). 
Capture output, filter only ESTABLISHED connections, and print them.
"""

"""
Run a command that sleeps for 10 seconds. 
Set a timeout of 3 seconds and handle the exception.
"""

"""
Use Popen() to run echo "hello\nworld" and pipe it into grep "hello". 
Capture and print the result.
"""

"""
7. Write a script that runs ls -l (Linux/Mac) or dir (Windows) using subprocess, 
captures the output, and saves it into a file command_output.txt.
"""
# subprocess practice exercises.

import subprocess

""" 1. Use subprocess.run() to execute whoami and print the current user."""
def whoami():
    p = subprocess.run(["whoami"], capture_output=True, text=True)
    print(p.stdout.strip())  # strip() removes trailing newline

"""
2. Use ps (Linux/Mac) to list active processes. 
Capture and print only the first 5 lines of output.
"""
ps = subprocess.run(["ps", "aux"], capture_output=True, text=True)

# Split into lines and take the first 5
lines = ps.stdout.splitlines()[:5]

for line in lines:
    print(line)

"""
3. Write a script that takes a hostname (e.g., google.com) 
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
4. Run netstat -an (Linux/Mac) or netstat -ano (Windows). 
Capture output, filter only ESTABLISHED connections, and print them.
"""
# Determine the correct command based on OS
if platform.system() == "Windows":
    cmd = ["netstat", "-ano"]
else:
    cmd = ["netstat", "-an"]

# Run the command and capture output
result = subprocess.run(cmd, capture_output=True, text=True)

# Split output into lines
lines = result.stdout.splitlines()

# Filter lines containing 'ESTABLISHED'
established = [line for line in lines if "ESTABLISHED" in line]

# Print filtered connections
for conn in established:
    print(conn)

"""
5. Run a command that sleeps for 10 seconds. 
Set a timeout of 3 seconds and handle the exception.
"""
try:
    subprocess.run(
        ["sleep", "10"],   # Command that actually sleeps 10s
        timeout=3       
    )
except subprocess.TimeoutExpired:
    print("Process timeout!")

"""
6. Use Popen() to run echo "hello\nworld" and pipe it into grep "hello". 
Capture and print the result.
"""
process = subprocess.Popen(
    "printf 'hello\nworld' | grep 'hello'",
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    shell=True
)

stdout, stderr = process.communicate()

print("STDOUT:", stdout.decode().strip())
print("STDERR:", stderr.decode().strip())
print("Return Code:", process.returncode)

"""
7. Write a script that runs ls -l (Linux/Mac) or dir (Windows) using subprocess, 
captures the output, and saves it into a file command_output.txt.
"""
# Run 'ls -l' and redirect output directly to a file
with open("command_output.txt", "w") as f:
    process = subprocess.Popen(["ls", "-l"], stdout=f, stderr=subprocess.PIPE)
    _, stderr = process.communicate()

if process.returncode == 0:
    print("Output saved to command_output.txt")
else:
    print("Error:", stderr.decode())
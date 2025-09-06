# Topic Review subprocess module.

import subprocess

subprocess.run() # Simplest way to run a command. Waits until command finishes and returns a CompletedProcess object.

result = subprocess.run(["echo", "Hello"], capture_output=True, text=True) # example.
print(result.stdout) # expected output: "Hello".

subprocess.Popen() # More advanced; allows asynchronous process execution.
proc = subprocess.Popen(["ping", "-c", "2", "google.com"], stdout=subprocess.PIPE, text=True)
output, _ = proc.communicate() 
print(output)
""" expected output: PING google.com (142.250.187.46): 56 data bytes
64 bytes from 142.250.187.46: icmp_seq=0 ttl=115 time=15.2 ms
64 bytes from 142.250.187.46: icmp_seq=1 ttl=115 time=14.9 ms
"""


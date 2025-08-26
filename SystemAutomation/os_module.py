# Topic Review OS Module

import os

print(os.getcwd())  # Returns the current working directory.

print(f"before: {os.getcwd()}")
os.chdir("/python/LogThreatDetection")
print(f"after: {os.getcwd()}")


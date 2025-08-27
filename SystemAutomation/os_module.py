# Topic Review OS Module

import os

print(os.getcwd())  # Returns the current working directory.

print(f"before: {os.getcwd()}")
os.chdir("../Modules") # Changes working directory.
print(f"after: {os.getcwd()}")

print(os.listdir(".")) # Lists all files in the current directory. os.listdir(path=".")


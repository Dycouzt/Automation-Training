# Topic Review OS Module

import os

print(os.getcwd())  # Returns the current working directory.

print(f"before: {os.getcwd()}")
os.chdir("../Modules") # Changes working directory.
print(f"after: {os.getcwd()}")

print(os.listdir(".")) # Lists all files in the current directory. os.listdir(path=".")

os.mkdir("new_folder") # Creates a single new directory in the current path.
os.makedirs("new_folder/nested_folder", exist_ok=True) # This won't raise error if the folder already exists.
print(os.listdir("new_folder")) # Expected output: "nested_folder"



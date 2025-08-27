# Topic Review OS Module

import os

print(os.getcwd())  # Returns the current working directory.

print(f"before: {os.getcwd()}")
os.chdir("../Modules") # Changes working directory.
print(f"after: {os.getcwd()}")

print(os.listdir(".")) # Lists all files in the current directory. os.listdir(path=".")

os.mkdir("new_directory") # Creates a single new directory in the current path.
os.makedirs("new_directory_2.0/nested_folder", exist_ok=True) # This won't raise error if the folder already exists.
print(os.listdir("new_directory_2.0")) # Expected output: "nested_folder"

os.remove("image.txt") # Deletes file "image.txt"
os.rmdir("new_directory") # Deletes a single directory.
os.removedirs("new_directory_2.0/nested_folder") # Removes folder and then "nested" if empty.

os.rename("image.txt", "background.txt") # Renames a file.



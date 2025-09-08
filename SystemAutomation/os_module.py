# Topic Review OS Module, essential for file, directory, and environment management.

import os # Key Idea: "raw building blocks"

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

path = os.path.join("logs", "app.log")  # Safely build a path by joining folder and file name
data_file = os.path.join("base_dir", "data", "input.csv")  # Create a cross-platform path to the data file
file_path = os.path.join("folder", "filename")  # Combine directory path and filename into a full path

print(os.path.exists("file.txt"))  # Checks if a file exists. (True/False) 
print(os.path.isfile("file.txt")) # Checks if path is a file.
print(os.path.isdir("folder")) # Checks if path is a directory.

print(os.path.abspath("file.txt")) # Returns the absolute path.

print(os.environ)  # Prints a mapping of all environment variables
'''
Expected Output:
environ({
  'PATH': '/usr/bin:/bin:/usr/local/bin',
  'HOME': '/Users/diego',
  'SHELL': '/bin/zsh',
  'LANG': 'en_US.UTF-8'
})
'''
os.system("echo Hello World")  # Runs terminal command. Important for automation scripts.

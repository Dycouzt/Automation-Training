import os


''' Example usage: 
os.mkdir('new_folder')
os.rename('old_name.txt', 'new_name.txt')
print(os.getenv('HOME'))
'''

# Create a directory
os.mkdir("new_folder")

# List contents of a directory
print(os.listdir("."))  # Lists files in current directory

# Rename a file or folder
os.rename("new_folder", "renamed_folder")

# Remove a file
os.remove("example.txt")

# Remove a directory (must be empty)
os.rmdir("renamed_folder")

# Join paths safely
full_path = os.path.join("/home/user", "file.txt")

# Check existence
print(os.path.exists(full_path))

# Check if it's a file or directory
print(os.path.isfile(full_path))
print(os.path.isdir(full_path))

# Get file size
print(os.path.getsize(full_path))

# Get absolute path
print(os.path.abspath("file.txt"))
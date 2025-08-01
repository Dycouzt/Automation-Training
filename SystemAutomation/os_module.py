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

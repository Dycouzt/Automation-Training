# Topic Review pathlib module. Used for object-oriented filesystem paths. Replaces some OS and OS.path functions.

from pathlib import Path

print(Path.cwd) # Prints current working directory.

p = Path("folder/subfolder/image.txt")
print(p) # Creates a path object.

print(Path.home) # Returns the user’s home directory.

print(p.Path.exists) # Checks if a path exists.

p2 = Path("file.txt")
print(p.is_file()) # Distinguishes between files and directories.
print(p.is_dir())

p3 = Path(".")
for item in p.iterdir(): # Iterates through directory contents.
    print(item) 
    """
      Example output: file1.txt file2.py subfolder within the cwd.
    """
Path.mkdir("new_folder") # Creates a new folder, same as os.mkdir


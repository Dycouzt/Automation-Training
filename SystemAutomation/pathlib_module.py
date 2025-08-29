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


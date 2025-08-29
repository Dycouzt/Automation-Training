# Topic Review pathlib module. Used for object-oriented filesystem paths. Replaces some OS and OS.path functions.

from pathlib import Path

print(Path.cwd) # Prints current working directory.
p = Path("folder/subfolder/image.txt")
print(p) # Creates a path object.


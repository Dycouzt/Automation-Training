# Topic Review pathlib module. Used for object-oriented filesystem paths. Replaces some OS and OS.path functions.

from pathlib import Path # Key Idea: "modern path manager"

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
p = Path("new_folder")
p.mkdir(exist_ok=True)  # exist_ok prevents error if it already exists

Path("new_folder").rmdir() # Removes a given directory. Must be empty in order to be successful.
p = Path("old.txt")
p.rename("new.txt") # Renames a given directory.

p = Path("folder/subfolder/file.txt")
print(p.name)     # file.txt
print(p.stem)     # file
print(p.suffix)   # .txt
print(p.parent)   # folder/subfolder
print(p.parts)    # ('folder', 'subfolder', 'file.txt')

p = Path("hello.txt")
p.write_text("Hello, World!") # Convenient way to writing and reading text to small files.
print(p.read_text())

p = Path(".")
for file in p.glob("*.py"): # Finds files matching a pattern.
    print(file)




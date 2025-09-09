# os module practice exercises.

import os

"""
1. Create a script that:
    - Creates a new directory named practice.
    - Changes into that directory.
    - Creates three empty files: a.txt, b.txt, c.txt.
    - Lists all files in the directory.
"""
"""
def practice_directory_creation():
    # Create 'practice' directory if it doesn't exist
    os.makedirs("practice", exist_ok=True)
    print("Directory 'practice' created (or already exists).")

    # Change into the new directory
    os.chdir("practice")
    print("Changed into directory:", os.getcwd())

    # Create three empty files
    for filename in ["a.txt", "b.txt", "c.txt"]:
        open(filename, "w").close()
    print("Empty files created: a.txt, b.txt, c.txt")

    # List files in the directory
    print("Files inside 'practice':", os.listdir("."))

practice_directory_creation()
"""
"""
2. Write a function that takes a directory path and prints:
All files.
All subdirectories.
Absolute paths of each file.
"""
def fls_and_subdirs(dir_path):
    os.listdir(dir_path)
    for dir in dir_path:
        os.path.abspath()

fls_and_subdirs("Networking")

"""
3. Write a script that:
Checks if notes.txt exists.
If yes, renames it to notes_old.txt.
If no, creates an empty notes.txt.
"""

"""
4. Write a script that:
Reads the environment variable PATH.
Splits it by : (or ; on Windows).
Prints each path component on a new line.
"""

"""
5. Write a script that deletes all .tmp files inside the current directory and its subdirectories.
"""
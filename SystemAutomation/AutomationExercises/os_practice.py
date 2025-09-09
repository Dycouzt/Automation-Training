# os module practice exercises.

import os
import pathlib as Path

# cwd: /Users/dieacost/Documents/Dycouzt/Python/Training/Networking/SystemAutomation/AutomationExercises/os_practice.py

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

def fls_and_subdirs():

    script_dir = Path(__file__).resolve().parent

    networking_dir = script_dir.parent.parent / "Networking"

    for item in os.listdir(networking_dir):
        full_path = os.path.join(networking_dir, item)  # Safe join
        abs_path = os.path.abspath(full_path)

        if os.path.isfile(full_path):
            print(f"File: {item} | Absolute Path: {abs_path}")
        elif os.path.isdir(full_path):
            print(f"Directory: {item} | Absolute Path: {abs_path}")

fls_and_subdirs("")

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
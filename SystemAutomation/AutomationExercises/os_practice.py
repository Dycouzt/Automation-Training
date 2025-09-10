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
2. Write a function that takes a directory path and prints:
All files.
All subdirectories.
Absolute paths of each file.
"""

def fls_and_subdirs():

    # Establish the parent directory of your script in order to call it from everywhere.
    script_dir = Path(__file__).resolve().parent 
    networking_dir = script_dir.parent.parent / "Networking"

    # pathlib instead of os because of modernity
    for item in networking_dir.iterdir():
        if item.is_file():
            print(f"File: {item.name} | Absolute Path: {item.resolve()}")
        elif item.is_dir():
            print(f"Directory: {item.name} | Absolute Path: {item.resolve()}")

fls_and_subdirs()

"""
3. Write a script that:
Checks if notes.txt exists.
If yes, renames it to notes_old.txt.
If no, creates an empty notes.txt.
"""
def fls_checker():
    base_dir = "/Users/dieacost/Documents/Dycouzt/Python/Training/Networking/SystemAutomation/AutomationExercises"
    notes_path = os.path.join(base_dir, "notes.txt")
    old_notes_path = os.path.join(base_dir, "old_notes.txt")

    if os.path.exists(notes_path):
        os.rename(notes_path, old_notes_path)
        print("notes.txt renamed to old_notes.txt.")
    else:
        open(notes_path, "x").close()
        print("notes.txt created.")

fls_checker()

"""
4. Write a script that:
Reads the environment variable PATH.
Splits it by : (or ; on Windows).
Prints each path component on a new line.
"""
def env_read():
    # Get PATH environment variable
    path_value = os.environ.get('PATH')
    
    if path_value is None:
        print("PATH variable not found.")
        return
    
    # Use os.pathsep (handles ':' on Linux/Mac, ';' on Windows)
    path_entries = path_value.split(os.pathsep)
    
    # Print each entry
    for entry in path_entries:
        print(entry)

# Run the function
env_read()
"""
5. Write a script that deletes all .tmp files inside the current directory and its subdirectories.
"""
def tmp_deleting():

    files = []
    tmp_files_dict = []

    base_dir = "/Users/dieacost/Documents/Dycouzt/Python/Training/Networking/SystemAutomation/AutomationExercises"
    for file in os.listdir(base_dir):
        if file.is_file():
            file.append(files)
            full_path = os.path.join(base_dir, "file")
            abs_path = os.path.abspath(full_path)

            if abs_path 
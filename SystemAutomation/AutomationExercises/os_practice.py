# os module practice exercises.

import os

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
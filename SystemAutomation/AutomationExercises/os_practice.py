# os module practice exercises.

import os

"""
1. Create a script that:
    - Creates a new directory named practice.
    - Changes into that directory.
    - Creates three empty files: a.txt, b.txt, c.txt.
    - Lists all files in the directory.
"""

print(os.getcwd())

def practice_directory_creation():
    
    # Create directory (ignore if it already exists)
    os.makedirs("practice", exist_ok=True) # exist_ok=True only usable for os.mkdirs! 
    print("success! ")
    expected_cwd = os.path.join(os.getcwd(), "practice")
    cwd = os.getcwd()
    print("Current working directory:", cwd)

    # Change into it
    if cwd == expected_cwd:
        os.chdir("practice")
    else:
         print("practice directory doesn't exist yet! ")

    # Create three empty files
    for filename in ["a.txt", "b.txt", "c.txt"]:
            open(filename, "w").close()     # "W" means write. Important to .close() after creating files.
    print("practice directory not exists yet! ")
    
     # List files
    print(os.listdir("."))

practice_directory_creation()
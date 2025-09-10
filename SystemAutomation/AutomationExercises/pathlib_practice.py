# pathlib practice exercises.

import pathlib as Path

# cwd: /Users/dieacost/Documents/Dycouzt/Python/Training/Networking/SystemAutomation/AutomationExercises/pathlib_practice.py

"""
1. Create a Path object pointing to your home directory. Print its .parts, .parent, and .name.
"""
def home_path():
    home_dir = Path.home()
    print(f"The home directory parts are: ",  home_dir.parts)
    print(f"The home directory's parent directory is: ", home_dir.parent)
    print(f"The home directory's name is: ", home_dir.name)

home_path()

"""
2. Create a folder called practice_pathlib. 
Inside it, create three text files (a.txt, b.txt, c.txt) with some text using .write_text(). 
List all files with .iterdir().
"""
def folder_creation():
    # create folder
    p = Path("practice_pathlib")
    p.mkdir(exist_ok=True)

    # create text files with content
    for filename in ["a.txt", "b.txt", "c.txt"]:
        (p / filename).write_text("Hello")

    # list all items in directory
    for item in p.iterdir():
        print(item)

folder_creation()

"""
3. Write a script that checks if notes.txt exists.
If yes, read and print its content.
If not, create it and write "New notes file created!".
"""

"""
4. In your current directory, find all .py files using .glob("*.py")
and print their absolute paths.
"""

"""
5. Rename a.txt to alpha.txt and delete b.txt.
"""

"""
6. Write a script that searches recursively for all .log files inside your home directory 
and prints their sizes in bytes.
"""
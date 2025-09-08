# os module practice exercises.

import os

print(os.getcwd())

def practice_directory_creation():
    os.makedirs("practice", exist_ok=True) # exist_ok=True only usable for os.mkdirs! 
    print("success! ")

    expected_cwd = os.path.join(os.getcwd(), "practice")
    cwd = os.getcwd()
    print(cwd)

    if cwd == expected_cwd:
        os.chdir("practice")
    else:
         print("practice directory doesn't exist yet! ")

    for filename in ["a.txt", "b.txt", "c.txt"]:
            open(filename, "w").close()     # "W" means write. Important to .close() after creating files.
    print("practice directory not exists yet! ")
    
    print(os.listdir("."))

practice_directory_creation()
# shutil practice exercises.

import shutil
import os
from pathlib import Path
from datetime import datetime

""" 1. Copy logs.txt to backup/logs_backup.txt using copy2."""

# Ensure backup directory exists
os.makedirs("backup", exist_ok=True)

# Copy file with metadata preserved
if os.path.exists("logs.txt"):
    shutil.copy2("logs.txt", "backup/logs_backup.txt")
    print("logs.txt successfully copied to backup/logs_backup.txt")
else:
    print("logs.txt not found")

""" 2. Copy the directory dataset/ to dataset_backup/, 
ensuring it works even if the backup directory already exists.
"""

def backup(directory):
    dataset = Path(directory).resolve()

    # Create a timestamp string like 2025-09-14_17-30-45
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    dataset_backup = dataset.parent / f"dataset_backup_{timestamp}"

    if dataset.exists() and dataset.is_dir():
        shutil.copytree(dataset, dataset_backup)
        print(f"Backup completed: {dataset} → {dataset_backup}")
    else:
        print(f"Error: {dataset} does not exist or is not a directory.")

backup("dataset")

""" 
3. Move all .txt files from downloads/ to organized/. 
Rename important.txt to important_backup.txt while moving.
"""
def move_txt():
    downloads = Path("downloads").resolve()
    organized = Path("organized").resolve()
    important_txt = downloads / "important.txt"

    for file in downloads.iterdir():
        if file.is_file() and file.suffix == ".txt":
            if file == important_txt:
                shutil.move(file, organized / "important_backup.txt")
                print(f"{file.name} has been moved and renamed to important_backup.txt")
            else:
                shutil.move(file, organized)
                print(f"{file.name} has been successfully moved to organized/")

move_txt()

""" 4. Create a zip archive of the dataset/ directory and extract it to restored_dataset/."""


""" 
5. Write a script that prints total, used, and free space of /. 
Add a warning if free space is below 10%.
"""


""" 6. Create a temporary directory temp_analysis/ with some files, then delete the directory with rmtree."""


"""7. Write a script that archives the directory logs/ into a timestamped .zip file (e.g., logs_2025-09-05.zip)."""
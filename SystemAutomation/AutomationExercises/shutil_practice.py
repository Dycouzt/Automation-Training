# shutil practice exercises.

import shutil
import os
from pathlib import Path

""" 1. Copy logs.txt to backup/logs_backup.txt using copy2."""

# Ensure backup directory exists
os.makedirs("backup", exist_ok=True)

# Copy file with metadata preserved
if os.path.exists("logs.txt"):
    shutil.copy2("logs.txt", "backup/logs_backup.txt")
    print("logs.txt successfully copied to backup/logs_backup.txt")
else:
    print("logs.txt not found")

""" 2. Copy the directory dataset/ to dataset_backup/, ensuring it works even if the backup directory already exists."""
import shutil
from pathlib import Path

def backup(directory):
    dataset = Path(directory).resolve()
    dataset_backup = dataset.parent / "dataset_backup"

    if dataset.exists() and dataset.is_dir():
        dataset_backup.mkdir(exist_ok=True)
        shutil.copytree(dataset, dataset_backup, dirs_exist_ok=True)
        print(f"Backup completed: {dataset} → {dataset_backup}")
    else:
        print(f"Error: {dataset} does not exist or is not a directory.")

backup("dataset")


""" 3. Move all .txt files from downloads/ to organized/. Rename important.txt to important_backup.txt while moving."""


""" 4. Create a zip archive of the dataset/ directory and extract it to restored_dataset/."""


""" 5. Write a script that prints total, used, and free space of /. Add a warning if free space is below 10%."""


""" 6. Create a temporary directory temp_analysis/ with some files, then delete the directory with rmtree."""


"""7. Write a script that archives the directory logs/ into a timestamped .zip file (e.g., logs_2025-09-05.zip)."""
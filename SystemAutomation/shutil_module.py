# Topic Review shutil module. shutil stands for shell utilities.

import shutil

shutil.copy("data.csv", "backup_data.csv")
"""
Copies a file from src to dst. Preserves content but not metadata (permissions, timestamps).
In this case, "data.csv" is copied as "backup_data.csv" in the same directory.
"""
shutil.copy("data.csv", "backup_data_metadata.csv") # Copies a file and preserves metadata.

shutil.copytree("dataset", "dataset_backup", dirs_exist_ok=True)
"""
Copies an entire directory tree.
dirs_exist_ok=True allows merging into an existing directory.
"""

shutil.move("old_logs/log1.txt", "archived_logs/log1.txt") # moves a folder to another location.

shutil.rmtree("temp_folder") # Deletes an entire tree directory. Use with caution.


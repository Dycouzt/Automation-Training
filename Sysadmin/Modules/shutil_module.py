# Topic Review shutil module. shutil stands for shell utilities.

import shutil # Key Idea: "file manager / archiver"

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

usage = shutil.disk_usage("/") # Returns total, used, and free space of a filesystem.
print(usage) # Use case: Monitor disk space for large AI datasets or logs.

shutil.make_archive("base_name", "format", "root_dir") # creates an archive (zip, tar, etc.) of a directory.
shutil.make_archive("dataset_backup", "zip", "dataset") # example.
# Use case: Archiving evidence in cybersecurity or compressing training datasets.

shutil.unpack_archive("filename", extract_dir=None) # Extracts archives (zip, tar, etc.) to a folder.
shutil.unpack_archive("dataset_backup.zip", "restored_dataset") # example.

"""
Key takeaways

- shutil complements os and pathlib for high-level file operations.
- Use these functions to backup data, automate evidence collection, manage datasets, or clean up temporary 
directories safely.
"""


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

"""
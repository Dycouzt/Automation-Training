import shutil

# Copy a file (contents + permissions)
shutil.copy("source.txt", "destination.txt")

# Copy a file with metadata (permissions, timestamps)
shutil.copy2("source.txt", "destination.txt")

# Copy an entire directory
shutil.copytree("source_folder", "destination_folder")
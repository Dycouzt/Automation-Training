from pathlib import Path

p = Path('example.txt')
if p.exists():
    print(p.read_text())

# Current directory
p = Path('.')

# Home directory
home = Path.home()

# Absolute path
abs_path = p.resolve()

data_path = Path("/home/user") / "documents" / "file.txt"
print(data_path)  # /home/user/documents/file.txt

p = Path('example.txt')

print(p.exists())       # True if the path exists
print(p.is_file())      # True if it's a file
print(p.is_dir())       # True if it's a directory
print(p.name)           # example.txt
print(p.suffix)         # .txt
print(p.stem)           # example
print(p.parent)         # path to parent directory
print(p.stat().st_size) # file size in bytes

# Create directory
Path("my_folder").mkdir()

# Create nested directories (if not existing)
Path("parent/child").mkdir(parents=True, exist_ok=True)

# Create a file (touch equivalent)
Path("empty.txt").touch()

# Write text to a file
Path("note.txt").write_text("System automation with pathlib")

# Read text from a file
content = Path("note.txt").read_text()
print(content)
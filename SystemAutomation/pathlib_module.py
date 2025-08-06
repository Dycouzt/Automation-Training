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


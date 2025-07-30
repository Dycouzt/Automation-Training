from pathlib import Path

p = Path('example.txt')
if p.exists():
    print(p.read_text())
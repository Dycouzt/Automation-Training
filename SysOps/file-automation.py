"""
List files recursively in a directory and filter by extension.
Monitor a directory for changes (creation/modification/deletion).
Automate backups: Copy files from one directory to another with timestamped folders.
Parse log files: Count error/warning lines from system/application logs.
"""
import time, datetime, shutil, re
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from collections import defaultdict

base_dir = Path(__file__).resolve().parent

def filter_extension(ext="*.log"):
    return [f for f in base_dir.rglob(ext)]

def get_backup(files):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_dir = base_dir / f"backup_{timestamp}"
    backup_dir.mkdir(exist_ok=True)
    for file in files:
        shutil.copy(file, backup_dir)
    print(f"Backup created: {backup_dir}")

def log_parse(log_files):
    pattern = re.compile(r"\bERROR\b")
    error_count = defaultdict(int)
    for file in log_files:
        with file.open() as f:
            for line in f:
                if pattern.search(line):
                    date = line.split()[0]
                    error_count[date] += 1
    return error_count

class Handler(FileSystemEventHandler):
    def on_modified(self, event): print(f"Modified: {event.src_path}")
    def on_created(self, event): print(f"Created: {event.src_path}")
    def on_deleted(self, event): print(f"Deleted: {event.src_path}")

class Watcher:
    def __init__(self, directory):
        self.directory = directory
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, str(self.directory), recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

if __name__ == "__main__":
    logs = filter_extension("*.log")
    get_backup(logs)
    print(log_parse(logs))
    Watcher(base_dir).run()

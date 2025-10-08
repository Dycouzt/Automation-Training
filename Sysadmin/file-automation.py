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

# List files recursively and filter by ".log" extension
def filter_extension(match):
    files = [item for item in base_dir.rglob(match)]

    for file in files:
        print(file)

# Automate backup of files filtered by given extension. 
def get_backup(intended_backup):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_dir = base_dir / f"files_backup_{timestamp}"

    if intended_backup.exists():
        shutil.copytree(intended_backup, backup_dir)
        print(f"{intended_backup} backup created to {backup_dir} -> {timestamp}")
    else:
        print(f"Files for backup not found. ")

# Parse given logs 
def log_parse(log_files):
    pattern = re.compile(r"/bERROR/b")
    error_counts = defaultdict(int)
    for file in log_files:
        with file.open("r") as f:
            for line in f:
                if pattern.search(line):
                    date = line.split()[0]
                    error_counts[date] += 1
    return error_counts
                

# Monitor directory for changes.
class Watcher:
    def __init__(self, directory_to_watch):
        self.DIRECTORY_TO_WATCH = directory_to_watch
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"Modified: {event.src_path}")

    def on_created(self, event):
        print(f"Created: {event.src_path}")

    def on_deleted(self, event):
        print(f"Deleted: {event.src_path}")


if __name__ == '__main__':
    intended_backup = filter_extension("**.log")
    path = "/path/to/watch"
    Watcher(path).run()

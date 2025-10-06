"""
List files recursively in a directory and filter by extension.
Monitor a directory for changes (creation/modification/deletion).
Automate backups: Copy files from one directory to another with timestamped folders.
Parse log files: Count error/warning lines from system/application logs.
"""

from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

base_dir = Path(__file__).resolve().parent

def filter_extension():
    files = [item for item in base_dir.iterdir() if item.is_file()]

    for files in files:
        file_ext = r.compile(r'/./w+')
        print(file_ext)

filter_extension()

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
    path = "/path/to/watch"
    Watcher(path).run()

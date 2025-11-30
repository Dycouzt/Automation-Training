"""
Detect and delete duplicate files in a directory.
Rotate log files older than X days.
Automatically restart failed services.
Parse configuration files (INI/YAML/JSON) and apply validation rules.
"""

import os
import hashlib
import subprocess
import configparser
from datetime import datetime, timedelta

# 1. Detect and Delete Duplicate Files
def detect_and_delete_duplicates(directory, dry_run=True):
    """
    Detects and optionally deletes duplicate files in a directory based on their content.

    Args:
        directory (str): The path to the directory to scan.
        dry_run (bool): If True, only logs duplicates; if False, deletes them.
    """
    hashes = {}
    duplicates = []
    print(f"\n--- Task 1: Detecting Duplicate Files in '{directory}' ---\n")
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            try:
                with open(path, 'rb') as f:
                    file_hash = hashlib.sha256(f.read()).hexdigest()
                if file_hash in hashes:
                    duplicates.append((path, hashes[file_hash]))
                else:
                    hashes[file_hash] = path
            except (IOError, OSError) as e:
                print(f"Could not read {path}: {e}")

    if duplicates:
        print("Duplicate files found:")
        for dup, orig in duplicates:
            print(f"  '{dup}' is a duplicate of '{orig}'")
            if not dry_run:
                try:
                    os.remove(dup)
                    print(f"    -> Deleted '{dup}'")
                except OSError as e:
                    print(f"    -> Error deleting '{dup}': {e}")
    else:
        print("No duplicate files found.")

# 2. Rotate Log Files
def rotate_log_files(log_dir, retention_days=7):
    """
    Rotates log files older than a specified number of days.

    Args:
        log_dir (str): The directory containing log files.
        retention_days (int): The number of days to keep logs.
    """
    print(f"\n--- Task 2: Rotating Log Files in '{log_dir}' (Retention: {retention_days} days) ---\n")
    if not os.path.isdir(log_dir):
        print(f"Log directory '{log_dir}' not found.")
        return

    cutoff = datetime.now() - timedelta(days=retention_days)
    for filename in os.listdir(log_dir):
        path = os.path.join(log_dir, filename)
        if os.path.isfile(path):
            try:
                file_mod_time = datetime.fromtimestamp(os.path.getmtime(path))
                if file_mod_time < cutoff:
                    print(f"'{filename}' is older than {retention_days} days. Archiving...")
                    # In a real script, you would compress and move the file.
                    # For this example, we'll just print the action.
                    # e.g., shutil.move(path, f"{path}.old")
            except OSError as e:
                print(f"Could not process {path}: {e}")

# 3. Automatically Restart Failed Services
def check_and_restart_service(service_name):
    """
    Checks if a service is running and restarts it if it's not.

    Args:
        service_name (str): The name of the service to check (e.g., 'ssh', 'nginx').
    """
    print(f"\n--- Task 3: Checking and Restarting Service '{service_name}' ---\n")
    try:
        # Use systemctl to check if the service is active
        subprocess.run(['systemctl', 'is-active', '--quiet', service_name], check=True)
        print(f"Service '{service_name}' is running.")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print(f"Service '{service_name}' is not running. Attempting to restart...")
        try:
            # Attempt to restart the service
            subprocess.run(['systemctl', 'restart', service_name], check=True)
            print(f"Service '{service_name}' restarted successfully.")
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            print(f"Failed to restart service '{service_name}': {e}")

# 4. Parse and Validate Configuration Files
def validate_config_file(config_path):
    """
    Parses an INI configuration file and validates its contents.

    Args:
        config_path (str): The path to the configuration file.
    """
    print(f"\n--- Task 4: Validating Configuration File '{config_path}' ---\n")
    if not os.path.exists(config_path):
        print(f"Configuration file '{config_path}' not found.")
        return

    config = configparser.ConfigParser()
    config.read(config_path)
    errors = []

    # Validate [server] section
    if 'server' in config:
        if not config.has_option('server', 'host'):
            errors.append("Missing 'host' in [server] section.")
        if not config.has_option('server', 'port'):
            errors.append("Missing 'port' in [server] section.")
        else:
            try:
                port = config.getint('server', 'port')
                if not (1 <= port <= 65535):
                    errors.append(f"Invalid port '{port}'. Must be between 1 and 65535.")
            except ValueError:
                errors.append("'port' in [server] is not a valid integer.")
    else:
        errors.append("Missing [server] section.")

    # Validate [database] section
    if 'database' in config:
        if not config.has_option('database', 'user'):
            errors.append("Missing 'user' in [database] section.")
        if not config.has_option('database', 'password'):
            errors.append("Missing 'password' in [database] section.")
    else:
        errors.append("Missing [database] section.")

    if errors:
        print("Configuration validation failed:")
        for error in errors:
            print(f"  - {error}")
    else:
        print("Configuration validation successful.")


def main():
    """Main function to run the challenges."""
    # --- Challenge 1: Duplicate File Detection ---
    # Create a dummy directory with some files to test duplicate detection
    dummy_dir = 'test_duplicates'
    if not os.path.exists(dummy_dir):
        os.makedirs(dummy_dir)
    with open(os.path.join(dummy_dir, 'file1.txt'), 'w') as f:
        f.write('hello')
    with open(os.path.join(dummy_dir, 'file2.txt'), 'w') as f:
        f.write('world')
    with open(os.path.join(dummy_dir, 'file3.txt'), 'w') as f:
        f.write('hello') # Duplicate of file1.txt
    detect_and_delete_duplicates(dummy_dir)

    # --- Challenge 2: Log Rotation ---
    # Create a dummy log directory and some old files
    log_dir = 'test_logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    with open(os.path.join(log_dir, 'log1.log'), 'w') as f:
        f.write('log entry')
    # Create an old file
    old_file_path = os.path.join(log_dir, 'log2.log')
    with open(old_file_path, 'w') as f:
        f.write('old log entry')
    two_weeks_ago = datetime.now() - timedelta(weeks=2)
    os.utime(old_file_path, (two_weeks_ago.timestamp(), two_weeks_ago.timestamp()))
    rotate_log_files(log_dir, retention_days=7)

    # --- Challenge 3: Service Restart ---
    # This requires a service that can be controlled by systemd.
    # Replace 'non_existent_service' with a real service name for testing.
    check_and_restart_service('non_existent_service')

    # --- Challenge 4: Configuration Validation ---
    validate_config_file('config.ini')

if __name__ == "__main__":
    main()

for c in images:
    print(c)
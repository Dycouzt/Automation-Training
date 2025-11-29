"""
4. System Observability and Monitoring
- Collect system metrics (CPU, RAM, disk, network) with psutil and store them in a time-series format.
- Build a real-time alert system that sends Slack/webhook alerts on thresholds.
- Write a service availability checker that retries failed endpoints with exponential backoff.
- Implement a log rotation and archival system with compression and retention policies.
"""

import psutil
import time
import requests
import logging
import os
import shutil
import gzip
import datetime
import json

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def collect_metrics():
    """Collect system metrics (CPU, RAM, disk, network)."""
    metrics = {
        "timestamp": datetime.datetime.now().isoformat(),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent,
        "net_io": psutil.net_io_counters()._asdict()
    }
    return metrics

def simple_alert(message):
    """Print alert message to console/log if thresholds are breached."""
    # In a real scenario, this might send an email or Slack message
    logging.warning(f"ALERT: {message}")

def check_thresholds(metrics):
    """Check metrics against thresholds and trigger alerts."""
    if metrics['cpu_percent'] > 80:
        simple_alert(f"High CPU usage: {metrics['cpu_percent']}%")
    if metrics['memory_percent'] > 80:
        simple_alert(f"High Memory usage: {metrics['memory_percent']}%")
    if metrics['disk_percent'] > 90:
        simple_alert(f"High Disk usage: {metrics['disk_percent']}%")

def check_service_availability(url, max_retries=3):
    """Check if a URL is reachable with exponential backoff."""
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                logging.info(f"Service {url} is UP.")
                return True
            else:
                logging.warning(f"Service {url} returned status {response.status_code}.")
        except requests.RequestException as e:
            logging.warning(f"Service {url} check failed: {e}")
        
        wait_time = 2 ** retries
        logging.info(f"Retrying in {wait_time} seconds...")
        time.sleep(wait_time)
        retries += 1
    
    simple_alert(f"Service {url} is DOWN after {max_retries} retries.")
    return False

def rotate_logs(log_file, retention_days=7):
    """Compress old logs and delete logs older than retention period."""
    if not os.path.exists(log_file):
        return

    # Compress current log
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    compressed_log = f"{log_file}.{timestamp}.gz"
    
    with open(log_file, 'rb') as f_in:
        with gzip.open(compressed_log, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    
    # Clear current log file
    open(log_file, 'w').close()
    logging.info(f"Rotated log to {compressed_log}")

    # Cleanup old logs
    cutoff_date = datetime.datetime.now() - datetime.timedelta(days=retention_days)
    log_dir = os.path.dirname(log_file) or "."
    
    for filename in os.listdir(log_dir):
        if filename.startswith(os.path.basename(log_file)) and filename.endswith(".gz"):
            file_path = os.path.join(log_dir, filename)
            file_mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            if file_mtime < cutoff_date:
                os.remove(file_path)
                logging.info(f"Deleted old log archive: {filename}")

def main():
    # 1. Collect Metrics
    metrics = collect_metrics()
    logging.info(f"Collected Metrics: {json.dumps(metrics, indent=2)}")
    
    # 2. Check Thresholds (Simulating a breach for demonstration if needed, but using real data)
    check_thresholds(metrics)

    # 3. Service Availability Check
    check_service_availability("https://www.google.com")
    # check_service_availability("https://invalid-url.test") # Uncomment to test failure

    # 4. Log Rotation (Demo)
    # Create a dummy log file for demonstration
    dummy_log = "sysops_monitor.log"
    with open(dummy_log, "a") as f:
        f.write(f"Log entry at {datetime.datetime.now()}\n")
    
    rotate_logs(dummy_log, retention_days=7)

if __name__ == "__main__":
    main()
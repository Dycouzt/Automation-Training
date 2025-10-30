import logging
import logging.handlers
import datetime
import os
import smtplib
import ssl
import socket
import psutil
import json
import csv
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the logger
logger = logging.getLogger('my_app')
logger.setLevel(logging.INFO)

# Define the log format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Create a handler for rotating files
handler = logging.handlers.TimedRotatingFileHandler(
    'app.log', when='D', interval=1, backupCount=7)
handler.setFormatter(formatter)
logger.addHandler(handler)

# --- Email Alerting ---
# ... (existing email functionality) ...

def send_email_alert(subject, body):
    """Sends an email alert."""
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT", 587))
    smtp_username = os.getenv("SMTP_USERNAME")
    smtp_password = os.getenv("SMTP_PASSWORD")
    recipient_email = os.getenv("RECIPIENT_EMAIL")

    if not all([smtp_server, smtp_port, smtp_username, smtp_password, recipient_email]):
        logger.error("SMTP credentials are not set in the environment variables.")
        return

    message = f"Subject: {subject}\n\n{body}"

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=context)
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, recipient_email, message)
            logger.info("Email alert sent successfully.")
    except Exception as e:
        logger.error(f"Failed to send email alert: {e}")

def check_logs_for_errors(log_file):
    """Checks the log file for errors and sends an email alert if any are found."""
    try:
        with open(log_file, 'r') as f:
            errors = [line for line in f if "ERROR" in line]
        
        if errors:
            hostname = socket.gethostname()
            subject = f"Error detected on {hostname}"
            body = f"The following errors were detected in {log_file}:\n\n"
            body += "\n".join(errors)
            send_email_alert(subject, body)
    except FileNotFoundError:
        logger.warning(f"Log file {log_file} not found.")

# --- System Metrics Reporting ---

def get_system_metrics():
    """Gathers system metrics."""
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')
    net_info = psutil.net_io_counters()

    metrics = {
        "timestamp": datetime.datetime.now().isoformat(),
        "cpu_usage_percent": cpu_usage,
        "memory_usage_percent": memory_info.percent,
        "disk_usage_percent": disk_info.percent,
        "bytes_sent": net_info.bytes_sent,
        "bytes_received": net_info.bytes_recv
    }
    return metrics

def generate_report(metrics, report_format='json'):
    """Generates a report of system metrics in the specified format."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"system_report_{timestamp}.{report_format}"

    if report_format == 'json':
        with open(filename, 'w') as f:
            json.dump(metrics, f, indent=4)
    elif report_format == 'csv':
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=metrics.keys())
            writer.writeheader()
            writer.writerow(metrics)
    
    logger.info(f"System metrics report generated: {filename}")

# --- Example Usage ---

def run_backup():
    logger.info("Starting backup process...")
    try:
        raise ValueError("Failed to connect to backup server")
    except ValueError as e:
        logger.error(f"Backup failed: {e}")

def check_disk_space():
    logger.info("Checking disk space...")
    disk_space = 15 # in GB
    if disk_space < 20:
        logger.warning(f"Low disk space: {disk_space}GB remaining.")

if __name__ == "__main__":
    logger.info("Script started.")
    run_backup()
    check_disk_space()
    
    # Generate system metrics report
    system_metrics = get_system_metrics()
    generate_report(system_metrics, report_format='json') # or 'csv'

    logger.info("Script finished.")
    
    # Check for errors and send an alert
    check_logs_for_errors('app.log')

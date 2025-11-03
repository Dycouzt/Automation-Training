"""
2. Cloud and Infrastructure Automation
Use boto3 to:
- List EC2 instances by tag and state.
- Start/stop instances on schedule.
- Fetch S3 bucket details and automate backups to S3.
- Write a wrapper script that automates AWS CLI tasks (e.g., upload logs, rotate credentials).
- Build a lightweight cloud resource auditor to check unused resources (simulated if no AWS access).
"""
import boto3
import os
import schedule
import time
from botocore.exceptions import NoCredentialsError

# --- Configuration ---
# In a real-world scenario, use more secure credential management.
# For this script, we'll simulate AWS access if credentials are not found.
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

def check_aws_credentials():
    """Check if AWS credentials are configured."""
    if not AWS_ACCESS_KEY_ID or not AWS_SECRET_ACCESS_KEY:
        print("AWS credentials not found. Running in simulation mode.")
        return False
    return True

HAS_AWS_CREDENTIALS = check_aws_credentials()

def get_boto3_client(service):
    """Get a boto3 client, handling simulation mode."""
    if not HAS_AWS_CREDENTIALS:
        return None
    try:
        return boto3.client(
            service,
            region_name=AWS_REGION,
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        )
    except NoCredentialsError:
        print(f"Credentials not available for {service}. Cannot create client.")
        return None

# --- EC2 Functions ---

def list_ec2_instances(tag_key, tag_value, state):
    """List EC2 instances by a specific tag and state."""
    print(f"Listing EC2 instances with tag '{tag_key}={tag_value}' and state '{state}':")
    if not HAS_AWS_CREDENTIALS:
        print("  - Simulation: instance-1 (running)")
        print("  - Simulation: instance-2 (stopped)")
        return

    ec2 = get_boto3_client("ec2")
    if not ec2:
        return

    filters = [
        {'Name': f'tag:{tag_key}', 'Values': [tag_value]},
        {'Name': 'instance-state-name', 'Values': [state]},
    ]
    
    try:
        response = ec2.describe_instances(Filters=filters)
        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                print(f"  - Instance ID: {instance['InstanceId']} ({instance['State']['Name']})")
    except Exception as e:
        print(f"Error listing EC2 instances: {e}")

def start_instance(instance_id):
    """Start a specific EC2 instance."""
    print(f"Starting instance {instance_id}...")
    if not HAS_AWS_CREDENTIALS:
        print("  - Simulation: Instance started.")
        return

    ec2 = get_boto3_client("ec2")
    if not ec2:
        return
        
    try:
        ec2.start_instances(InstanceIds=[instance_id])
        print(f"  - Instance {instance_id} start command sent.")
    except Exception as e:
        print(f"Error starting instance: {e}")

def stop_instance(instance_id):
    """Stop a specific EC2 instance."""
    print(f"Stopping instance {instance_id}...")
    if not HAS_AWS_CREDENTIALS:
        print("  - Simulation: Instance stopped.")
        return

    ec2 = get_boto3_client("ec2")
    if not ec2:
        return

    try:
        ec2.stop_instances(InstanceIds=[instance_id])
        print(f"  - Instance {instance_id} stop command sent.")
    except Exception as e:
        print(f"Error stopping instance: {e}")

# --- S3 Functions ---

def list_s3_buckets():
    """List all S3 buckets."""
    print("Listing S3 buckets:")
    if not HAS_AWS_CREDENTIALS:
        print("  - Simulation: my-backup-bucket")
        print("  - Simulation: my-log-bucket")
        return

    s3 = get_boto3_client("s3")
    if not s3:
        return

    try:
        response = s3.list_buckets()
        for bucket in response['Buckets']:
            print(f"  - {bucket['Name']}")
    except Exception as e:
        print(f"Error listing S3 buckets: {e}")

def backup_to_s3(file_path, bucket_name, s3_key):
    """Upload a file to an S3 bucket."""
    print(f"Backing up '{file_path}' to S3 bucket '{bucket_name}' as '{s3_key}'...")
    if not HAS_AWS_CREDENTIALS:
        print("  - Simulation: Backup successful.")
        return

    s3 = get_boto3_client("s3")
    if not s3:
        return

    try:
        s3.upload_file(file_path, bucket_name, s3_key)
        print("  - Backup successful.")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"Error backing up to S3: {e}")

# --- AWS CLI Wrapper ---

def aws_cli_wrapper(command):
    """A simple wrapper to run AWS CLI commands."""
    print(f"Running AWS CLI command: '{command}'")
    if not HAS_AWS_CREDENTIALS:
        print("  - Simulation: Command executed successfully.")
        return
    
    # In a real script, you might use subprocess to run the AWS CLI
    # For simplicity, we'll just print the command
    print(f"  - (Execute with subprocess) aws {command}")

# --- Cloud Resource Auditor ---

def audit_unused_resources():
    """Simulated audit of unused cloud resources."""
    print("Auditing for unused cloud resources (Simulated):")
    print("  - Unused Elastic IP: 52.91.123.45")
    print("  - Detached EBS Volume: vol-0123456789abcdef0")
    print("  - Idle RDS Instance: db-instance-1")

# --- Scheduler ---

def setup_scheduler():
    """Set up scheduled tasks."""
    # Schedule jobs, e.g., stop instances at 8 PM daily
    schedule.every().day.at("20:00").do(stop_instance, instance_id="instance-to-stop")
    
    # Schedule a backup every Sunday
    schedule.every().sunday.at("02:00").do(
        backup_to_s3, 
        file_path="app.log", 
        bucket_name="my-backup-bucket", 
        s3_key="logs/app.log"
    )

def run_scheduled_tasks():
    """Run all pending scheduled tasks."""
    while True:
        schedule.run_pending()
        time.sleep(1)

# --- Main Execution ---

if __name__ == "__main__":
    print("--- Cloud and Infrastructure Automation Script ---")

    # 1. List EC2 instances
    list_ec2_instances(tag_key="Environment", tag_value="Dev", state="running")
    
    # 2. Start/stop an instance (example)
    start_instance("i-0123456789abcdef0")
    stop_instance("i-0123456789abcdef0")

    # 3. S3 operations
    list_s3_buckets()
    # Create a dummy file for backup simulation
    with open("app.log", "w") as f:
        f.write("Log entry for backup.")
    backup_to_s3("app.log", "my-backup-bucket", "logs/app.log")

    # 4. AWS CLI wrapper example
    aws_cli_wrapper("s3 ls")

    # 5. Cloud resource auditor
    audit_unused_resources()

    # 6. Scheduler (uncomment to run)
    # print("\n--- Starting Scheduler (runs indefinitely) ---")
    # setup_scheduler()
    # run_scheduled_tasks()
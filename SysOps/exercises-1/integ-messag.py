"""
7. Integrations and Messaging
- Post deployment updates to Slack/Teams via webhook.
- Fetch and summarize cloudwatch or ELK logs via REST API.
- Create a small Flask or FastAPI endpoint to trigger scripts remotely (basic API-driven automation).
- Implement a chatbot-style CLI that takes commands (start backup, check uptime, etc.) and executes Python scripts.
"""

import requests
import json
import sys
import threading
from flask import Flask, request, jsonify

# --- 1. Post deployment updates to Slack/Teams via webhook ---
def send_notification(webhook_url, message):
    """
    Sends a message to a Slack or Teams webhook.
    """
    headers = {'Content-Type': 'application/json'}
    payload = {'text': message}
    
    try:
        response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        print(f"Notification sent successfully: {message}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send notification: {e}")

# --- 2. Fetch and summarize cloudwatch or ELK logs via REST API ---
def fetch_and_summarize_logs(api_url, query_params=None):
    """
    Fetches logs from a REST API (simulating CloudWatch/ELK) and summarizes them.
    """
    try:
        response = requests.get(api_url, params=query_params)
        response.raise_for_status()
        logs = response.json()
        
        # Assuming logs is a list of dicts with 'timestamp' and 'message'
        print(f"--- Log Summary for {api_url} ---")
        error_count = 0
        for log in logs:
            if 'error' in log.get('message', '').lower():
                error_count += 1
        
        print(f"Total Logs Fetched: {len(logs)}")
        print(f"Error Count: {error_count}")
        return logs
    except requests.exceptions.RequestException as e:
        print(f"Error fetching logs: {e}")
        return []

# --- 3. Create a small Flask endpoint to trigger scripts remotely ---
app = Flask(__name__)

@app.route('/trigger-script', methods=['POST'])
def trigger_script():
    """
    Endpoint to trigger a script remotely.
    Expects JSON: {"script_name": "backup", "params": {...}}
    """
    data = request.json
    script_name = data.get('script_name')
    
    if script_name == 'backup':
        # Simulate running a backup script
        return jsonify({"status": "success", "message": "Backup started"}), 200
    elif script_name == 'uptime':
        # Simulate checking uptime
        return jsonify({"status": "success", "message": "System uptime: 99.9%"}), 200
    else:
        return jsonify({"status": "error", "message": "Unknown script"}), 400

def run_api_server():
    """Runs the Flask app in a separate thread for demonstration purposes."""
    app.run(port=5000, debug=False, use_reloader=False)

# --- 4. Implement a chatbot-style CLI ---
def chatbot_cli():
    """
    Interactive CLI that takes commands and executes actions.
    """
    print("\n--- SysOps Chatbot CLI ---")
    print("Available commands: 'start backup', 'check uptime', 'send alert', 'exit'")
    
    while True:
        try:
            command = input("SysOpsBot> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            break

        if command == 'exit':
            print("Goodbye!")
            break
        elif command == 'start backup':
            print("Initiating backup sequence...")
            # Logic to call backup function would go here
            print("Backup completed successfully.")
        elif command == 'check uptime':
            print("Checking system status...")
            print("All systems operational. Uptime: 14 days, 3 hours.")
        elif command == 'send alert':
            msg = input("Enter alert message: ")
            # Example webhook URL (would be real in production)
            send_notification("https://hooks.slack.com/services/T000/B000/XXX", msg)
        else:
            print("I didn't understand that command. Try 'start backup' or 'check uptime'.")

if __name__ == "__main__":
    # In a real scenario, you might choose to run EITHER the API OR the CLI, 
    # or run the API in a background thread if this script needs to do both.
    
    print("Select mode:")
    print("1. Run Chatbot CLI")
    print("2. Run API Server")
    print("3. Run Both (API in background)")
    
    # For the purpose of this script generation, we'll default to CLI if run directly,
    # but show how to start the API.
    
    # Uncomment the following line to test the API server:
    # run_api_server()
    
    # Default to CLI
    chatbot_cli()
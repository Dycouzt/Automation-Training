"""
Ping multiple servers and report uptime.
Fetch API data (e.g., REST API call) and parse JSON.
Monitor HTTP endpoints for status codes.
Automate DNS lookups or IP validations.
"""

import subprocess
from pathlib import Path
import platform
import re
import requests

def api_fetch(api_url):
    try:
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def get_ip_list():
    ip_pattern = re.compile(
        r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    )  # simple IPv4 validation

    ips = []

    print("Enter IPs to ping (press Enter without input to finish):")
    while True:
        ip = input("> ").strip()
        if not ip:
            break
        if ip_pattern.match(ip):
            ips.append(ip)
        else:
            print("Invalid IP format. Try again.")
    return ips

def ping_servers(servers):
    print(f"Starting ICMP call to {servers}")
    count_flag = "-n" if platform.system().lower() == "windows" else "-c"

    for server in servers:     
        try:
            result = subprocess.run(
                ["ping", count_flag, "3", server],
                capture_output=True,
                text=True,
                check=True
            )
            print(result.stdout.strip())
        except subprocess.CalledProcessError as e:
            print("Ping failed:")
            print(e.stderr.strip() if e.stderr else "Unknown error")



if __name__ == "__main__":
    api_url = "https://api.github.com/repos/python/cpython"
    api_fetch(api_url)
    ip_list = get_ip_list()
    print(f"Starting ICMP call to: {ip_list}")
    ping_servers(ip_list)


"""
Ping multiple servers and report uptime.
Fetch API data (e.g., REST API call) and parse JSON.
Monitor HTTP endpoints for status codes.
Automate DNS lookups or IP validations.
"""

import subprocess
import platform
import re
import requests
import ipaddress

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

def api_fetch(api_url):
    try:
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        if data:
            print("Repository:", data["name"])
            print("Stars:", data["stargazers_count"])
            print("Forks:", data["forks_count"])
        return None

def monitor_endpoints(endpoints_list):
    status_codes = []
    for endpoint in endpoints_list:
        response = requests.get(endpoint)
        status_codes.append(response.status_code())
        return status_codes
    
    for status in status_codes:
        print(f"Status Code: {status}")

def validate_ip(address):
    try:
        ip = ipaddress.ip_address(address)
        if isinstance(ip, ipaddress.IPv4Address):
            return "IPv4"
        elif isinstance(ip, ipaddress.IPv6Address):
            return "IPv6"
    except ValueError:
        return None

def get_name(website):
    match = re.compile(r"(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}")
    
    if website.match(match):
        try:
            dns_lookup = subprocess.run(f"nslookup {website}", capture_output=True, text=True, check=True)
            lines = dns_lookup.stdout.strip().splitlines()
            print(lines[0-1])

        except subprocess.CalledProcessError as e:
            print("Lookup failed:")
            print(e.stderr.strip() if e.stderr else "Unknown error")

    else:
        print("Invalid service / website name.")
            

if __name__ == "__main__":
    api_url_2 = "https://jsonplaceholder.typicode.com" # One can set a url as a variable in order to use it multiple times.
    endpoints_list = ["/posts/1", "/posts/2", "/posts/3"] # The specific last part of a url is called endpoint
    api_url_1 = "https://api.github.com/repos/python/cpython"
    api_fetch(api_url_1)
    ip_list = get_ip_list()
    print(f"Starting ICMP call to: {ip_list}")
    address = "192.168.64.100"
    website = "netflix.com"
    ping_servers(ip_list)


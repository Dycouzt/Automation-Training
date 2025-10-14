"""
Ping multiple servers and report uptime.
Fetch API data (e.g., REST API call) and parse JSON.
Monitor HTTP endpoints for status codes.
Automate DNS lookups or IP validations.
"""

import subprocess
import platform
import requests
import ipaddress
import socket

def get_ip_list():
    ips = []
    print("Enter IPs to ping (press Enter without input to finish):")
    while True:
        ip = input("> ").strip()
        if not ip:
            break
        try:
            ipaddress.ip_address(ip)
            ips.append(ip)
        except ValueError:
            print("Invalid IP format. Try again.")
    return ips


def ping_servers(servers):
    count_flag = "-n" if platform.system().lower() == "windows" else "-c"
    for server in servers:
        print(f"Pinging {server}...")
        try:
            result = subprocess.run(
                ["ping", count_flag, "3", server],
                capture_output=True,
                text=True,
                check=True
            )
            print("Ping success.")
        except subprocess.CalledProcessError:
            print(f"Ping failed for {server}")


def api_fetch(api_url):
    try:
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()
        data = response.json()
        print("API data fetched successfully.")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def monitor_endpoints(base_url, endpoints):
    for endpoint in endpoints:
        url = f"{base_url}{endpoint}"
        try:
            r = requests.get(url, timeout=5)
            print(f"{url} -> Status: {r.status_code}")
        except requests.RequestException as e:
            print(f"Failed to reach {url}: {e}")


def validate_ip(address):
    try:
        ip = ipaddress.ip_address(address)
        return "IPv4" if isinstance(ip, ipaddress.IPv4Address) else "IPv6"
    except ValueError:
        return None


def dns_lookup(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"{domain} resolves to {ip}")
    except socket.gaierror:
        print(f"DNS lookup failed for {domain}")


if __name__ == "__main__":
    # Example usage
    github_repo = "https://api.github.com/repos/python/cpython"
    json_data = api_fetch(github_repo)
    if json_data:
        print(f"Repository: {json_data['name']}")
        print(f"Stars: {json_data['stargazers_count']}")
        print(f"Forks: {json_data['forks_count']}")

    monitor_endpoints("https://jsonplaceholder.typicode.com", ["/posts/1", "/posts/2", "/posts/3"])

    ip_list = get_ip_list()
    if ip_list:
        ping_servers(ip_list)

    address = "192.168.64.10"
    website = "netflix.com"
    print(f"{address} is {validate_ip(address)}")
    dns_lookup(website)



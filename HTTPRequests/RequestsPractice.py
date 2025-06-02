# This script contains some practice exercises for the 'requests' module.
import requests


url = "https://jsonplaceholder.typicode.com"
response = requests.get(url + "/users/2")
print(f"Status code: {response.status_code}")
data = response.json()
print("Username: ", data["name"])
print("Email: ", data["email"])
print("City: ", data["address"])



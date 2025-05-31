# This script shows how the 'requests' module works in python.

import requests


base_url1 = "https://jsonplaceholder.typicode.com" # One can set a url as a variable in order to use it multiple times.
endpoint1 = "/posts/1" # The specific last part of a url is called endpoint

response1 = requests.get(base_url1 + endpoint1) # The GET function asks for a resource. URL needs to be specific
print(f"Status Code: {response1.status_code}") # Status code isn't necessary, but helps to validate the request
data1 = response1.json() # Responses are always either in bytes or JSON formatted
print("Title: ", data1["title"])
print("Body: ", data1["body"])

payload = {"name": "Diego", "age": "21"}
response2 = requests.post("https://httpbin.org/post", data=payload)
print(f"Status Code: {response2.status_code}")
print(response2.json())

url = "https://api.github.com/repos/python/cpython"
response3 = requests.get(url)
data2 = response3.json()
print("Stars:", data2["stargazers_count"])
print("Forks:", data2["forks_count"])
print("Open Issues:", data2["open_issues_count"])


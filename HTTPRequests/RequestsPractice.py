# This script contains some practice exercises for the 'requests' module.
import requests


# Beginner Exercises
url = "https://jsonplaceholder.typicode.com"
response = requests.get(url + "/users/2")
"""
print(f"Status code: {response.status_code}")
data = response.json()
print("Username: ", data["name"])
print("Email: ", data["email"])
print("City: ", data["address"])


payload = {
    "title": "Network Security",
    "body": "Always scan your open ports.",
    "userId": 101
}
post = requests.post(url + "/posts", data=payload)
print(f"Status code: {post.status_code}")
print(post.json())


check = requests.get(url + "/invalidendpoint")
status = check.status_code

if status != 200:
    print("Error, page not found")

# Intermediate Exercises

fetch = requests.get(url + "/posts")
data = fetch.json()
for post in data[:5]:
    print("Title: ", post["title"])


header = {
    "User-Agent": "CyberStudent/1.0"
}
custom = requests.get("https://httpbin.org/headers", headers=header)
response1 = custom.json()
print(f"Status code: {custom.status_code}")
print(response1)


# Create a session object to store cookies
session = requests.Session()
# 1. Set the cookie
session.get("https://httpbin.org/cookies/set/sessionid/abc123")
# 2. Get the cookie back
response = session.get("https://httpbin.org/cookies")
# 3. Print the cookies
print("Cookies:", response.json()["cookies"])
"""
# Advanced Exercises

info = {"username": "admin", "password": "hunter2"}
upload = requests.post("https://httpbin.org/post", data=info)
response2 = upload.json()
print(f"Status code: {upload.status_code}")
print(response2["form"]["username"])


for user_id in range(1, 6):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    user = response.json()

    print("Username: ", user["username"])
    print("Website: ", user["website"])
    print("-" * 30)

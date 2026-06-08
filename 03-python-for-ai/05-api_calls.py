# ============================================================
# API CALLS IN PYTHON
# ============================================================

# API = Application Programming Interface
#
# APIs allow your Python programs to communicate with
# external applications and services.
#
# Examples:
# - OpenAI API
# - Weather API
# - GitHub API
# - Google Maps API
#
# Most modern APIs return data in JSON format.

# ============================================================
# INSTALL REQUESTS PACKAGE
# ============================================================

# pip install requests

# ============================================================
# IMPORT REQUESTS
# ============================================================

import requests

# ============================================================
# SIMPLE GET REQUEST
# ============================================================

response = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

print(response.status_code)

# Output:
# 200

# ============================================================
# GET RESPONSE DATA
# ============================================================

response = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

data = response.json()

print(data)

# ============================================================
# ACCESSING JSON DATA
# ============================================================

response = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

users = response.json()

print(users[0]["name"])
print(users[0]["email"])

# ============================================================
# LOOPING THROUGH API DATA
# ============================================================

response = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

users = response.json()

for user in users:
    print(user["name"])

# ============================================================
# GET REQUEST WITH PARAMETERS
# ============================================================

params = {
    "userId": 1
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params=params
)

print(response.json())

# ============================================================
# POST REQUEST
# ============================================================

data = {
    "title": "Python API",
    "body": "Learning API Calls",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data
)

print(response.status_code)
print(response.json())

# ============================================================
# PUT REQUEST (UPDATE)
# ============================================================

updated_data = {
    "id": 1,
    "title": "Updated Title",
    "body": "Updated Content",
    "userId": 1
}

response = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",
    json=updated_data
)

print(response.json())

# ============================================================
# DELETE REQUEST
# ============================================================

response = requests.delete(
    "https://jsonplaceholder.typicode.com/posts/1"
)

print(response.status_code)

# ============================================================
# HEADERS
# ============================================================

headers = {
    "User-Agent": "Python-App"
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/users",
    headers=headers
)

print(response.status_code)

# ============================================================
# API KEY EXAMPLE
# ============================================================

# Many APIs require authentication.

# api_key = "YOUR_API_KEY"

# headers = {
#     "Authorization": f"Bearer {api_key}"
# }

# response = requests.get(
#     "https://api.example.com/data",
#     headers=headers
# )

# ============================================================
# ERROR CHECKING
# ============================================================

response = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

if response.status_code == 200:
    print("Success")
else:
    print("Request Failed")

# ============================================================
# PRACTICAL EXAMPLE
# FETCH USER DETAILS
# ============================================================

response = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

users = response.json()

for user in users:

    print("Name :", user["name"])
    print("Email:", user["email"])
    print("-" * 30)

# ============================================================
# SUMMARY
# ============================================================

print("""
Common Request Methods:

GET    -> Fetch data
POST   -> Create data
PUT    -> Update data
DELETE -> Delete data

Common Response Methods:

response.status_code
response.json()
response.text

Common Parameters:

headers={}
params={}
json={}

Most APIs return JSON data.
""")
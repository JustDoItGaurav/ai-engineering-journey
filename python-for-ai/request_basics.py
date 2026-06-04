# ============================================================
# REQUESTS BASICS IN PYTHON
# ============================================================

# requests is one of the most popular Python libraries
# used to make HTTP requests.

# Install:
# pip install requests

import requests

# ============================================================
# SIMPLE GET REQUEST
# ============================================================

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1"
)

print(response)

# Output:
# <Response [200]>

# ============================================================
# STATUS CODE
# ============================================================

print(response.status_code)

# Common Status Codes:
# 200 -> Success
# 201 -> Created
# 400 -> Bad Request
# 401 -> Unauthorized
# 404 -> Not Found
# 500 -> Server Error

# ============================================================
# RESPONSE TEXT
# ============================================================

print(response.text)

# Returns the response as plain text

# ============================================================
# RESPONSE JSON
# ============================================================

data = response.json()

print(data)

# ============================================================
# ACCESSING JSON DATA
# ============================================================

print(data["id"])
print(data["title"])

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

print(response.url)
print(response.json())

# ============================================================
# CUSTOM HEADERS
# ============================================================

headers = {
    "User-Agent": "Python Requests"
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    headers=headers
)

print(response.status_code)

# ============================================================
# POST REQUEST
# ============================================================

payload = {
    "title": "Python",
    "body": "Learning Requests",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=payload
)

print(response.status_code)
print(response.json())

# ============================================================
# PUT REQUEST
# ============================================================

updated_data = {
    "id": 1,
    "title": "Updated Post",
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
# TIMEOUT
# ============================================================

try:

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        timeout=5
    )

    print(response.status_code)

except requests.exceptions.Timeout:
    print("Request Timed Out")

# ============================================================
# ERROR HANDLING
# ============================================================

try:

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

    response.raise_for_status()

    print("Request Successful")

except requests.exceptions.RequestException as error:
    print("Error:", error)

# ============================================================
# PRACTICAL EXAMPLE 1
# FETCH USERS
# ============================================================

response = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

users = response.json()

for user in users:

    print(user["name"])

# ============================================================
# PRACTICAL EXAMPLE 2
# FETCH POSTS
# ============================================================

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts"
)

posts = response.json()

for post in posts[:5]:

    print(post["title"])

# ============================================================
# PRACTICAL EXAMPLE 3
# FETCH TODO ITEMS
# ============================================================

response = requests.get(
    "https://jsonplaceholder.typicode.com/todos"
)

todos = response.json()

for todo in todos[:5]:

    print(todo["title"])

# ============================================================
# SUMMARY
# ============================================================

print("""
Common Requests Methods:

requests.get()
requests.post()
requests.put()
requests.delete()

Useful Response Attributes:

response.status_code
response.text
response.json()

Useful Parameters:

params={}
headers={}
json={}
timeout=5

Best Practice:

response.raise_for_status()

This automatically raises an exception
if the request fails.
""")
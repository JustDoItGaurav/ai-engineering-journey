# ============================================================
# JSON HANDLING IN PYTHON
# ============================================================

# JSON = JavaScript Object Notation
#
# JSON is the most common format used for:
# - APIs
# - Configuration files
# - Data exchange
# - AI/ML applications
#
# Python provides a built-in module called json.

import json

# ============================================================
# PYTHON DICTIONARY
# ============================================================

student = {
    "name": "Gaurav",
    "age": 21,
    "is_student": True
}

print(student)
print(type(student))

# ============================================================
# CONVERT PYTHON OBJECT TO JSON STRING
# json.dumps()
# ============================================================

json_data = json.dumps(student)

print(json_data)
print(type(json_data))

# Output:
# {"name": "Gaurav", "age": 21, "is_student": true}

# ============================================================
# PRETTY PRINT JSON
# ============================================================

formatted_json = json.dumps(
    student,
    indent=4
)

print(formatted_json)

# ============================================================
# CONVERT JSON STRING TO PYTHON OBJECT
# json.loads()
# ============================================================

json_string = '''
{
    "name": "Rahul",
    "age": 22,
    "is_student": true
}
'''

python_data = json.loads(json_string)

print(python_data)
print(type(python_data))

# ============================================================
# ACCESSING JSON DATA
# ============================================================

print(python_data["name"])
print(python_data["age"])

# ============================================================
# WRITING JSON TO A FILE
# json.dump()
# ============================================================

student = {
    "name": "Priya",
    "age": 20,
    "city": "Mumbai"
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON file created successfully.")

# ============================================================
# READING JSON FROM A FILE
# json.load()
# ============================================================

with open("student.json", "r") as file:
    data = json.load(file)

print(data)

# ============================================================
# JSON ARRAY EXAMPLE
# ============================================================

students = [
    {
        "name": "Gaurav",
        "age": 21
    },
    {
        "name": "Rahul",
        "age": 22
    },
    {
        "name": "Priya",
        "age": 20
    }
]

json_students = json.dumps(
    students,
    indent=4
)

print(json_students)

# ============================================================
# LOOPING THROUGH JSON DATA
# ============================================================

for student in students:

    print(student["name"])
    print(student["age"])

# ============================================================
# NESTED JSON
# ============================================================

data = {
    "student": {
        "name": "Gaurav",
        "age": 21
    },
    "course": {
        "name": "Python",
        "duration": "3 Months"
    }
}

print(data["student"]["name"])
print(data["course"]["name"])

# ============================================================
# PRACTICAL EXAMPLE 1
# SAVE USER PROFILE
# ============================================================

user = {
    "name": "Gaurav",
    "age": 21,
    "skills": [
        "Python",
        "AI",
        "Machine Learning"
    ]
}

with open("user_profile.json", "w") as file:
    json.dump(user, file, indent=4)

print("User profile saved.")

# ============================================================
# PRACTICAL EXAMPLE 2
# READ USER PROFILE
# ============================================================

with open("user_profile.json", "r") as file:

    profile = json.load(file)

print(profile["name"])
print(profile["skills"])

# ============================================================
# PRACTICAL EXAMPLE 3
# API RESPONSE SIMULATION
# ============================================================

api_response = '''
{
    "status": "success",
    "data": {
        "name": "Gaurav",
        "score": 95
    }
}
'''

response = json.loads(api_response)

print(response["status"])
print(response["data"]["name"])
print(response["data"]["score"])

# ============================================================
# SUMMARY
# ============================================================

print("""
JSON Functions:

json.dumps() -> Python Object to JSON String
json.loads() -> JSON String to Python Object

json.dump()  -> Write JSON to File
json.load()  -> Read JSON from File

Common JSON Types:

Object  -> Dictionary
Array   -> List
String  -> str
Number  -> int/float
Boolean -> True/False
Null    -> None

JSON is heavily used in:
✔ APIs
✔ AI Applications
✔ Configuration Files
✔ Web Development
""")
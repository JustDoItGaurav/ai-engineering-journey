# ============================================================
# DICTIONARIES IN PYTHON
# ============================================================

# A dictionary stores data in key-value pairs.
# Dictionaries are mutable (changeable) and unordered.

# ------------------------------------------------------------
# Creating a Dictionary
# ------------------------------------------------------------

student = {
    "name": "Gaurav",
    "age": 21,
    "is_student": True
}

print(student)
print(type(student))

# ------------------------------------------------------------
# Accessing Values
# ------------------------------------------------------------

print(student["name"])
print(student["age"])

# ------------------------------------------------------------
# Using get()
# Safer than direct indexing
# ------------------------------------------------------------

print(student.get("name"))
print(student.get("city"))  # Returns None if key doesn't exist

# ------------------------------------------------------------
# Adding New Key-Value Pairs
# ------------------------------------------------------------

student["city"] = "Mumbai"

print(student)

# ------------------------------------------------------------
# Updating Existing Values
# ------------------------------------------------------------

student["age"] = 22

print(student)

# ------------------------------------------------------------
# Removing Items
# ------------------------------------------------------------

student.pop("city")

print(student)

# ------------------------------------------------------------
# Removing the Last Inserted Item
# ------------------------------------------------------------

student.popitem()

print(student)

# ------------------------------------------------------------
# Dictionary Length
# ------------------------------------------------------------

print(len(student))

# ------------------------------------------------------------
# Checking if a Key Exists
# ------------------------------------------------------------

print("name" in student)
print("city" in student)

# ------------------------------------------------------------
# Getting All Keys
# ------------------------------------------------------------

print(student.keys())

# ------------------------------------------------------------
# Getting All Values
# ------------------------------------------------------------

print(student.values())

# ------------------------------------------------------------
# Getting All Key-Value Pairs
# ------------------------------------------------------------

print(student.items())

# ------------------------------------------------------------
# Looping Through Keys
# ------------------------------------------------------------

for key in student:
    print(key)

# ------------------------------------------------------------
# Looping Through Values
# ------------------------------------------------------------

for value in student.values():
    print(value)

# ------------------------------------------------------------
# Looping Through Key-Value Pairs
# ------------------------------------------------------------

for key, value in student.items():
    print(key, ":", value)

# ------------------------------------------------------------
# Nested Dictionary
# ------------------------------------------------------------

students = {
    "student1": {
        "name": "Gaurav",
        "age": 21
    },
    "student2": {
        "name": "Rahul",
        "age": 22
    }
}

print(students)

# Accessing Nested Values
print(students["student1"]["name"])

# ------------------------------------------------------------
# Copying a Dictionary
# ------------------------------------------------------------

student_copy = student.copy()

print(student_copy)

# ------------------------------------------------------------
# Clearing a Dictionary
# ------------------------------------------------------------

temp_dict = {
    "a": 1,
    "b": 2
}

temp_dict.clear()

print(temp_dict)

# ------------------------------------------------------------
# AI/Data Science Example
# ------------------------------------------------------------

prediction = {
    "label": "Cat",
    "confidence": 0.97
}

print(prediction["label"])
print(prediction["confidence"])

# ------------------------------------------------------------
# Summary
# ------------------------------------------------------------

print("""
Common Dictionary Methods:

get()      -> Get value by key
keys()     -> Get all keys
values()   -> Get all values
items()    -> Get key-value pairs
pop()      -> Remove specific item
popitem()  -> Remove last item
copy()     -> Copy dictionary
clear()    -> Remove all items

Dictionary Features:

{}          -> Create dictionary
key:value   -> Store data
Mutable     -> Can be modified
Unique Keys -> Duplicate keys not allowed
""")
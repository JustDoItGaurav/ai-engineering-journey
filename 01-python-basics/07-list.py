# ============================================================
# LISTS IN PYTHON
# ============================================================

# A list is an ordered, mutable (changeable) collection of items.

# ------------------------------------------------------------
# Creating Lists
# ------------------------------------------------------------

fruits = ["Apple", "Banana", "Mango"]

print(fruits)
print(type(fruits))

# ------------------------------------------------------------
# Accessing Elements (Indexing)
# ------------------------------------------------------------

print(fruits[0])   # First element
print(fruits[1])   # Second element
print(fruits[-1])  # Last element

# ------------------------------------------------------------
# Slicing Lists
# ------------------------------------------------------------

numbers = [10, 20, 30, 40, 50]

print(numbers[0:3])  # Elements from index 0 to 2
print(numbers[:3])   # First 3 elements
print(numbers[2:])   # From index 2 to end
print(numbers[::-1]) # Reverse the list

# ------------------------------------------------------------
# Modifying Elements
# ------------------------------------------------------------

fruits[1] = "Orange"

print(fruits)

# ------------------------------------------------------------
# Adding Elements
# ------------------------------------------------------------

fruits.append("Grapes")  # Add one element at the end

print(fruits)

# ------------------------------------------------------------
# Adding Multiple Elements
# ------------------------------------------------------------

fruits.extend(["Pineapple", "Kiwi"])

print(fruits)

# ------------------------------------------------------------
# Inserting Elements
# ------------------------------------------------------------

fruits.insert(1, "Watermelon")

print(fruits)

# ------------------------------------------------------------
# Removing Elements
# ------------------------------------------------------------

fruits.remove("Orange")  # Remove by value

print(fruits)

# ------------------------------------------------------------
# Removing Last Element
# ------------------------------------------------------------

fruits.pop()

print(fruits)

# ------------------------------------------------------------
# Removing Element by Index
# ------------------------------------------------------------

fruits.pop(0)

print(fruits)

# ------------------------------------------------------------
# Finding Length
# ------------------------------------------------------------

print(len(fruits))

# ------------------------------------------------------------
# Checking if an Item Exists
# ------------------------------------------------------------

print("Mango" in fruits)
print("Apple" in fruits)

# ------------------------------------------------------------
# Sorting Lists
# ------------------------------------------------------------

numbers = [5, 2, 8, 1, 9]

numbers.sort()

print(numbers)

# ------------------------------------------------------------
# Reversing Lists
# ------------------------------------------------------------

numbers.reverse()

print(numbers)

# ------------------------------------------------------------
# Looping Through a List
# ------------------------------------------------------------

for fruit in fruits:
    print(fruit)

# ------------------------------------------------------------
# AI/Data Science Example
# ------------------------------------------------------------

features = [5.1, 3.5, 1.4, 0.2]

print(features)

features.append(0.1)

print(features)

# ------------------------------------------------------------
# List of Dictionaries (Common in APIs and AI)
# ------------------------------------------------------------

students = [
    {"name": "Gaurav", "age": 21},
    {"name": "Rahul", "age": 22}
]

print(students)

# Accessing nested data
print(students[0]["name"])

# ------------------------------------------------------------
# Summary
# ------------------------------------------------------------

print("""
Common List Methods:

append()  -> Add one item
extend()  -> Add multiple items
insert()  -> Insert at specific position
remove()  -> Remove by value
pop()     -> Remove by index
sort()    -> Sort the list
reverse() -> Reverse the list
len()     -> Length of list
""")
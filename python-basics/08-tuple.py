# ============================================================
# TUPLES IN PYTHON
# ============================================================

# A tuple is an ordered, immutable (cannot be changed)
# collection of items.

# ------------------------------------------------------------
# Creating Tuples
# ------------------------------------------------------------

fruits = ("Apple", "Banana", "Mango")

print(fruits)
print(type(fruits))

# ------------------------------------------------------------
# Accessing Elements (Indexing)
# ------------------------------------------------------------

print(fruits[0])   # First element
print(fruits[1])   # Second element
print(fruits[-1])  # Last element

# ------------------------------------------------------------
# Slicing Tuples
# ------------------------------------------------------------

numbers = (10, 20, 30, 40, 50)

print(numbers[0:3])  # Elements from index 0 to 2
print(numbers[:3])   # First 3 elements
print(numbers[2:])   # From index 2 to end
print(numbers[::-1]) # Reverse tuple

# ------------------------------------------------------------
# Tuple Length
# ------------------------------------------------------------

print(len(fruits))

# ------------------------------------------------------------
# Checking if an Item Exists
# ------------------------------------------------------------

print("Mango" in fruits)
print("Apple" in fruits)

# ------------------------------------------------------------
# Looping Through a Tuple
# ------------------------------------------------------------

for fruit in fruits:
    print(fruit)

# ------------------------------------------------------------
# Count Method
# ------------------------------------------------------------

numbers = (1, 2, 3, 1, 1, 4)

print(numbers.count(1))

# ------------------------------------------------------------
# Index Method
# ------------------------------------------------------------

print(numbers.index(3))

# ------------------------------------------------------------
# Single Item Tuple
# Comma is mandatory
# ------------------------------------------------------------

single_value = (100,)

print(single_value)
print(type(single_value))

# ------------------------------------------------------------
# Tuple Packing
# ------------------------------------------------------------

student = ("Gaurav", 21, True)

print(student)

# ------------------------------------------------------------
# Tuple Unpacking
# ------------------------------------------------------------

name, age, is_student = student

print(name)
print(age)
print(is_student)

# ------------------------------------------------------------
# Immutable Nature of Tuples
# ------------------------------------------------------------

# This will produce an error because tuples cannot be modified

# fruits[0] = "Orange"

# TypeError: 'tuple' object does not support item assignment

# ------------------------------------------------------------
# AI/Data Science Example
# ------------------------------------------------------------

# Storing fixed dimensions of an image
image_size = (224, 224)

print(image_size)

# Storing RGB color values
rgb = (255, 0, 0)

print(rgb)

# ------------------------------------------------------------
# Summary
# ------------------------------------------------------------

print("""
Tuple Features:

()          -> Create a tuple
[index]     -> Access elements
[start:end] -> Slicing
len()       -> Length
count()     -> Count occurrences
index()     -> Find position

Tuples are:
✔ Ordered
✔ Allow duplicates
✔ Immutable (cannot be changed)
""")
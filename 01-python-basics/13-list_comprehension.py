# ============================================================
# LIST COMPREHENSIONS IN PYTHON
# ============================================================

# List comprehensions provide a shorter and cleaner way
# to create lists.

# Syntax:
# [expression for item in iterable]

# ============================================================
# WITHOUT LIST COMPREHENSION
# ============================================================

numbers = []

for num in range(1, 6):
    numbers.append(num)

print(numbers)

# Output:
# [1, 2, 3, 4, 5]

# ============================================================
# WITH LIST COMPREHENSION
# ============================================================

numbers = [num for num in range(1, 6)]

print(numbers)

# Output:
# [1, 2, 3, 4, 5]

# ============================================================
# SQUARE OF NUMBERS
# ============================================================

squares = [num ** 2 for num in range(1, 6)]

print(squares)

# Output:
# [1, 4, 9, 16, 25]

# ============================================================
# CUBE OF NUMBERS
# ============================================================

cubes = [num ** 3 for num in range(1, 6)]

print(cubes)

# Output:
# [1, 8, 27, 64, 125]

# ============================================================
# USING CONDITIONS
# ============================================================

even_numbers = [num for num in range(1, 11) if num % 2 == 0]

print(even_numbers)

# Output:
# [2, 4, 6, 8, 10]

# ============================================================
# ODD NUMBERS
# ============================================================

odd_numbers = [num for num in range(1, 11) if num % 2 != 0]

print(odd_numbers)

# Output:
# [1, 3, 5, 7, 9]

# ============================================================
# WORKING WITH STRINGS
# ============================================================

names = ["gaurav", "rahul", "priya"]

capitalized_names = [name.capitalize() for name in names]

print(capitalized_names)

# Output:
# ['Gaurav', 'Rahul', 'Priya']

# ============================================================
# STRING LENGTHS
# ============================================================

names = ["Gaurav", "Rahul", "Priya"]

lengths = [len(name) for name in names]

print(lengths)

# Output:
# [6, 5, 5]

# ============================================================
# FILTERING STRINGS
# ============================================================

names = ["Gaurav", "Rahul", "Priya", "An"]

long_names = [name for name in names if len(name) > 4]

print(long_names)

# Output:
# ['Gaurav', 'Rahul', 'Priya']

# ============================================================
# WORKING WITH LISTS
# ============================================================

numbers = [10, 20, 30, 40]

doubled = [num * 2 for num in numbers]

print(doubled)

# Output:
# [20, 40, 60, 80]

# ============================================================
# IF-ELSE IN LIST COMPREHENSION
# ============================================================

numbers = [1, 2, 3, 4, 5]

result = ["Even" if num % 2 == 0 else "Odd" for num in numbers]

print(result)

# Output:
# ['Odd', 'Even', 'Odd', 'Even', 'Odd']

# ============================================================
# AI / DATA SCIENCE EXAMPLES
# ============================================================

# Convert temperatures from Celsius to Fahrenheit

celsius = [0, 10, 20, 30]

fahrenheit = [(temp * 9/5) + 32 for temp in celsius]

print(fahrenheit)

# ------------------------------------------------------------

# Normalize values

scores = [50, 60, 70, 80, 90]

normalized_scores = [score / 100 for score in scores]

print(normalized_scores)

# ------------------------------------------------------------

# Extract values from dictionaries

students = [
    {"name": "Gaurav", "age": 21},
    {"name": "Rahul", "age": 22},
    {"name": "Priya", "age": 20}
]

names = [student["name"] for student in students]

print(names)

# Output:
# ['Gaurav', 'Rahul', 'Priya']

# ============================================================
# SUMMARY
# ============================================================

print("""
List Comprehension Syntax:

[expression for item in iterable]

With Condition:

[expression for item in iterable if condition]

With If-Else:

[value_if_true if condition else value_if_false for item in iterable]

Benefits:

✔ Shorter Code
✔ Cleaner Code
✔ Faster Than Traditional Loops
""")
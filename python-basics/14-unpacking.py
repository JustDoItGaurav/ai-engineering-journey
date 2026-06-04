# ============================================================
# UNPACKING IN PYTHON
# ============================================================

# Unpacking means assigning values from a collection
# (list, tuple, string, etc.) to multiple variables at once.

# ============================================================
# TUPLE UNPACKING
# ============================================================

student = ("Gaurav", 21)

name, age = student

print(name)
print(age)

# ============================================================
# LIST UNPACKING
# ============================================================

fruits = ["Apple", "Banana", "Mango"]

fruit1, fruit2, fruit3 = fruits

print(fruit1)
print(fruit2)
print(fruit3)

# ============================================================
# STRING UNPACKING
# ============================================================

word = "AI"

letter1, letter2 = word

print(letter1)
print(letter2)

# ============================================================
# USING THE * OPERATOR
# ============================================================

numbers = [10, 20, 30, 40, 50]

first, *middle, last = numbers

print(first)
print(middle)
print(last)

# Output:
# 10
# [20, 30, 40]
# 50

# ============================================================
# IGNORING VALUES
# ============================================================

data = ("Gaurav", 21, "Mumbai")

name, _, city = data

print(name)
print(city)

# "_" is commonly used to ignore values

# ============================================================
# SWAPPING VARIABLES
# ============================================================

a = 10
b = 20

print("Before Swap:")
print(a, b)

a, b = b, a

print("After Swap:")
print(a, b)

# ============================================================
# FUNCTION RETURN VALUE UNPACKING
# ============================================================

def calculate(a, b):
    return a + b, a - b

addition, subtraction = calculate(20, 10)

print(addition)
print(subtraction)

# ============================================================
# DICTIONARY UNPACKING
# ============================================================

student = {
    "name": "Gaurav",
    "age": 21
}

# Unpacking keys

name_key, age_key = student

print(name_key)
print(age_key)

# ============================================================
# DICTIONARY ITEMS UNPACKING
# ============================================================

for key, value in student.items():
    print(key, value)

# ============================================================
# PRACTICAL EXAMPLES
# ============================================================

# Example 1: Coordinates

coordinates = (10, 20)

x, y = coordinates

print(f"X = {x}")
print(f"Y = {y}")

# ------------------------------------------------------------

# Example 2: RGB Colors

rgb = (255, 0, 0)

red, green, blue = rgb

print(red)
print(green)
print(blue)

# ------------------------------------------------------------

# Example 3: Student Information

student = ["Gaurav", 21, "Engineering"]

name, age, course = student

print(name)
print(age)
print(course)

# ============================================================
# SUMMARY
# ============================================================

print("""
Unpacking Examples:

a, b = (10, 20)

name, age = ["Gaurav", 21]

first, *middle, last = [1, 2, 3, 4, 5]

a, b = b, a

Benefits:

✔ Cleaner Code
✔ Easy Variable Assignment
✔ Useful with Functions
✔ Common in Data Science & AI
""")
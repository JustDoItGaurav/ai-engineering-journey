# ============================================================
# LAMBDA FUNCTIONS IN PYTHON
# ============================================================

# A lambda function is a small anonymous function.
# Anonymous means it does not have a name.

# Syntax:
# lambda arguments : expression

# ============================================================
# NORMAL FUNCTION
# ============================================================

def square(number):
    return number * number

print(square(5))

# ============================================================
# LAMBDA FUNCTION
# ============================================================

square = lambda number: number * number

print(square(5))

# ============================================================
# LAMBDA WITH MULTIPLE PARAMETERS
# ============================================================

add = lambda a, b: a + b

print(add(10, 20))

# ============================================================
# LAMBDA FOR MULTIPLICATION
# ============================================================

multiply = lambda a, b: a * b

print(multiply(5, 4))

# ============================================================
# LAMBDA WITH CONDITIONAL EXPRESSION
# ============================================================

is_even = lambda number: True if number % 2 == 0 else False

print(is_even(10))
print(is_even(7))

# ============================================================
# USING LAMBDA WITH map()
# ============================================================

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda num: num ** 2, numbers))

print(squares)

# Output:
# [1, 4, 9, 16, 25]

# ============================================================
# USING LAMBDA WITH filter()
# ============================================================

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda num: num % 2 == 0, numbers))

print(even_numbers)

# Output:
# [2, 4, 6]

# ============================================================
# USING LAMBDA WITH sorted()
# ============================================================

students = [
    {"name": "Gaurav", "age": 21},
    {"name": "Rahul", "age": 19},
    {"name": "Priya", "age": 22}
]

sorted_students = sorted(
    students,
    key=lambda student: student["age"]
)

print(sorted_students)

# ============================================================
# SORTING STRINGS BY LENGTH
# ============================================================

names = ["Python", "AI", "Machine Learning", "Data"]

sorted_names = sorted(
    names,
    key=lambda name: len(name)
)

print(sorted_names)

# ============================================================
# PRACTICAL EXAMPLES
# ============================================================

# Example 1: Double a Number

double = lambda num: num * 2

print(double(10))

# ------------------------------------------------------------

# Example 2: Convert Celsius to Fahrenheit

celsius_to_fahrenheit = lambda temp: (temp * 9/5) + 32

print(celsius_to_fahrenheit(30))

# ------------------------------------------------------------

# Example 3: Get Student Name

student = {
    "name": "Gaurav",
    "age": 21
}

get_name = lambda data: data["name"]

print(get_name(student))

# ============================================================
# SUMMARY
# ============================================================

print("""
Lambda Function Syntax:

lambda arguments : expression

Examples:

square = lambda x: x * x

add = lambda a, b: a + b

is_even = lambda x: x % 2 == 0

Common Usage:

map()
filter()
sorted()

Benefits:

✔ Short and Concise
✔ Useful for One-Time Functions
✔ Common with map(), filter(), sorted()
""")
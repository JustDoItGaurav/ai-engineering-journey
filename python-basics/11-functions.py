# ============================================================
# FUNCTIONS IN PYTHON
# ============================================================

# A function is a block of reusable code that performs
# a specific task.

# Functions help:
# ✔ Avoid code repetition
# ✔ Improve readability
# ✔ Make programs easier to maintain

# ============================================================
# FUNCTION SYNTAX
# ============================================================

# def function_name(parameters):
#     code
#     return value

# ============================================================
# SIMPLE FUNCTION
# ============================================================

def greet():
    print("Hello, Welcome to Python!")

greet()

# ============================================================
# FUNCTION WITH PARAMETERS
# ============================================================

def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Gaurav")
greet_user("Rahul")

# ============================================================
# FUNCTION WITH MULTIPLE PARAMETERS
# ============================================================

def add(a, b):
    print(a + b)

add(10, 20)

# ============================================================
# FUNCTION WITH RETURN VALUE
# ============================================================

def square(number):
    return number * number

result = square(5)

print(result)

# ============================================================
# RETURNING MULTIPLE VALUES
# ============================================================

def calculate(a, b):
    return a + b, a - b, a * b

sum_result, diff_result, product_result = calculate(10, 5)

print(sum_result)
print(diff_result)
print(product_result)

# ============================================================
# DEFAULT PARAMETERS
# ============================================================

def greet(name="Guest"):
    print(f"Hello, {name}")

greet()
greet("Gaurav")

# ============================================================
# KEYWORD ARGUMENTS
# ============================================================

def student(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")

student(age=21, name="Gaurav")

# ============================================================
# POSITIONAL ARGUMENTS
# ============================================================

def multiply(a, b):
    print(a * b)

multiply(5, 4)

# ============================================================
# ARBITRARY ARGUMENTS (*args)
# ============================================================

def total(*numbers):
    print(sum(numbers))

total(10, 20, 30)
total(1, 2, 3, 4, 5)

# ============================================================
# KEYWORD ARBITRARY ARGUMENTS (**kwargs)
# ============================================================

def display_info(**data):
    print(data)

display_info(
    name="Gaurav",
    age=21,
    city="Delhi"
)

# ============================================================
# LOCAL VARIABLES
# ============================================================

def my_function():
    message = "Inside Function"
    print(message)

my_function()

# print(message)  # Error

# ============================================================
# GLOBAL VARIABLES
# ============================================================

name = "Python"

def show_name():
    print(name)

show_name()

# ============================================================
# RECURSION
# ============================================================

# A function calling itself.

def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))

# Output:
# 120

# ============================================================
# NESTED FUNCTIONS
# ============================================================

def outer():

    def inner():
        print("Inside Inner Function")

    inner()

outer()

# ============================================================
# PRACTICAL EXAMPLES
# ============================================================

# Example 1: Check Even Number

def is_even(number):

    return number % 2 == 0

print(is_even(10))
print(is_even(7))

# ------------------------------------------------------------

# Example 2: Celsius to Fahrenheit

def celsius_to_fahrenheit(temp):

    return (temp * 9/5) + 32

print(celsius_to_fahrenheit(30))

# ------------------------------------------------------------

# Example 3: Find Largest Number

def largest(a, b):

    if a > b:
        return a

    return b

print(largest(20, 15))

# ============================================================
# FUNCTION VS LAMBDA
# ============================================================

# Normal Function

def square(num):
    return num * num

print(square(5))

# Lambda Function

square_lambda = lambda num: num * num

print(square_lambda(5))

# ============================================================
# SUMMARY
# ============================================================

print("""

Function Syntax:

def function_name(parameters):
    code
    return value

Examples:

def greet():
    print("Hello")

def add(a, b):
    return a + b

def square(x):
    return x * x

Types:

✔ Simple Functions
✔ Functions with Parameters
✔ Return Functions
✔ Default Parameters
✔ *args
✔ **kwargs
✔ Recursive Functions

Benefits:

✔ Reusable Code
✔ Better Readability
✔ Easy Maintenance
✔ Reduces Repetition

""")
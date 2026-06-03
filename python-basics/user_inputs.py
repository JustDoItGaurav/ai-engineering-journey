# ============================================================
# USER INPUT IN PYTHON
# ============================================================

# The input() function is used to take input from the user.
# By default, input() always returns a string (str).

# ============================================================
# BASIC INPUT
# ============================================================

name = input("Enter your name: ")

print("Hello", name)

# ============================================================
# CHECKING THE DATA TYPE
# ============================================================

age = input("Enter your age: ")

print(age)
print(type(age))

# Output:
# <class 'str'>

# ============================================================
# CONVERTING INPUT TO INTEGER
# ============================================================

age = int(input("Enter your age: "))

print(age)
print(type(age))

# Output:
# <class 'int'>

# ============================================================
# CONVERTING INPUT TO FLOAT
# ============================================================

height = float(input("Enter your height: "))

print(height)
print(type(height))

# Output:
# <class 'float'>

# ============================================================
# USING F-STRINGS WITH INPUT
# ============================================================

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"My name is {name} and I am {age} years old.")

# ============================================================
# SIMPLE ADDITION PROGRAM
# ============================================================

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = num1 + num2

print("Sum =", result)

# ============================================================
# SIMPLE CALCULATOR
# ============================================================

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)
print("Division =", num1 / num2)

# ============================================================
# USER PROFILE EXAMPLE
# ============================================================

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print("\nUser Profile")
print("------------")
print("Name :", name)
print("Age  :", age)
print("City :", city)

# ============================================================
# SUMMARY
# ============================================================

print("""
Common Input Functions:

input()       -> Returns string
int(input())  -> Returns integer
float(input())-> Returns float

Examples:

name = input("Enter name: ")
age = int(input("Enter age: "))
height = float(input("Enter height: "))
""")
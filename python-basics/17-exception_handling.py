# ============================================================
# EXCEPTION HANDLING IN PYTHON
# ============================================================

# Exception Handling is used to handle runtime errors
# and prevent the program from crashing.

# Keywords:
# try
# except
# else
# finally

# ============================================================
# BASIC EXCEPTION HANDLING
# ============================================================

try:
    number = int(input("Enter a number: "))
    print(number)

except:
    print("Invalid Input")

# ============================================================
# HANDLING SPECIFIC EXCEPTIONS
# ============================================================

try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")

# ============================================================
# VALUE ERROR
# ============================================================

try:
    age = int(input("Enter your age: "))

except ValueError:
    print("Please enter a valid number")

# ============================================================
# MULTIPLE EXCEPT BLOCKS
# ============================================================

try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Please enter a valid integer")

except ZeroDivisionError:
    print("Cannot divide by zero")

# ============================================================
# USING ELSE
# ============================================================

try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid Input")

else:
    print("Input accepted")
    print(number)

# ============================================================
# USING FINALLY
# ============================================================

try:
    result = 10 / 2

except ZeroDivisionError:
    print("Division by zero")

finally:
    print("This block always executes")

# ============================================================
# EXCEPTION OBJECT
# ============================================================

try:
    number = int("abc")

except ValueError as error:
    print("Error:", error)

# ============================================================
# HANDLING MULTIPLE EXCEPTIONS TOGETHER
# ============================================================

try:
    number = int(input("Enter a number: "))
    result = 100 / number

except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero")

# ============================================================
# PRACTICAL EXAMPLE 1
# SIMPLE CALCULATOR
# ============================================================

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2

    print("Result =", result)

except ValueError:
    print("Please enter valid numbers")

except ZeroDivisionError:
    print("Cannot divide by zero")

# ============================================================
# PRACTICAL EXAMPLE 2
# LIST INDEX ERROR
# ============================================================

numbers = [10, 20, 30]

try:
    print(numbers[5])

except IndexError:
    print("Index out of range")

# ============================================================
# PRACTICAL EXAMPLE 3
# FILE NOT FOUND
# ============================================================

try:
    with open("data.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File does not exist")

# ============================================================
# RAISING EXCEPTIONS
# ============================================================

age = -5

try:

    if age < 0:
        raise ValueError("Age cannot be negative")

except ValueError as error:
    print(error)

# ============================================================
# SUMMARY
# ============================================================

print("""
Exception Handling Keywords:

try      -> Code that may cause an error
except   -> Handles the error
else     -> Runs if no error occurs
finally  -> Runs no matter what
raise    -> Manually create an exception

Common Exceptions:

ValueError
ZeroDivisionError
IndexError
FileNotFoundError
TypeError

Benefits:

✔ Prevents program crashes
✔ Improves user experience
✔ Handles unexpected input
✔ Makes code more robust
""")
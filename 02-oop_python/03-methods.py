# ============================================================
# METHODS IN PYTHON
# ============================================================

# Method:
# A method is a function defined inside a class.

# Purpose:
# Methods define the behavior/actions of objects.

# ============================================================
# BASIC METHOD
# ============================================================

class Student:

    def greet(self):
        print("Hello Student")

student1 = Student()

student1.greet()

# Output:
# Hello Student

# ============================================================
# UNDERSTANDING self
# ============================================================

# self refers to the current object.

class Student:

    def show(self):
        print("Current object:", self)

student1 = Student()

student1.show()

# ============================================================
# METHOD WITH INSTANCE VARIABLES
# ============================================================

class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

student1 = Student("Gaurav")

student1.display()

# Output:
# Name: Gaurav

# ============================================================
# MULTIPLE METHODS IN A CLASS
# ============================================================

class Student:

    def study(self):
        print("Studying")

    def sleep(self):
        print("Sleeping")

student1 = Student()

student1.study()
student1.sleep()

# Output:
# Studying
# Sleeping

# ============================================================
# METHOD WITH PARAMETERS
# ============================================================

class Calculator:

    def add(self, a, b):
        print("Sum =", a + b)

calc = Calculator()

calc.add(10, 20)

# Output:
# Sum = 30

# ============================================================
# METHOD RETURNING A VALUE
# ============================================================

class Calculator:

    def add(self, a, b):
        return a + b

calc = Calculator()

result = calc.add(5, 7)

print(result)

# Output:
# 12

# ============================================================
# REAL-WORLD EXAMPLE
# ============================================================

class Car:

    def start(self):
        print("Car Started")

    def stop(self):
        print("Car Stopped")

car1 = Car()

car1.start()
car1.stop()

# Output:
# Car Started
# Car Stopped

# ============================================================
# METHOD USING MULTIPLE ATTRIBUTES
# ============================================================

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def details(self):
        print("Name  :", self.name)
        print("Salary:", self.salary)

employee1 = Employee("Amit", 50000)

employee1.details()

# Output:
# Name  : Amit
# Salary: 50000

# ============================================================
# CALLING ONE METHOD FROM ANOTHER
# ============================================================

class Student:

    def greet(self):
        print("Hello")

    def welcome(self):
        self.greet()
        print("Welcome to Python")

student1 = Student()

student1.welcome()

# Output:
# Hello
# Welcome to Python

# ============================================================
# PRACTICAL EXAMPLES
# ============================================================

# Example 1: Mobile Class

class Mobile:

    def call(self):
        print("Calling...")

phone = Mobile()

phone.call()

# ------------------------------------------------------------

# Example 2: Bank Account

class BankAccount:

    def check_balance(self):
        print("Balance Checked")

account = BankAccount()

account.check_balance()

# ------------------------------------------------------------

# Example 3: Calculator

class Calculator:

    def multiply(self, a, b):
        print("Product =", a * b)

calc = Calculator()

calc.multiply(5, 4)

# Output:
# Product = 20

# ============================================================
# SUMMARY
# ============================================================

print("""
Methods:

Method -> Function inside a class

Purpose:
- Define object behavior
- Perform actions
- Process data

self -> Refers to current object

Types of Methods Covered:

1. Basic Method
2. Method with Parameters
3. Method with Return Value
4. Method Using Attributes
5. Method Calling Another Method

Syntax:

class MyClass:

    def method_name(self):
        pass
""")
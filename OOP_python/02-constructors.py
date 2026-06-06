# ============================================================
# CONSTRUCTORS (__init__) IN PYTHON
# ============================================================

# Constructor:
# A special method that automatically executes when
# an object is created.

# Constructor Name:
# __init__()

# Purpose:
# Used to initialize object data.

# ============================================================
# BASIC CONSTRUCTOR
# ============================================================

class Student:

    def __init__(self):
        print("Constructor Executed")

student1 = Student()

# Output:
# Constructor Executed

# ============================================================
# WHY USE CONSTRUCTORS?
# ============================================================

# Without constructor, values must be assigned manually.

class Student:
    pass

student1 = Student()

student1.name = "Gaurav"
student1.age = 21

print(student1.name)
print(student1.age)

# Output:
# Gaurav
# 21

# ============================================================
# CONSTRUCTOR WITH PARAMETERS
# ============================================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Gaurav", 21)

print(student1.name)
print(student1.age)

# Output:
# Gaurav
# 21

# ============================================================
# CREATING MULTIPLE OBJECTS
# ============================================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Gaurav", 21)
student2 = Student("Rahul", 20)

print(student1.name, student1.age)
print(student2.name, student2.age)

# Output:
# Gaurav 21
# Rahul 20

# ============================================================
# USING CONSTRUCTOR IN REAL-WORLD EXAMPLE
# ============================================================

class Car:

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car1 = Car("Toyota", "Black")

print(car1.brand)
print(car1.color)

# Output:
# Toyota
# Black

# ============================================================
# DEFAULT VALUES IN CONSTRUCTOR
# ============================================================

class Employee:

    def __init__(self, name="Unknown"):
        self.name = name

employee1 = Employee()
employee2 = Employee("Amit")

print(employee1.name)
print(employee2.name)

# Output:
# Unknown
# Amit

# ============================================================
# CONSTRUCTOR WITH MULTIPLE ATTRIBUTES
# ============================================================

class Laptop:

    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price

laptop1 = Laptop("HP", 16, 65000)

print(laptop1.brand)
print(laptop1.ram)
print(laptop1.price)

# Output:
# HP
# 16
# 65000

# ============================================================
# PRINTING OBJECT DATA
# ============================================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Gaurav", 21)

print("Name:", student1.name)
print("Age :", student1.age)

# Output:
# Name: Gaurav
# Age : 21

# ============================================================
# PRACTICAL EXAMPLES
# ============================================================

# Example 1: Mobile Class

class Mobile:

    def __init__(self, brand):
        self.brand = brand

phone = Mobile("Samsung")

print(phone.brand)

# ------------------------------------------------------------

# Example 2: Book Class

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("Python Basics", "Gaurav")

print(book1.title)
print(book1.author)

# ------------------------------------------------------------

# Example 3: Bank Account

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

account = BankAccount(5000)

print(account.balance)

# ============================================================
# SUMMARY
# ============================================================

print("""
Constructors (__init__):

__init__()  -> Special method

Purpose:
- Automatically runs when object is created
- Initializes object data

self        -> Refers to current object

Constructor can:
- Accept parameters
- Set attributes
- Initialize object state

Syntax:

class MyClass:

    def __init__(self):
        pass
""")
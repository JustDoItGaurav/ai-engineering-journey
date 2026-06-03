# ============================================================
# CLASSES AND OBJECTS IN PYTHON
# ============================================================

# A Class is a blueprint/template for creating objects.
# An Object is an instance of a class.

# Example:
# Class -> Student
# Object -> Gaurav, Rahul, Priya

# ============================================================
# CREATING A CLASS
# ============================================================

class Student:
    pass

# Creating Objects

student1 = Student()
student2 = Student()

print(student1)
print(student2)

# ============================================================
# CLASS WITH ATTRIBUTES
# ============================================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating Objects

student1 = Student("Gaurav", 21)
student2 = Student("Rahul", 22)

print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)

# ============================================================
# INSTANCE METHODS
# ============================================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}")
        print(f"I am {self.age} years old")

student = Student("Gaurav", 21)

student.introduce()

# ============================================================
# MULTIPLE OBJECTS
# ============================================================

student1 = Student("Gaurav", 21)
student2 = Student("Rahul", 22)
student3 = Student("Priya", 20)

student1.introduce()
student2.introduce()
student3.introduce()

# ============================================================
# MODIFYING OBJECT ATTRIBUTES
# ============================================================

student = Student("Gaurav", 21)

print(student.age)

student.age = 22

print(student.age)

# ============================================================
# DELETING ATTRIBUTES
# ============================================================

student = Student("Gaurav", 21)

del student.age

# print(student.age)  # Error

# ============================================================
# CLASS WITH RETURN METHODS
# ============================================================

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

calc = Calculator()

print(calc.add(10, 20))
print(calc.subtract(20, 10))

# ============================================================
# CLASS VARIABLES
# ============================================================

class Student:

    school = "Pillai College"

    def __init__(self, name):
        self.name = name

student1 = Student("Gaurav")
student2 = Student("Rahul")

print(student1.school)
print(student2.school)

# ============================================================
# PRACTICAL EXAMPLE 1
# BANK ACCOUNT
# ============================================================

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_balance(self):
        print(f"Balance: {self.balance}")

account = BankAccount("Gaurav", 1000)

account.deposit(500)
account.withdraw(200)

account.display_balance()

# ============================================================
# PRACTICAL EXAMPLE 2
# CAR
# ============================================================

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"{self.brand} {self.model}")

car = Car("Toyota", "Camry")

car.display()

# ============================================================
# PRACTICAL EXAMPLE 3
# STUDENT
# ============================================================

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

student = Student("Gaurav", 95)

student.display()

# ============================================================
# SUMMARY
# ============================================================

print("""
OOP Concepts:

class      -> Blueprint
object     -> Instance of a class
__init__() -> Constructor
self       -> Refers to current object
method     -> Function inside a class

Syntax:

class Student:

    def __init__(self, name):
        self.name = name

student = Student("Gaurav")

Benefits:

✔ Code Reusability
✔ Better Organization
✔ Real World Modeling
✔ Easier Maintenance
""")
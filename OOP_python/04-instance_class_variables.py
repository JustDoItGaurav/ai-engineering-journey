# ============================================================
# INSTANCE VARIABLES VS CLASS VARIABLES IN PYTHON
# ============================================================

# Variables inside a class are mainly of two types:
#
# 1. Instance Variables
# 2. Class Variables

# ============================================================
# INSTANCE VARIABLES
# ============================================================

# Instance Variables:
# Variables that belong to a specific object.

# Each object gets its own copy.

class Student:

    def __init__(self, name):
        self.name = name

student1 = Student("Gaurav")
student2 = Student("Rahul")

print(student1.name)
print(student2.name)

# Output:
# Gaurav
# Rahul

# ============================================================
# CHANGING INSTANCE VARIABLES
# ============================================================

class Student:

    def __init__(self, name):
        self.name = name

student1 = Student("Gaurav")
student2 = Student("Rahul")

student1.name = "Amit"

print(student1.name)
print(student2.name)

# Output:
# Amit
# Rahul

# Only student1 changes.

# ============================================================
# CLASS VARIABLES
# ============================================================

# Class Variables:
# Variables shared by all objects of the class.

class Student:

    school = "ABC School"

student1 = Student()
student2 = Student()

print(student1.school)
print(student2.school)

# Output:
# ABC School
# ABC School

# ============================================================
# MODIFYING CLASS VARIABLES
# ============================================================

class Student:

    school = "ABC School"

student1 = Student()
student2 = Student()

Student.school = "XYZ School"

print(student1.school)
print(student2.school)

# Output:
# XYZ School
# XYZ School

# Changes affect all objects.

# ============================================================
# USING INSTANCE AND CLASS VARIABLES TOGETHER
# ============================================================

class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name

student1 = Student("Gaurav")
student2 = Student("Rahul")

print(student1.name, "-", student1.school)
print(student2.name, "-", student2.school)

# Output:
# Gaurav - ABC School
# Rahul - ABC School

# ============================================================
# ACCESSING CLASS VARIABLES
# ============================================================

class Student:

    school = "ABC School"

print(Student.school)

# Output:
# ABC School

# ============================================================
# ACCESSING CLASS VARIABLES USING OBJECTS
# ============================================================

class Student:

    school = "ABC School"

student1 = Student()

print(student1.school)

# Output:
# ABC School

# ============================================================
# OVERRIDING CLASS VARIABLES
# ============================================================

class Student:

    school = "ABC School"

student1 = Student()

student1.school = "XYZ School"

print(student1.school)
print(Student.school)

# Output:
# XYZ School
# ABC School

# student1 now has its own instance variable.

# ============================================================
# REAL-WORLD EXAMPLE
# ============================================================

class Employee:

    company = "Google"

    def __init__(self, name):
        self.name = name

employee1 = Employee("Amit")
employee2 = Employee("Rohit")

print(employee1.name, "-", employee1.company)
print(employee2.name, "-", employee2.company)

# Output:
# Amit - Google
# Rohit - Google

# ============================================================
# COMPARISON EXAMPLE
# ============================================================

class Car:

    wheels = 4

    def __init__(self, color):
        self.color = color

car1 = Car("Black")
car2 = Car("White")

print(car1.color)
print(car2.color)

print(car1.wheels)
print(car2.wheels)

# Output:
# Black
# White
# 4
# 4

# color  -> Instance Variable
# wheels -> Class Variable

# ============================================================
# PRACTICAL EXAMPLES
# ============================================================

# Example 1

class Mobile:

    brand = "Samsung"

    def __init__(self, model):
        self.model = model

phone1 = Mobile("S24")
phone2 = Mobile("A55")

print(phone1.model)
print(phone2.model)

print(phone1.brand)

# ------------------------------------------------------------

# Example 2

class Book:

    category = "Programming"

    def __init__(self, title):
        self.title = title

book1 = Book("Python Basics")

print(book1.title)
print(book1.category)

# ------------------------------------------------------------

# Example 3

class Bank:

    bank_name = "SBI"

    def __init__(self, customer):
        self.customer = customer

account = Bank("Gaurav")

print(account.customer)
print(account.bank_name)

# ============================================================
# SUMMARY
# ============================================================

print("""
Instance Variables vs Class Variables

Instance Variable:
- Belongs to an object
- Created using self.variable
- Separate copy for each object

Class Variable:
- Belongs to the class
- Defined directly inside class
- Shared by all objects

Example:

class Student:

    school = "ABC School"     # Class Variable

    def __init__(self, name):
        self.name = name      # Instance Variable
""")
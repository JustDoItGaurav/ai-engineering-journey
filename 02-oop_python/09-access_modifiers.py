# ============================================================
# ACCESS MODIFIERS IN PYTHON
# ============================================================

# Access Modifiers:
# Control the accessibility (visibility)
# of variables and methods.

# Python provides three types:

# 1. Public
# 2. Protected
# 3. Private

# ============================================================
# PUBLIC MEMBERS
# ============================================================

# Public members can be accessed
# from anywhere.

class Student:

    def __init__(self):
        self.name = "Gaurav"

student1 = Student()

print(student1.name)

# Output:
# Gaurav

# ============================================================
# PUBLIC METHODS
# ============================================================

class Student:

    def show(self):
        print("Public Method")

student1 = Student()

student1.show()

# Output:
# Public Method

# ============================================================
# MODIFYING PUBLIC VARIABLES
# ============================================================

class Student:

    def __init__(self):
        self.name = "Gaurav"

student1 = Student()

student1.name = "Rahul"

print(student1.name)

# Output:
# Rahul

# ============================================================
# PROTECTED MEMBERS
# ============================================================

# Protected members start with
# a single underscore (_)

# Syntax:
# _variable
# _method()

# Convention:
# Should not be accessed directly
# outside the class.

class Student:

    def __init__(self):
        self._name = "Gaurav"

student1 = Student()

print(student1._name)

# Output:
# Gaurav

# Accessible, but not recommended.

# ============================================================
# PROTECTED METHOD
# ============================================================

class Student:

    def _show(self):
        print("Protected Method")

student1 = Student()

student1._show()

# Output:
# Protected Method

# ============================================================
# PROTECTED MEMBERS IN INHERITANCE
# ============================================================

class Person:

    def __init__(self):
        self._name = "Gaurav"

class Student(Person):

    def display(self):
        print(self._name)

student1 = Student()

student1.display()

# Output:
# Gaurav

# Child classes can access protected members.

# ============================================================
# PRIVATE MEMBERS
# ============================================================

# Private members start with
# double underscore (__)

# Syntax:
# __variable
# __method()

# Direct access is restricted.

class Student:

    def __init__(self):
        self.__name = "Gaurav"

student1 = Student()

# print(student1.__name)

# Output:
# AttributeError

# ============================================================
# ACCESSING PRIVATE MEMBERS USING METHODS
# ============================================================

class Student:

    def __init__(self):
        self.__name = "Gaurav"

    def get_name(self):
        return self.__name

student1 = Student()

print(student1.get_name())

# Output:
# Gaurav

# ============================================================
# MODIFYING PRIVATE MEMBERS USING METHODS
# ============================================================

class Student:

    def __init__(self):
        self.__name = "Gaurav"

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

student1 = Student()

student1.set_name("Rahul")

print(student1.get_name())

# Output:
# Rahul

# ============================================================
# PRIVATE METHODS
# ============================================================

class Student:

    def __show(self):
        print("Private Method")

    def access_method(self):
        self.__show()

student1 = Student()

student1.access_method()

# Output:
# Private Method

# ============================================================
# NAME MANGLING
# ============================================================

# Python internally changes:

# __name

# to

# _ClassName__name

class Student:

    def __init__(self):
        self.__name = "Gaurav"

student1 = Student()

print(student1._Student__name)

# Output:
# Gaurav

# This process is called Name Mangling.

# ============================================================
# COMPARISON OF ACCESS MODIFIERS
# ============================================================

class Demo:

    public_var = "Public"

    _protected_var = "Protected"

    __private_var = "Private"

print(Demo.public_var)

print(Demo._protected_var)

# print(Demo.__private_var)
# Error

# ============================================================
# REAL-WORLD EXAMPLE
# ============================================================

class BankAccount:

    def __init__(self):

        self.account_holder = "Gaurav"     # Public

        self._account_type = "Savings"     # Protected

        self.__balance = 5000              # Private

    def get_balance(self):
        return self.__balance

account = BankAccount()

print(account.account_holder)

print(account._account_type)

print(account.get_balance())

# Output:
# Gaurav
# Savings
# 5000

# ============================================================
# PRACTICAL EXAMPLES
# ============================================================

# Example 1

class Mobile:

    def __init__(self):

        self.brand = "Samsung"

        self._model = "S24"

        self.__price = 80000

    def get_price(self):
        return self.__price

phone = Mobile()

print(phone.brand)
print(phone._model)
print(phone.get_price())

# ------------------------------------------------------------

# Example 2

class Employee:

    def __init__(self):

        self.name = "Amit"

        self._department = "IT"

        self.__salary = 50000

    def get_salary(self):
        return self.__salary

employee = Employee()

print(employee.name)
print(employee._department)
print(employee.get_salary())

# ------------------------------------------------------------

# Example 3

class Laptop:

    def __init__(self):

        self.brand = "HP"

        self._ram = 16

        self.__price = 65000

    def get_price(self):
        return self.__price

laptop = Laptop()

print(laptop.brand)
print(laptop._ram)
print(laptop.get_price())

# ============================================================
# SUMMARY
# ============================================================

print("""
Access Modifiers:

1. Public
   -> Accessible everywhere

2. Protected
   -> Accessible inside class
      and child classes

   Syntax:
   _variable

3. Private
   -> Accessible only inside class

   Syntax:
   __variable

Name Mangling:

__name

becomes

_ClassName__name

Purpose:

- Data Protection
- Controlled Access
- Better Encapsulation

Example:

public_var

_protected_var

__private_var
""")
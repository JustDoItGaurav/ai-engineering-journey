# ============================================================
# ENCAPSULATION IN PYTHON
# ============================================================

# Encapsulation:
# Wrapping data (variables) and methods into a single unit
# and restricting direct access to some data.

# Purpose:
# - Data Security
# - Data Hiding
# - Controlled Access

# ============================================================
# ACCESS MODIFIERS IN PYTHON
# ============================================================

# Public Variable      -> variable
# Protected Variable   -> _variable
# Private Variable     -> __variable

# ============================================================
# PUBLIC VARIABLES
# ============================================================

class Student:

    def __init__(self):
        self.name = "Gaurav"

student1 = Student()

print(student1.name)

# Output:
# Gaurav

# Public variables can be accessed directly.

# ============================================================
# PROTECTED VARIABLES
# ============================================================

class Student:

    def __init__(self):
        self._name = "Gaurav"

student1 = Student()

print(student1._name)

# Output:
# Gaurav

# Protected variables should not be accessed directly
# outside the class (convention only).

# ============================================================
# PRIVATE VARIABLES
# ============================================================

class Student:

    def __init__(self):
        self.__name = "Gaurav"

student1 = Student()

# print(student1.__name)

# Output:
# AttributeError

# Private variables cannot be accessed directly.

# ============================================================
# ACCESSING PRIVATE VARIABLES USING METHODS
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
# MODIFYING PRIVATE VARIABLES USING METHODS
# ============================================================

class Student:

    def __init__(self):
        self.__name = "Gaurav"

    def set_name(self, new_name):
        self.__name = new_name

    def get_name(self):
        return self.__name

student1 = Student()

student1.set_name("Rahul")

print(student1.get_name())

# Output:
# Rahul

# ============================================================
# BANK ACCOUNT EXAMPLE
# ============================================================

class BankAccount:

    def __init__(self):
        self.__balance = 1000

    def get_balance(self):
        return self.__balance

account = BankAccount()

print(account.get_balance())

# Output:
# 1000

# ============================================================
# DEPOSIT METHOD
# ============================================================

class BankAccount:

    def __init__(self):
        self.__balance = 1000

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount()

account.deposit(500)

print(account.get_balance())

# Output:
# 1500

# ============================================================
# WITHDRAW METHOD
# ============================================================

class BankAccount:

    def __init__(self):
        self.__balance = 5000

    def withdraw(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal Successful")

        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance

account = BankAccount()

account.withdraw(2000)

print(account.get_balance())

# Output:
# Withdrawal Successful
# 3000

# ============================================================
# UNDERSTANDING NAME MANGLING
# ============================================================

class Student:

    def __init__(self):
        self.__name = "Gaurav"

student1 = Student()

print(student1._Student__name)

# Output:
# Gaurav

# Python internally changes:
# __name -> _Student__name

# This process is called Name Mangling.

# ============================================================
# REAL-WORLD EXAMPLE
# ============================================================

class Employee:

    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

employee1 = Employee(50000)

print(employee1.get_salary())

# Output:
# 50000

# ============================================================
# PRACTICAL EXAMPLES
# ============================================================

# Example 1

class User:

    def __init__(self):
        self.__password = "admin123"

    def show_password(self):
        return self.__password

user = User()

print(user.show_password())

# ------------------------------------------------------------

# Example 2

class Mobile:

    def __init__(self):
        self.__price = 50000

    def get_price(self):
        return self.__price

phone = Mobile()

print(phone.get_price())

# ------------------------------------------------------------

# Example 3

class Laptop:

    def __init__(self):
        self.__ram = 16

    def get_ram(self):
        return self.__ram

laptop = Laptop()

print(laptop.get_ram())

# ============================================================
# SUMMARY
# ============================================================

print("""
Encapsulation:

Encapsulation
    -> Data Hiding + Controlled Access

Access Modifiers:

Public Variable
    -> variable

Protected Variable
    -> _variable

Private Variable
    -> __variable

Private variables:
- Cannot be accessed directly
- Accessed through methods

Benefits:
- Data Security
- Better Control
- Code Maintainability

Common Methods:

Getter
    -> Read data

Setter
    -> Modify data

Syntax:

class MyClass:

    def __init__(self):
        self.__data = 100
""")
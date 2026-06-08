# ============================================================
# ABSTRACTION IN PYTHON
# ============================================================

# Abstraction:
# Hiding implementation details and showing only
# essential features to the user.

# Real-Life Example:
# When driving a car, you use the steering wheel,
# accelerator, and brakes.
#
# You don't need to know how the engine works internally.

# ============================================================
# WHY ABSTRACTION?
# ============================================================

# Benefits:
#
# 1. Hides complex implementation
# 2. Improves security
# 3. Reduces code complexity
# 4. Makes code easier to maintain

# ============================================================
# ABSTRACT CLASSES
# ============================================================

# Python provides abstraction through the abc module.

from abc import ABC, abstractmethod

# ABC = Abstract Base Class

# ============================================================
# CREATING AN ABSTRACT CLASS
# ============================================================

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

# Cannot create object of abstract class

# animal = Animal()   # Error

# ============================================================
# IMPLEMENTING ABSTRACT METHODS
# ============================================================

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Bark")

dog = Dog()

dog.sound()

# Output:
# Bark

# ============================================================
# MULTIPLE CHILD CLASSES
# ============================================================

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Bark")

class Cat(Animal):

    def sound(self):
        print("Meow")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

# Output:
# Bark
# Meow

# ============================================================
# ABSTRACT CLASS WITH MULTIPLE METHODS
# ============================================================

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car Started")

    def stop(self):
        print("Car Stopped")

car = Car()

car.start()
car.stop()

# Output:
# Car Started
# Car Stopped

# ============================================================
# CHILD CLASS MUST IMPLEMENT ABSTRACT METHODS
# ============================================================

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

# This class is incomplete

class Circle(Shape):
    pass

# circle = Circle()

# Error:
# Can't instantiate abstract class Circle

# ============================================================
# COMPLETE IMPLEMENTATION
# ============================================================

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def area(self):
        print("Area of Circle")

circle = Circle()

circle.area()

# Output:
# Area of Circle

# ============================================================
# REAL-WORLD EXAMPLE
# ============================================================

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

class CreditCard(Payment):

    def pay(self):
        print("Paid using Credit Card")

class UPI(Payment):

    def pay(self):
        print("Paid using UPI")

card = CreditCard()
upi = UPI()

card.pay()
upi.pay()

# Output:
# Paid using Credit Card
# Paid using UPI

# ============================================================
# ABSTRACT CLASS CAN HAVE NORMAL METHODS
# ============================================================

from abc import ABC, abstractmethod

class Animal(ABC):

    def sleep(self):
        print("Sleeping")

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Bark")

dog = Dog()

dog.sleep()
dog.sound()

# Output:
# Sleeping
# Bark

# ============================================================
# PRACTICAL EXAMPLES
# ============================================================

# Example 1

from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def work(self):
        pass

class Developer(Employee):

    def work(self):
        print("Writing Code")

developer = Developer()

developer.work()

# ------------------------------------------------------------

# Example 2

from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def send(self):
        pass

class Email(Notification):

    def send(self):
        print("Sending Email")

email = Email()

email.send()

# ------------------------------------------------------------

# Example 3

from abc import ABC, abstractmethod

class Database(ABC):

    @abstractmethod
    def connect(self):
        pass

class MySQL(Database):

    def connect(self):
        print("Connected to MySQL")

db = MySQL()

db.connect()

# ============================================================
# SUMMARY
# ============================================================

print("""
Abstraction:

Definition:
- Hide implementation details
- Show only essential functionality

Module:
from abc import ABC, abstractmethod

Important Terms:

ABC
    -> Abstract Base Class

@abstractmethod
    -> Defines an abstract method

Rules:

1. Cannot create object of abstract class

2. Child class must implement
   all abstract methods

3. Abstract class can contain
   normal methods as well

Benefits:

- Security
- Simplicity
- Better Design
- Easy Maintenance

Syntax:

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
""")
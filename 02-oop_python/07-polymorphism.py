# ============================================================
# POLYMORPHISM IN PYTHON
# ============================================================

# Polymorphism:
# "Poly" = Many
# "Morphism" = Forms

# Meaning:
# The same method name can perform different actions
# depending on the object that calls it.

# ============================================================
# BASIC EXAMPLE
# ============================================================

class Dog:

    def sound(self):
        print("Bark")

class Cat:

    def sound(self):
        print("Meow")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

# Output:
# Bark
# Meow

# Same method name: sound()
# Different behavior.

# ============================================================
# ANOTHER EXAMPLE
# ============================================================

class Bird:

    def move(self):
        print("Flying")

class Fish:

    def move(self):
        print("Swimming")

bird = Bird()
fish = Fish()

bird.move()
fish.move()

# Output:
# Flying
# Swimming

# ============================================================
# POLYMORPHISM USING LOOP
# ============================================================

class Dog:

    def sound(self):
        print("Bark")

class Cat:

    def sound(self):
        print("Meow")

animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()

# Output:
# Bark
# Meow

# Same code works for different objects.

# ============================================================
# POLYMORPHISM WITH FUNCTIONS
# ============================================================

class Dog:

    def sound(self):
        print("Bark")

class Cat:

    def sound(self):
        print("Meow")

def make_sound(animal):
    animal.sound()

dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)

# Output:
# Bark
# Meow

# ============================================================
# POLYMORPHISM THROUGH INHERITANCE
# ============================================================

class Animal:

    def sound(self):
        print("Animal Sound")

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

# Child classes override the parent method.

# ============================================================
# METHOD OVERRIDING
# ============================================================

class Vehicle:

    def start(self):
        print("Vehicle Started")

class Car(Vehicle):

    def start(self):
        print("Car Started")

car = Car()

car.start()

# Output:
# Car Started

# ============================================================
# REAL-WORLD EXAMPLE
# ============================================================

class Payment:

    def pay(self):
        print("Processing Payment")

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
# BUILT-IN POLYMORPHISM
# ============================================================

print(len("Python"))

print(len([10, 20, 30]))

print(len((1, 2, 3, 4)))

# Output:
# 6
# 3
# 4

# Same len() function works for
# different types of objects.

# ============================================================
# OPERATOR POLYMORPHISM
# ============================================================

print(10 + 20)

print("Hello " + "World")

# Output:
# 30
# Hello World

# + behaves differently depending
# on the data type.

# ============================================================
# PRACTICAL EXAMPLES
# ============================================================

# Example 1

class Shape:

    def area(self):
        print("Calculating Area")

class Circle(Shape):

    def area(self):
        print("Area of Circle")

class Rectangle(Shape):

    def area(self):
        print("Area of Rectangle")

circle = Circle()
rectangle = Rectangle()

circle.area()
rectangle.area()

# ------------------------------------------------------------

# Example 2

class Employee:

    def work(self):
        print("Employee Working")

class Developer(Employee):

    def work(self):
        print("Writing Code")

class Tester(Employee):

    def work(self):
        print("Testing Application")

developer = Developer()
tester = Tester()

developer.work()
tester.work()

# ------------------------------------------------------------

# Example 3

class Notification:

    def send(self):
        print("Sending Notification")

class Email(Notification):

    def send(self):
        print("Sending Email")

class SMS(Notification):

    def send(self):
        print("Sending SMS")

email = Email()
sms = SMS()

email.send()
sms.send()

# ============================================================
# SUMMARY
# ============================================================

print("""
Polymorphism:

Poly      -> Many
Morphism  -> Forms

Definition:
- Same method name
- Different behavior

Achieved Through:

1. Method Overriding
2. Inheritance
3. Duck Typing
4. Built-in Functions

Examples:

sound()
move()
pay()
area()

Benefits:
- Flexible Code
- Reusable Code
- Easy Maintenance

Method Overriding:

class Parent:

    def show(self):
        pass

class Child(Parent):

    def show(self):
        pass
""")
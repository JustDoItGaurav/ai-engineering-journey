# ============================================================
# INHERITANCE IN PYTHON
# ============================================================

# Inheritance:
# A mechanism that allows one class to acquire
# properties and methods from another class.

# Parent Class (Base Class):
# Class whose properties are inherited.

# Child Class (Derived Class):
# Class that inherits properties from another class.

# ============================================================
# BASIC INHERITANCE
# ============================================================

class Animal:

    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    pass

dog = Dog()

dog.eat()

# Output:
# Animal is eating

# ============================================================
# UNDERSTANDING THE FLOW
# ============================================================

# Parent Class --> Animal
# Child Class  --> Dog

# Dog automatically gets access to
# methods present in Animal.

# ============================================================
# INHERITING MULTIPLE METHODS
# ============================================================

class Animal:

    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")

class Dog(Animal):
    pass

dog = Dog()

dog.eat()
dog.sleep()

# Output:
# Eating
# Sleeping

# ============================================================
# ADDING NEW METHODS IN CHILD CLASS
# ============================================================

class Animal:

    def eat(self):
        print("Eating")

class Dog(Animal):

    def bark(self):
        print("Barking")

dog = Dog()

dog.eat()
dog.bark()

# Output:
# Eating
# Barking

# ============================================================
# USING CONSTRUCTORS WITH INHERITANCE
# ============================================================

class Person:

    def __init__(self, name):
        self.name = name

class Student(Person):
    pass

student1 = Student("Gaurav")

print(student1.name)

# Output:
# Gaurav

# ============================================================
# METHOD OVERRIDING
# ============================================================

# Child class can redefine a method
# already present in parent class.

class Animal:

    def sound(self):
        print("Animal Sound")

class Dog(Animal):

    def sound(self):
        print("Bark")

dog = Dog()

dog.sound()

# Output:
# Bark

# ============================================================
# SINGLE INHERITANCE
# ============================================================

class Parent:

    def show(self):
        print("Parent Class")

class Child(Parent):
    pass

child = Child()

child.show()

# ============================================================
# MULTILEVEL INHERITANCE
# ============================================================

class GrandParent:

    def house(self):
        print("Grandparent's House")

class Parent(GrandParent):
    pass

class Child(Parent):
    pass

child = Child()

child.house()

# Output:
# Grandparent's House

# ============================================================
# HIERARCHICAL INHERITANCE
# ============================================================

class Animal:

    def eat(self):
        print("Eating")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
cat = Cat()

dog.eat()
cat.eat()

# Output:
# Eating
# Eating

# ============================================================
# USING isinstance()
# ============================================================

class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))

# Output:
# True
# True

# ============================================================
# REAL-WORLD EXAMPLE
# ============================================================

class Vehicle:

    def start(self):
        print("Vehicle Started")

class Car(Vehicle):
    pass

car = Car()

car.start()

# Output:
# Vehicle Started

# ============================================================
# PRACTICAL EXAMPLES
# ============================================================

# Example 1

class Person:

    def introduce(self):
        print("I am a person")

class Student(Person):
    pass

student1 = Student()

student1.introduce()

# ------------------------------------------------------------

# Example 2

class Animal:

    def eat(self):
        print("Eating")

class Bird(Animal):

    def fly(self):
        print("Flying")

bird = Bird()

bird.eat()
bird.fly()

# ------------------------------------------------------------

# Example 3

class Employee:

    def work(self):
        print("Working")

class Manager(Employee):

    def manage(self):
        print("Managing Team")

manager = Manager()

manager.work()
manager.manage()

# ============================================================
# SUMMARY
# ============================================================

print("""
Inheritance:

Inheritance
    -> Acquire properties and methods
       from another class

Parent Class
    -> Class being inherited

Child Class
    -> Class that inherits

Benefits:
- Code Reusability
- Easy Maintenance
- Better Organization

Types Covered:

1. Single Inheritance
2. Multilevel Inheritance
3. Hierarchical Inheritance

Method Overriding:
- Child class can redefine
  parent class methods

Syntax:

class Parent:
    pass

class Child(Parent):
    pass
""")
# ============================================================
# IMPORTANT OOP TOPICS FOR AI ENGINEERS
# ============================================================
#
# Topics Covered:
# 1. super()
# 2. Static Methods (@staticmethod)
# 3. Class Methods (@classmethod)
# 4. __str__()
# 5. __repr__()
# 6. Composition
#
# These are the OOP concepts you are most likely to encounter
# while working with PyTorch, LangChain, LLM applications,
# AI agents, and production Python code.
#
# ============================================================



# ============================================================
# 1. super() METHOD
# ============================================================

# super() is used to call methods or constructors
# of the parent class.

class Person:

    def __init__(self, name):
        self.name = name

class Student(Person):

    def __init__(self, name, course):

        # Call Parent Constructor
        super().__init__(name)

        self.course = course

student1 = Student("Gaurav", "AI Engineering")

print(student1.name)
print(student1.course)

# Output:
# Gaurav
# AI Engineering

# ------------------------------------------------------------
# Real AI Example
# ------------------------------------------------------------

class Model:

    def __init__(self):
        print("Base Model Initialized")

class NeuralNetwork(Model):

    def __init__(self):

        super().__init__()

        print("Neural Network Initialized")

nn = NeuralNetwork()

# Output:
# Base Model Initialized
# Neural Network Initialized



# ============================================================
# 2. STATIC METHODS
# ============================================================

# Static methods belong to the class.
# They do not use self or cls.

class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(10, 20))

# Output:
# 30

# ------------------------------------------------------------
# Real AI Example
# ------------------------------------------------------------

class DataCleaner:

    @staticmethod
    def clean_text(text):

        return text.lower().strip()

print(DataCleaner.clean_text("   HELLO WORLD   "))

# Output:
# hello world



# ============================================================
# 3. CLASS METHODS
# ============================================================

# Class methods use cls.
# They work with the class itself.

class Student:

    school = "ABC School"

    @classmethod
    def show_school(cls):

        print(cls.school)

Student.show_school()

# Output:
# ABC School

# ------------------------------------------------------------
# Factory Method Example
# ------------------------------------------------------------

class User:

    def __init__(self, name):
        self.name = name

    @classmethod
    def from_dict(cls, data):

        return cls(data["name"])

user_data = {
    "name": "Gaurav"
}

user = User.from_dict(user_data)

print(user.name)

# Output:
# Gaurav



# ============================================================
# 4. __str__()
# ============================================================

# __str__() controls how an object is displayed
# when using print().

class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):

        return f"Student Name: {self.name}"

student1 = Student("Gaurav")

print(student1)

# Output:
# Student Name: Gaurav

# Without __str__:
# <__main__.Student object at 0x...>



# ============================================================
# 5. __repr__()
# ============================================================

# __repr__() provides an official string
# representation of the object.

class Student:

    def __init__(self, name):
        self.name = name

    def __repr__(self):

        return f"Student('{self.name}')"

student1 = Student("Gaurav")

print(student1)

# Output:
# Student('Gaurav')

# Useful for debugging and logging.



# ============================================================
# __str__() vs __repr__()
# ============================================================

class Employee:

    def __init__(self, name):
        self.name = name

    def __str__(self):

        return f"Employee: {self.name}"

    def __repr__(self):

        return f"Employee('{self.name}')"

employee1 = Employee("Amit")

print(employee1)

# Output:
# Employee: Amit



# ============================================================
# 6. COMPOSITION
# ============================================================

# Composition means:
#
# HAS-A Relationship
#
# One class contains another class as an object.

# ============================================================
# BASIC EXAMPLE
# ============================================================

class Engine:

    def start(self):
        print("Engine Started")

class Car:

    def __init__(self):

        self.engine = Engine()

car = Car()

car.engine.start()

# Output:
# Engine Started

# Car HAS-A Engine



# ============================================================
# AI EXAMPLE
# ============================================================

class LLM:

    def generate(self):

        return "AI Response"

class Memory:

    def store(self):

        print("Memory Stored")

class Agent:

    def __init__(self):

        self.llm = LLM()

        self.memory = Memory()

agent = Agent()

print(agent.llm.generate())

agent.memory.store()

# Output:
# AI Response
# Memory Stored

# Agent HAS-A LLM
# Agent HAS-A Memory

# This is how many AI systems are designed.



# ============================================================
# PRACTICAL EXAMPLES
# ============================================================

# Example 1

class Calculator:

    @staticmethod
    def multiply(a, b):

        return a * b

print(Calculator.multiply(5, 4))

# ------------------------------------------------------------

# Example 2

class Product:

    def __init__(self, name):

        self.name = name

    def __str__(self):

        return self.name

product = Product("Laptop")

print(product)

# ------------------------------------------------------------

# Example 3

class Database:

    def connect(self):

        print("Connected")

class Application:

    def __init__(self):

        self.database = Database()

app = Application()

app.database.connect()



# ============================================================
# SUMMARY
# ============================================================

print("""
IMPORTANT OOP FOR AI ENGINEERS

1. super()
   -> Call parent constructor/method

2. @staticmethod
   -> Utility functions

3. @classmethod
   -> Factory methods
   -> Class-level operations

4. __str__()
   -> Human-readable object output

5. __repr__()
   -> Debug representation

6. Composition
   -> HAS-A relationship

AI Examples:

Agent HAS-A LLM
Agent HAS-A Memory
Agent HAS-A Vector Store

These concepts are commonly used in:

- PyTorch
- LangChain
- CrewAI
- AutoGen
- AI Agents
- Production Python Applications
""")
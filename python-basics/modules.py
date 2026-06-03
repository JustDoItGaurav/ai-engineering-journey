# ============================================================
# MODULES IN PYTHON
# ============================================================

# A module is a Python file that contains functions,
# variables, and classes that can be reused in other files.

# Python provides many built-in modules such as:
# math, random, datetime, os, etc.

# ============================================================
# IMPORTING A MODULE
# ============================================================

import math

print(math.sqrt(25))
print(math.pi)

# ============================================================
# IMPORTING SPECIFIC FUNCTIONS
# ============================================================

from math import sqrt, pi

print(sqrt(36))
print(pi)

# ============================================================
# USING AN ALIAS
# ============================================================

import math as m

print(m.sqrt(49))
print(m.pi)

# ============================================================
# RANDOM MODULE
# ============================================================

import random

print(random.randint(1, 10))
print(random.choice(["Apple", "Banana", "Mango"]))

# ============================================================
# DATETIME MODULE
# ============================================================

import datetime

current_date = datetime.datetime.now()

print(current_date)

# ============================================================
# OS MODULE
# ============================================================

import os

print(os.getcwd())  # Current working directory

# ============================================================
# CREATING YOUR OWN MODULE
# ============================================================

# File: mymodule.py

# def greet(name):
#     return f"Hello {name}"

# ------------------------------------------------------------
# File: main.py
# ------------------------------------------------------------

# import mymodule

# print(mymodule.greet("Gaurav"))

# ============================================================
# IMPORTING SPECIFIC FUNCTION FROM CUSTOM MODULE
# ============================================================

# File: mymodule.py

# def add(a, b):
#     return a + b

# ------------------------------------------------------------
# File: main.py
# ------------------------------------------------------------

# from mymodule import add

# print(add(10, 20))

# ============================================================
# MODULE INFORMATION
# ============================================================

import math

print(math.__name__)

# ============================================================
# PRACTICAL EXAMPLES
# ============================================================

# Example 1: Calculate Square Root

import math

number = 64

print(math.sqrt(number))

# ------------------------------------------------------------

# Example 2: Generate Random Number

import random

print(random.randint(100, 999))

# ------------------------------------------------------------

# Example 3: Get Today's Date

import datetime

today = datetime.date.today()

print(today)

# ============================================================
# SUMMARY
# ============================================================

print("""
Module Syntax:

import module_name

from module_name import function_name

import module_name as alias

Common Built-in Modules:

math      -> Mathematical operations
random    -> Random values
datetime  -> Date and time
os        -> Operating system functions

Benefits:

✔ Code Reusability
✔ Better Organization
✔ Access to Built-in Libraries
✔ Easier Maintenance
""")
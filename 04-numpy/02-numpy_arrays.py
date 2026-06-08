# ============================================================
# NUMPY ARRAYS IN PYTHON
# ============================================================

# NumPy Arrays are the core data structure of NumPy.
# They are faster and more memory efficient than Python Lists.

# Install NumPy:
# pip install numpy

import numpy as np

# ============================================================
# CREATING NUMPY ARRAYS
# ============================================================

arr = np.array([10, 20, 30, 40, 50])

print(arr)

# ============================================================
# WHY NUMPY ARRAYS?
# ============================================================

# Python List

numbers = [10, 20, 30, 40, 50]

# NumPy Array

arr = np.array([10, 20, 30, 40, 50])

print(type(numbers))
print(type(arr))

# ============================================================
# 1D ARRAY
# ============================================================

arr = np.array([1, 2, 3, 4, 5])

print(arr)

# ============================================================
# 2D ARRAY
# ============================================================

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr)

# ============================================================
# 3D ARRAY
# ============================================================

arr = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print(arr)

# ============================================================
# ARRAY DIMENSIONS
# ============================================================

arr1 = np.array([1, 2, 3])

arr2 = np.array([
    [1, 2],
    [3, 4]
])

arr3 = np.array([
    [
        [1, 2],
        [3, 4]
    ]
])

print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

# ============================================================
# ARRAY SHAPE
# ============================================================

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.shape)

# Output:
# (2, 3)

# ============================================================
# ARRAY SIZE
# ============================================================

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.size)

# Output:
# 6

# ============================================================
# ARRAY DATA TYPE
# ============================================================

arr = np.array([1, 2, 3])

print(arr.dtype)

# ============================================================
# ACCESSING ARRAY ELEMENTS
# ============================================================

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])
print(arr[2])
print(arr[-1])

# ============================================================
# ACCESSING 2D ARRAY ELEMENTS
# ============================================================

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr[0, 0])
print(arr[0, 2])
print(arr[1, 1])

# ============================================================
# ACCESSING 3D ARRAY ELEMENTS
# ============================================================

arr = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print(arr[0, 1, 1])
print(arr[1, 0, 0])

# ============================================================
# ARRAY SLICING
# ============================================================

arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])
print(arr[:3])
print(arr[2:])
print(arr[::-1])

# ============================================================
# 2D ARRAY SLICING
# ============================================================

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(arr[0:2, 1:3])

# ============================================================
# MODIFYING ARRAY ELEMENTS
# ============================================================

arr = np.array([10, 20, 30])

arr[1] = 100

print(arr)

# ============================================================
# MODIFYING MULTIPLE VALUES
# ============================================================

arr = np.array([10, 20, 30, 40, 50])

arr[1:4] = [100, 200, 300]

print(arr)

# ============================================================
# ARRAY ATTRIBUTES
# ============================================================

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Dimensions :", arr.ndim)
print("Shape      :", arr.shape)
print("Size       :", arr.size)
print("Datatype   :", arr.dtype)

# ============================================================
# CREATING ARRAYS WITH DIFFERENT DATA TYPES
# ============================================================

int_array = np.array([1, 2, 3])

float_array = np.array([1.1, 2.2, 3.3])

string_array = np.array(["Python", "NumPy"])

print(int_array.dtype)
print(float_array.dtype)
print(string_array.dtype)

# ============================================================
# CONVERTING DATA TYPES
# ============================================================

arr = np.array([1.1, 2.2, 3.3])

new_arr = arr.astype(int)

print(new_arr)

# ============================================================
# COPYING ARRAYS
# ============================================================

arr1 = np.array([1, 2, 3])

arr2 = arr1.copy()

arr2[0] = 100

print(arr1)
print(arr2)

# ============================================================
# VIEW ARRAYS
# ============================================================

arr1 = np.array([1, 2, 3])

arr2 = arr1.view()

arr2[0] = 100

print(arr1)
print(arr2)

# ============================================================
# ITERATING THROUGH ARRAYS
# ============================================================

arr = np.array([10, 20, 30])

for value in arr:
    print(value)

# ============================================================
# ITERATING THROUGH 2D ARRAYS
# ============================================================

arr = np.array([
    [1, 2],
    [3, 4]
])

for row in arr:
    print(row)

# ============================================================
# ITERATING THROUGH EACH ELEMENT
# ============================================================

arr = np.array([
    [1, 2],
    [3, 4]
])

for value in np.nditer(arr):
    print(value)

# ============================================================
# CHECKING ARRAY DIMENSIONS
# ============================================================

arr = np.array([1, 2, 3])

print(arr.ndim)

# ============================================================
# PRACTICAL EXAMPLE 1
# STUDENT MARKS
# ============================================================

marks = np.array([85, 90, 78, 92, 88])

print("Marks :", marks)

print("First Student :", marks[0])

print("Last Student :", marks[-1])

# ============================================================
# PRACTICAL EXAMPLE 2
# SALES MATRIX
# ============================================================

sales = np.array([
    [1000, 1200, 1500],
    [900, 1400, 1600]
])

print(sales)

print("January Sales :", sales[:, 0])

# ============================================================
# PRACTICAL EXAMPLE 3
# TEMPERATURE DATA
# ============================================================

temperature = np.array([30, 32, 35, 31, 29])

print("Temperatures :", temperature)

temperature[2] = 36

print("Updated :", temperature)

# ============================================================
# SUMMARY
# ============================================================

print("""
NUMPY ARRAYS SUMMARY

Array Creation:

np.array()

Array Types:

1D Array
2D Array
3D Array

Important Attributes:

ndim    -> Number of Dimensions
shape   -> Array Shape
size    -> Total Elements
dtype   -> Data Type

Array Operations:

Indexing
Slicing
Modification
Iteration

Useful Methods:

copy()
view()
astype()

Benefits:

✔ Faster than Lists
✔ Less Memory Usage
✔ Easy Data Manipulation
✔ Essential for Data Science
✔ Supports Multi-Dimensional Data
""")
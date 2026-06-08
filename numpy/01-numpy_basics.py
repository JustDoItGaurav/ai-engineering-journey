# ============================================================
# NUMPY BASICS IN PYTHON
# ============================================================

# NumPy (Numerical Python) is a powerful library used for:
# ✔ Fast numerical computations
# ✔ Working with arrays and matrices
# ✔ Mathematical operations
# ✔ Data Science & Machine Learning

# Install NumPy:
# pip install numpy

import numpy as np

# ============================================================
# CREATING NUMPY ARRAYS
# ============================================================

# Python List
numbers = [1, 2, 3, 4, 5]

# Convert List to NumPy Array
arr = np.array(numbers)

print(arr)
print(type(arr))

# ============================================================
# CREATING 1D ARRAY
# ============================================================

arr = np.array([10, 20, 30, 40, 50])

print(arr)

# ============================================================
# CREATING 2D ARRAY
# ============================================================

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
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

print(arr1.ndim)   # 1 Dimension
print(arr2.ndim)   # 2 Dimensions

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
# 2 rows and 3 columns

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
# CREATING SPECIAL ARRAYS
# ============================================================

# Array of Zeros

zeros = np.zeros((2, 3))

print(zeros)

# Array of Ones

ones = np.ones((3, 3))

print(ones)

# Identity Matrix

identity = np.eye(3)

print(identity)

# ============================================================
# USING arange()
# ============================================================

arr = np.arange(1, 11)

print(arr)

# Start, Stop, Step

arr = np.arange(0, 20, 2)

print(arr)

# ============================================================
# USING linspace()
# ============================================================

arr = np.linspace(0, 10, 5)

print(arr)

# Output:
# 5 equally spaced values between 0 and 10

# ============================================================
# RANDOM ARRAYS
# ============================================================

# Random values between 0 and 1

arr = np.random.rand(3)

print(arr)

# Random Integer Values

arr = np.random.randint(1, 100, 5)

print(arr)

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

print(arr[0, 1])
print(arr[1, 2])

# ============================================================
# ARRAY SLICING
# ============================================================

arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])
print(arr[:3])
print(arr[2:])

# ============================================================
# MODIFYING ARRAY ELEMENTS
# ============================================================

arr = np.array([10, 20, 30])

arr[1] = 100

print(arr)

# ============================================================
# ARRAY MATHEMATICAL OPERATIONS
# ============================================================

arr = np.array([1, 2, 3, 4])

print(arr + 10)
print(arr - 1)
print(arr * 2)
print(arr / 2)

# ============================================================
# ARRAY TO ARRAY OPERATIONS
# ============================================================

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)

# ============================================================
# COMMON NUMPY FUNCTIONS
# ============================================================

arr = np.array([10, 20, 30, 40, 50])

print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))
print(np.std(arr))

# ============================================================
# RESHAPING ARRAYS
# ============================================================

arr = np.array([1, 2, 3, 4, 5, 6])

new_arr = arr.reshape(2, 3)

print(new_arr)

# ============================================================
# FLATTENING ARRAYS
# ============================================================

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

flat = arr.flatten()

print(flat)

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
# COPYING ARRAYS
# ============================================================

arr1 = np.array([1, 2, 3])

arr2 = arr1.copy()

arr2[0] = 100

print(arr1)
print(arr2)

# ============================================================
# VIEW OF ARRAY
# ============================================================

arr1 = np.array([1, 2, 3])

arr2 = arr1.view()

arr2[0] = 100

print(arr1)
print(arr2)

# ============================================================
# FILTERING ARRAYS
# ============================================================

arr = np.array([10, 20, 30, 40, 50])

result = arr[arr > 25]

print(result)

# ============================================================
# SORTING ARRAYS
# ============================================================

arr = np.array([50, 10, 40, 20, 30])

sorted_arr = np.sort(arr)

print(sorted_arr)

# ============================================================
# PRACTICAL EXAMPLE 1
# STUDENT MARKS ANALYSIS
# ============================================================

marks = np.array([80, 75, 90, 95, 85])

print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))

# ============================================================
# PRACTICAL EXAMPLE 2
# SALES DATA
# ============================================================

sales = np.array([1000, 1200, 900, 1500, 2000])

print("Total Sales:", np.sum(sales))
print("Average Sales:", np.mean(sales))

# ============================================================
# PRACTICAL EXAMPLE 3
# MATRIX OPERATIONS
# ============================================================

matrix1 = np.array([
    [1, 2],
    [3, 4]
])

matrix2 = np.array([
    [5, 6],
    [7, 8]
])

print(matrix1 + matrix2)

# Matrix Multiplication

print(matrix1 @ matrix2)

# ============================================================
# SUMMARY
# ============================================================

print("""
NUMPY BASICS SUMMARY

Important Concepts:

np.array()     -> Create Array
ndim           -> Number of Dimensions
shape          -> Array Shape
size           -> Total Elements
dtype          -> Data Type

Special Arrays:

np.zeros()     -> Array of Zeros
np.ones()      -> Array of Ones
np.eye()       -> Identity Matrix

Range Functions:

np.arange()    -> Range of Values
np.linspace()  -> Equal Spacing Values

Math Functions:

np.sum()
np.mean()
np.max()
np.min()
np.std()

Array Operations:

+  Addition
-  Subtraction
*  Multiplication
/  Division

Useful Methods:

reshape()
flatten()
copy()
view()
sort()

Benefits of NumPy:

✔ Faster than Python Lists
✔ Less Memory Usage
✔ Powerful Mathematical Functions
✔ Easy Matrix Operations
✔ Essential for Data Science & Machine Learning
""")
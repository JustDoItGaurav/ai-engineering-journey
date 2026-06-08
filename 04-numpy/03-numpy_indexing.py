# ============================================================
# NUMPY INDEXING IN PYTHON
# ============================================================

# Indexing is used to access specific elements from a NumPy array.
# Index numbers start from 0.

# Install NumPy:
# pip install numpy

import numpy as np

# ============================================================
# 1D ARRAY INDEXING
# ============================================================

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])   # First element
print(arr[1])   # Second element
print(arr[2])   # Third element

# Output:
# 10
# 20
# 30

# ============================================================
# NEGATIVE INDEXING
# ============================================================

arr = np.array([10, 20, 30, 40, 50])

print(arr[-1])  # Last element
print(arr[-2])  # Second last element
print(arr[-3])  # Third last element

# Output:
# 50
# 40
# 30

# ============================================================
# MODIFYING VALUES USING INDEXING
# ============================================================

arr = np.array([10, 20, 30, 40])

print("Before:", arr)

arr[1] = 100

print("After :", arr)

# ============================================================
# 2D ARRAY INDEXING
# ============================================================

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr[0, 0])   # Row 0, Column 0
print(arr[0, 2])   # Row 0, Column 2
print(arr[1, 1])   # Row 1, Column 1

# Output:
# 10
# 30
# 50

# ============================================================
# ACCESSING COMPLETE ROWS
# ============================================================

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(arr[0])   # First Row
print(arr[1])   # Second Row
print(arr[2])   # Third Row

# ============================================================
# ACCESSING COMPLETE COLUMNS
# ============================================================

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(arr[:, 0])   # First Column
print(arr[:, 1])   # Second Column
print(arr[:, 2])   # Third Column

# ============================================================
# 3D ARRAY INDEXING
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

print(arr[0, 0, 0])
print(arr[0, 1, 1])
print(arr[1, 0, 1])
print(arr[1, 1, 0])

# Output:
# 1
# 4
# 6
# 7

# ============================================================
# ACCESSING LAST ELEMENT IN EACH DIMENSION
# ============================================================

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr[-1, -1])

# Output:
# 60

# ============================================================
# MULTIPLE INDEX ACCESS
# ============================================================

arr = np.array([10, 20, 30, 40, 50])

indices = [0, 2, 4]

print(arr[indices])

# Output:
# [10 30 50]

# ============================================================
# BOOLEAN INDEXING
# ============================================================

arr = np.array([10, 20, 30, 40, 50])

print(arr[arr > 25])

# Output:
# [30 40 50]

# ============================================================
# BOOLEAN INDEXING WITH CONDITIONS
# ============================================================

arr = np.array([5, 10, 15, 20, 25, 30])

print(arr[arr >= 20])

# Output:
# [20 25 30]

# ============================================================
# FINDING EVEN NUMBERS
# ============================================================

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

even_numbers = arr[arr % 2 == 0]

print(even_numbers)

# Output:
# [2 4 6 8]

# ============================================================
# FINDING ODD NUMBERS
# ============================================================

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

odd_numbers = arr[arr % 2 != 0]

print(odd_numbers)

# Output:
# [1 3 5 7]

# ============================================================
# CONDITIONAL MODIFICATION
# ============================================================

arr = np.array([10, 20, 30, 40, 50])

arr[arr > 30] = 999

print(arr)

# Output:
# [ 10  20  30 999 999 ]

# ============================================================
# USING np.where()
# ============================================================

arr = np.array([10, 20, 30, 40, 50])

result = np.where(arr > 25)

print(result)

# Output:
# (array([2, 3, 4]),)

# ============================================================
# USING np.where() FOR REPLACEMENT
# ============================================================

arr = np.array([10, 20, 30, 40, 50])

new_arr = np.where(arr > 25, 1, 0)

print(new_arr)

# Output:
# [0 0 1 1 1]

# ============================================================
# PRACTICAL EXAMPLE 1
# STUDENT MARKS
# ============================================================

marks = np.array([75, 88, 92, 67, 95])

print("Topper Marks :", marks[np.argmax(marks)])

print("Students Above 80 :", marks[marks > 80])

# ============================================================
# PRACTICAL EXAMPLE 2
# SALES DATA
# ============================================================

sales = np.array([
    [1000, 1200, 1400],
    [900, 1500, 1700]
])

print("January Sales :", sales[:, 0])

print("Highest Sales :", np.max(sales))

# ============================================================
# PRACTICAL EXAMPLE 3
# TEMPERATURE DATA
# ============================================================

temperature = np.array([28, 30, 35, 40, 25, 38])

hot_days = temperature[temperature > 35]

print("Hot Days :", hot_days)

# ============================================================
# SUMMARY
# ============================================================

print("""
NUMPY INDEXING SUMMARY

1D Indexing:

arr[0]
arr[1]
arr[-1]

2D Indexing:

arr[row, column]

Examples:

arr[0,0]
arr[1,2]

3D Indexing:

arr[layer, row, column]

Special Indexing:

Negative Indexing
Boolean Indexing
Multiple Indexing

Useful Functions:

np.where()
np.argmax()
np.argmin()

Benefits:

✔ Fast Data Access
✔ Easy Filtering
✔ Conditional Selection
✔ Supports Multi-Dimensional Arrays
✔ Essential for Data Analysis
""")
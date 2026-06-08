# ============================================================
# NUMPY RESHAPING IN PYTHON
# ============================================================

# Reshaping means changing the shape (dimensions) of an array
# without changing its data.

# Syntax:
# array.reshape(rows, columns)

import numpy as np

# ============================================================
# WHY RESHAPING?
# ============================================================

# Original Array

arr = np.array([1, 2, 3, 4, 5, 6])

print(arr)

# Shape

print(arr.shape)

# Output:
# (6,)

# ============================================================
# RESHAPE 1D TO 2D
# ============================================================

arr = np.array([1, 2, 3, 4, 5, 6])

new_arr = arr.reshape(2, 3)

print(new_arr)

# Output:
# [[1 2 3]
#  [4 5 6]]

# Shape

print(new_arr.shape)

# Output:
# (2, 3)

# ============================================================
# RESHAPE 1D TO 3D
# ============================================================

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

new_arr = arr.reshape(2, 2, 2)

print(new_arr)

# Shape

print(new_arr.shape)

# Output:
# (2, 2, 2)

# ============================================================
# IMPORTANT RULE
# ============================================================

# Total Elements Must Remain Same

arr = np.array([1, 2, 3, 4, 5, 6])

print(arr.size)

# 2 × 3 = 6 ✔

new_arr = arr.reshape(2, 3)

print(new_arr)

# ============================================================
# INVALID RESHAPE
# ============================================================

arr = np.array([1, 2, 3, 4, 5, 6])

# Uncomment to see error

# arr.reshape(4, 2)

# Because:
# 4 × 2 = 8
# Original size = 6

# ============================================================
# USING -1 IN RESHAPE
# ============================================================

# NumPy automatically calculates the missing dimension

arr = np.array([1, 2, 3, 4, 5, 6])

new_arr = arr.reshape(2, -1)

print(new_arr)

# Output:
# [[1 2 3]
#  [4 5 6]]

# ============================================================
# ANOTHER -1 EXAMPLE
# ============================================================

arr = np.array([1, 2, 3, 4, 5, 6])

new_arr = arr.reshape(3, -1)

print(new_arr)

# Output:
# [[1 2]
#  [3 4]
#  [5 6]]

# ============================================================
# RESHAPE TO SINGLE ROW
# ============================================================

arr = np.array([1, 2, 3, 4, 5, 6])

new_arr = arr.reshape(1, 6)

print(new_arr)

# Output:
# [[1 2 3 4 5 6]]

# ============================================================
# RESHAPE TO SINGLE COLUMN
# ============================================================

arr = np.array([1, 2, 3, 4, 5, 6])

new_arr = arr.reshape(6, 1)

print(new_arr)

# Output:
# [[1]
#  [2]
#  [3]
#  [4]
#  [5]
#  [6]]

# ============================================================
# FLATTENING ARRAY
# ============================================================

# Convert Multi-Dimensional Array into 1D Array

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

flat = arr.reshape(-1)

print(flat)

# Output:
# [1 2 3 4 5 6]

# ============================================================
# USING flatten()
# ============================================================

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

flat = arr.flatten()

print(flat)

# ============================================================
# USING ravel()
# ============================================================

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

flat = arr.ravel()

print(flat)

# ============================================================
# DIFFERENCE BETWEEN flatten() AND ravel()
# ============================================================

arr = np.array([
    [1, 2],
    [3, 4]
])

flat1 = arr.flatten()   # Copy

flat2 = arr.ravel()     # View

flat2[0] = 100

print(arr)

# Original array changes when using ravel()

# ============================================================
# CHECKING SHAPE BEFORE AND AFTER
# ============================================================

arr = np.array([1, 2, 3, 4, 5, 6])

print("Original Shape:", arr.shape)

new_arr = arr.reshape(2, 3)

print("New Shape:", new_arr.shape)

# ============================================================
# PRACTICAL EXAMPLE 1
# STUDENT MARKS
# ============================================================

marks = np.array([80, 75, 90, 95, 85, 70])

marks_table = marks.reshape(2, 3)

print(marks_table)

# Output:
# [[80 75 90]
#  [95 85 70]]

# ============================================================
# PRACTICAL EXAMPLE 2
# SALES DATA
# ============================================================

sales = np.array([
    1000, 1200, 1500,
    900, 1400, 1700
])

sales_matrix = sales.reshape(2, 3)

print(sales_matrix)

# ============================================================
# PRACTICAL EXAMPLE 3
# IMAGE PIXELS
# ============================================================

pixels = np.arange(16)

image = pixels.reshape(4, 4)

print(image)

# Output:
# 4x4 Image Matrix

# ============================================================
# COMMON RESHAPING PATTERNS
# ============================================================

arr = np.arange(12)

print(arr.reshape(3, 4))

print(arr.reshape(4, 3))

print(arr.reshape(2, 2, 3))

# ============================================================
# SUMMARY
# ============================================================

print("""
NUMPY RESHAPING SUMMARY

Purpose:
Change the shape of an array without changing data.

Syntax:

arr.reshape(rows, columns)

Important Rule:

Total Elements Must Remain Same

Examples:

6 Elements

reshape(2,3) ✔
reshape(3,2) ✔
reshape(1,6) ✔
reshape(6,1) ✔
reshape(4,2) ✘

Using -1:

reshape(2,-1)
reshape(3,-1)

Flattening:

reshape(-1)
flatten()
ravel()

Useful Attributes:

shape
size
ndim

Benefits:

✔ Organize Data
✔ Prepare Data for ML
✔ Convert Between Dimensions
✔ Easy Matrix Creation
✔ Essential for Data Science
""")
# ============================================================
# NUMPY BROADCASTING IN PYTHON
# ============================================================

# Broadcasting allows NumPy to perform operations on arrays
# of different shapes without explicitly reshaping them.

# It automatically expands smaller arrays to match larger arrays.

import numpy as np

# ============================================================
# WHAT IS BROADCASTING?
# ============================================================

arr = np.array([10, 20, 30, 40])

result = arr + 5

print(result)

# Output:
# [15 25 35 45]

# Here, NumPy broadcasts the value 5 to:
# [5 5 5 5]

# ============================================================
# BROADCASTING WITH SCALARS
# ============================================================

arr = np.array([1, 2, 3, 4])

print(arr + 10)
print(arr - 1)
print(arr * 2)
print(arr / 2)

# ============================================================
# ARRAY + ARRAY (SAME SHAPE)
# ============================================================

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

print(arr1 + arr2)

# Output:
# [5 7 9]

# ============================================================
# BROADCASTING 1D ARRAY TO 2D ARRAY
# ============================================================

arr1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

arr2 = np.array([10, 20, 30])

result = arr1 + arr2

print(result)

# Output:
# [[11 22 33]
#  [14 25 36]]

# NumPy treats arr2 as:
#
# [[10 20 30]
#  [10 20 30]]

# ============================================================
# ANOTHER BROADCASTING EXAMPLE
# ============================================================

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matrix * 10)

# Output:
# [[10 20 30]
#  [40 50 60]]

# ============================================================
# COLUMN-WISE BROADCASTING
# ============================================================

arr1 = np.array([
    [1],
    [2],
    [3]
])

arr2 = np.array([10, 20, 30])

result = arr1 + arr2

print(result)

# Output:
# [[11 21 31]
#  [12 22 32]
#  [13 23 33]]

# Shapes:
# arr1 = (3,1)
# arr2 = (3,)
#
# Result = (3,3)

# ============================================================
# BROADCASTING RULES
# ============================================================

# Rule 1:
# Dimensions are compared from right to left.

# Rule 2:
# Dimensions are compatible if:
#
# They are equal
# OR
# One of them is 1

# ============================================================
# VALID BROADCASTING
# ============================================================

# Shape (2,3)

arr1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Shape (3,)

arr2 = np.array([10, 20, 30])

print(arr1 + arr2)

# Compatible:
#
# (2,3)
# (  3)

# ============================================================
# INVALID BROADCASTING
# ============================================================

arr1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

arr2 = np.array([10, 20])

# Uncomment to see error

# print(arr1 + arr2)

# Shapes:
#
# (2,3)
# (2,)
#
# Not compatible

# ============================================================
# USING np.newaxis
# ============================================================

arr = np.array([1, 2, 3])

column = arr[:, np.newaxis]

print(column)

# Output:
# [[1]
#  [2]
#  [3]]

print(column.shape)

# Output:
# (3,1)

# ============================================================
# BROADCASTING USING np.newaxis
# ============================================================

row = np.array([10, 20, 30])

column = np.array([1, 2, 3])[:, np.newaxis]

result = row + column

print(result)

# Output:
# [[11 21 31]
#  [12 22 32]
#  [13 23 33]]

# ============================================================
# PRACTICAL EXAMPLE 1
# STUDENT BONUS MARKS
# ============================================================

marks = np.array([70, 80, 90, 85])

bonus_marks = marks + 5

print(bonus_marks)

# Output:
# [75 85 95 90]

# ============================================================
# PRACTICAL EXAMPLE 2
# MONTHLY SALES INCREASE
# ============================================================

sales = np.array([
    [1000, 1200, 1500],
    [900, 1400, 1700]
])

increase = np.array([100, 100, 100])

updated_sales = sales + increase

print(updated_sales)

# Output:
# [[1100 1300 1600]
#  [1000 1500 1800]]

# ============================================================
# PRACTICAL EXAMPLE 3
# TEMPERATURE ADJUSTMENT
# ============================================================

temperature = np.array([28, 30, 32, 35])

adjusted = temperature + 2

print(adjusted)

# Output:
# [30 32 34 37]

# ============================================================
# SHAPE COMPARISON EXAMPLES
# ============================================================

# Valid

# (3,4)
# (4,)

# Valid

# (5,1)
# (5,)

# Valid

# (3,1)
# (1,4)

# Result -> (3,4)

# Invalid

# (3,4)
# (2,)

# ============================================================
# SUMMARY
# ============================================================

print("""
NUMPY BROADCASTING SUMMARY

Definition:
Automatically expands smaller arrays
to perform operations with larger arrays.

Examples:

arr + 5

[1 2 3] + 5

Result:
[6 7 8]

Broadcasting Rules:

1. Compare dimensions from right to left.

2. Dimensions are compatible if:
   - Equal
   - One dimension is 1

Valid Shapes:

(2,3) + (3,)
(3,1) + (3,)
(3,1) + (1,3)

Invalid Shapes:

(2,3) + (2,)

Useful Tool:

np.newaxis

Benefits:

✔ Less Code
✔ Faster Computations
✔ No Manual Loops
✔ Efficient Memory Usage
✔ Essential for Data Science & ML
""")
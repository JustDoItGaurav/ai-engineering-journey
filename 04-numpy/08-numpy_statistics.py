# ============================================================
# NUMPY STATISTICS IN PYTHON
# ============================================================

# NumPy provides many statistical functions to analyze data.
#
# Statistics help us understand:
# ✔ Average Value
# ✔ Highest Value
# ✔ Lowest Value
# ✔ Spread of Data
# ✔ Variability of Data

import numpy as np

# ============================================================
# SAMPLE DATA
# ============================================================

marks = np.array([80, 75, 90, 95, 85])

print(marks)

# ============================================================
# MEAN (AVERAGE)
# ============================================================

marks = np.array([80, 75, 90, 95, 85])

print(np.mean(marks))

# Output:
# 85.0

# Formula:
# Sum of values / Number of values

# ============================================================
# MEDIAN
# ============================================================

marks = np.array([80, 75, 90, 95, 85])

print(np.median(marks))

# Output:
# 85.0

# Median = Middle value after sorting

# ============================================================
# MODE
# ============================================================

# NumPy does not provide a direct mode function.
# Use SciPy for mode calculation.

from scipy import stats

marks = np.array([80, 85, 85, 90, 95])

print(stats.mode(marks))

# ============================================================
# MAXIMUM VALUE
# ============================================================

marks = np.array([80, 75, 90, 95, 85])

print(np.max(marks))

# Output:
# 95

# ============================================================
# MINIMUM VALUE
# ============================================================

marks = np.array([80, 75, 90, 95, 85])

print(np.min(marks))

# Output:
# 75

# ============================================================
# RANGE
# ============================================================

marks = np.array([80, 75, 90, 95, 85])

range_value = np.max(marks) - np.min(marks)

print(range_value)

# Output:
# 20

# ============================================================
# STANDARD DEVIATION
# ============================================================

marks = np.array([80, 75, 90, 95, 85])

print(np.std(marks))

# Measures spread of data

# ============================================================
# VARIANCE
# ============================================================

marks = np.array([80, 75, 90, 95, 85])

print(np.var(marks))

# Variance = Standard Deviation²

# ============================================================
# PERCENTILES
# ============================================================

marks = np.array([80, 75, 90, 95, 85])

print(np.percentile(marks, 25))

# 25th Percentile

print(np.percentile(marks, 50))

# 50th Percentile (Median)

print(np.percentile(marks, 75))

# 75th Percentile

# ============================================================
# QUARTILES
# ============================================================

marks = np.array([80, 75, 90, 95, 85])

Q1 = np.percentile(marks, 25)
Q2 = np.percentile(marks, 50)
Q3 = np.percentile(marks, 75)

print("Q1 =", Q1)
print("Q2 =", Q2)
print("Q3 =", Q3)

# ============================================================
# SUM
# ============================================================

marks = np.array([80, 75, 90, 95, 85])

print(np.sum(marks))

# Output:
# 425

# ============================================================
# PRODUCT
# ============================================================

arr = np.array([1, 2, 3, 4])

print(np.prod(arr))

# Output:
# 24

# ============================================================
# CUMULATIVE SUM
# ============================================================

arr = np.array([10, 20, 30, 40])

print(np.cumsum(arr))

# Output:
# [10 30 60 100]

# ============================================================
# CUMULATIVE PRODUCT
# ============================================================

arr = np.array([1, 2, 3, 4])

print(np.cumprod(arr))

# Output:
# [ 1  2  6 24 ]

# ============================================================
# INDEX OF MAXIMUM VALUE
# ============================================================

marks = np.array([80, 75, 90, 95, 85])

print(np.argmax(marks))

# Output:
# 3

# ============================================================
# INDEX OF MINIMUM VALUE
# ============================================================

marks = np.array([80, 75, 90, 95, 85])

print(np.argmin(marks))

# Output:
# 1

# ============================================================
# STATISTICS ON 2D ARRAYS
# ============================================================

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))

# ============================================================
# ROW-WISE MEAN
# ============================================================

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(np.mean(arr, axis=1))

# Output:
# [20. 50.]

# ============================================================
# COLUMN-WISE MEAN
# ============================================================

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(np.mean(arr, axis=0))

# Output:
# [25. 35. 45.]

# ============================================================
# ROW-WISE SUM
# ============================================================

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(np.sum(arr, axis=1))

# Output:
# [ 60 150 ]

# ============================================================
# COLUMN-WISE SUM
# ============================================================

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(np.sum(arr, axis=0))

# Output:
# [50 70 90]

# ============================================================
# PRACTICAL EXAMPLE 1
# STUDENT MARKS ANALYSIS
# ============================================================

marks = np.array([80, 75, 90, 95, 85])

print("Average Marks :", np.mean(marks))
print("Highest Marks :", np.max(marks))
print("Lowest Marks  :", np.min(marks))
print("Std Dev       :", np.std(marks))

# ============================================================
# PRACTICAL EXAMPLE 2
# MONTHLY SALES
# ============================================================

sales = np.array([
    1000, 1200, 1500,
    1800, 2000, 2200
])

print("Total Sales :", np.sum(sales))
print("Average Sales :", np.mean(sales))
print("Maximum Sales :", np.max(sales))

# ============================================================
# PRACTICAL EXAMPLE 3
# TEMPERATURE ANALYSIS
# ============================================================

temperature = np.array([
    30, 32, 35, 31, 29, 28, 34
])

print("Average Temp :", np.mean(temperature))
print("Highest Temp :", np.max(temperature))
print("Lowest Temp  :", np.min(temperature))

# ============================================================
# SUMMARY
# ============================================================

print("""
NUMPY STATISTICS SUMMARY

Central Tendency:

np.mean()      -> Average
np.median()    -> Middle Value
stats.mode()   -> Most Frequent Value

Spread Measures:

np.std()       -> Standard Deviation
np.var()       -> Variance
Range          -> Max - Min

Percentiles:

np.percentile(arr, 25)
np.percentile(arr, 50)
np.percentile(arr, 75)

Aggregate Functions:

np.sum()
np.prod()
np.max()
np.min()

Index Functions:

np.argmax()
np.argmin()

Cumulative Functions:

np.cumsum()
np.cumprod()

Axis Operations:

axis=0 -> Column-wise
axis=1 -> Row-wise

Benefits:

✔ Quick Data Analysis
✔ Data Distribution Understanding
✔ Machine Learning Preparation
✔ Statistical Insights
✔ Efficient Computations
""")
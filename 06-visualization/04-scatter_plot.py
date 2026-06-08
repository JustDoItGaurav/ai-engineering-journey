# ============================================================
# SCATTER PLOT IN MATPLOTLIB
# ============================================================

# A Scatter Plot is used to show the relationship between
# two numerical variables.
#
# Examples:
# ✔ Height vs Weight
# ✔ Age vs Salary
# ✔ Study Hours vs Marks
# ✔ Advertising vs Sales

# Install:
# pip install matplotlib

import matplotlib.pyplot as plt

# ============================================================
# SIMPLE SCATTER PLOT
# ============================================================

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.scatter(x, y)

plt.show()

# ============================================================
# ADDING TITLE
# ============================================================

plt.scatter(x, y)

plt.title("Simple Scatter Plot")

plt.show()

# ============================================================
# ADDING AXIS LABELS
# ============================================================

plt.scatter(x, y)

plt.title("Scatter Plot Example")

plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()

# ============================================================
# CHANGING POINT COLOR
# ============================================================

plt.scatter(
    x,
    y,
    color="red"
)

plt.show()

# ============================================================
# CHANGING POINT SIZE
# ============================================================

plt.scatter(
    x,
    y,
    s=200
)

plt.show()

# ============================================================
# CHANGING MARKER STYLE
# ============================================================

plt.scatter(
    x,
    y,
    marker="*"
)

plt.show()

# Available Markers:
#
# o  Circle
# s  Square
# ^  Triangle
# *  Star
# +  Plus

# ============================================================
# ADDING TRANSPARENCY
# ============================================================

plt.scatter(
    x,
    y,
    alpha=0.5
)

plt.show()

# ============================================================
# ADDING GRID
# ============================================================

plt.scatter(x, y)

plt.grid(True)

plt.show()

# ============================================================
# MULTIPLE SCATTER PLOTS
# ============================================================

x1 = [1, 2, 3, 4]
y1 = [10, 20, 30, 40]

x2 = [1, 2, 3, 4]
y2 = [40, 30, 20, 10]

plt.scatter(
    x1,
    y1,
    label="Group A"
)

plt.scatter(
    x2,
    y2,
    label="Group B"
)

plt.legend()

plt.show()

# ============================================================
# FIGURE SIZE
# ============================================================

plt.figure(figsize=(8, 4))

plt.scatter(x, y)

plt.show()

# ============================================================
# USING NUMPY DATA
# ============================================================

import numpy as np

x = np.array([1, 2, 3, 4, 5])

y = np.array([10, 20, 15, 30, 25])

plt.scatter(x, y)

plt.show()

# ============================================================
# PRACTICAL EXAMPLE 1
# STUDY HOURS VS MARKS
# ============================================================

hours = [1, 2, 3, 4, 5, 6]

marks = [40, 50, 60, 70, 80, 90]

plt.scatter(hours, marks)

plt.title("Study Hours vs Marks")

plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.grid(True)

plt.show()

# ============================================================
# PRACTICAL EXAMPLE 2
# HEIGHT VS WEIGHT
# ============================================================

height = [150, 160, 170, 180, 190]

weight = [50, 60, 70, 80, 90]

plt.scatter(height, weight)

plt.title("Height vs Weight")

plt.xlabel("Height")
plt.ylabel("Weight")

plt.show()

# ============================================================
# PRACTICAL EXAMPLE 3
# AGE VS SALARY
# ============================================================

age = [22, 25, 28, 32, 35]

salary = [
    25000,
    35000,
    45000,
    60000,
    75000
]

plt.scatter(age, salary)

plt.title("Age vs Salary")

plt.xlabel("Age")
plt.ylabel("Salary")

plt.show()

# ============================================================
# MOST COMMON SCATTER PLOT STRUCTURE
# ============================================================

x = [10, 20, 30, 40, 50]

y = [15, 25, 35, 45, 55]

plt.scatter(
    x,
    y,
    s=100
)

plt.title("Scatter Plot")

plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.grid(True)

plt.show()

# ============================================================
# SUMMARY
# ============================================================

print("""
SCATTER PLOT SUMMARY

Function:

plt.scatter()

Important Parameters:

color=
s=
marker=
alpha=
label=

Useful Functions:

plt.title()
plt.xlabel()
plt.ylabel()
plt.legend()
plt.grid()
plt.show()

Common Markers:

o  Circle
s  Square
^  Triangle
*  Star
+  Plus

Uses:

✔ Correlation Analysis
✔ Height vs Weight
✔ Age vs Salary
✔ Study Hours vs Marks
✔ Advertising vs Sales

Benefits:

✔ Shows Relationships
✔ Detects Trends
✔ Identifies Outliers
✔ Essential for Data Analysis
""")
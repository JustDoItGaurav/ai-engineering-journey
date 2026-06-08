# ============================================================
# LINE PLOT IN MATPLOTLIB
# ============================================================

# A Line Plot is used to show trends or changes over time.
#
# Examples:
# ✔ Monthly Sales
# ✔ Temperature Changes
# ✔ Stock Prices
# ✔ Population Growth

# Install:
# pip install matplotlib

import matplotlib.pyplot as plt

# ============================================================
# SIMPLE LINE PLOT
# ============================================================

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

plt.plot(x, y)

plt.show()

# ============================================================
# ADDING TITLE
# ============================================================

plt.plot(x, y)

plt.title("Simple Line Plot")

plt.show()

# ============================================================
# ADDING AXIS LABELS
# ============================================================

plt.plot(x, y)

plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.title("Line Plot Example")

plt.show()

# ============================================================
# ADDING MARKERS
# ============================================================

plt.plot(
    x,
    y,
    marker="o"
)

plt.show()

# ============================================================
# CHANGING LINE STYLE
# ============================================================

plt.plot(
    x,
    y,
    linestyle="--"
)

plt.show()

# Available Styles:
#
# "-"   Solid
# "--"  Dashed
# ":"   Dotted
# "-."  Dash-Dot

# ============================================================
# CHANGING LINE COLOR
# ============================================================

plt.plot(
    x,
    y,
    color="red"
)

plt.show()

# ============================================================
# CHANGING LINE WIDTH
# ============================================================

plt.plot(
    x,
    y,
    linewidth=3
)

plt.show()

# ============================================================
# COMBINING OPTIONS
# ============================================================

plt.plot(
    x,
    y,
    color="blue",
    marker="o",
    linestyle="--",
    linewidth=2
)

plt.show()

# ============================================================
# MULTIPLE LINE PLOTS
# ============================================================

months = [1, 2, 3, 4, 5]

sales = [100, 200, 300, 400, 500]
expenses = [80, 150, 250, 350, 450]

plt.plot(months, sales)

plt.plot(months, expenses)

plt.show()

# ============================================================
# ADDING LEGEND
# ============================================================

plt.plot(
    months,
    sales,
    label="Sales"
)

plt.plot(
    months,
    expenses,
    label="Expenses"
)

plt.legend()

plt.show()

# ============================================================
# ADDING GRID
# ============================================================

plt.plot(months, sales)

plt.grid(True)

plt.show()

# ============================================================
# FIGURE SIZE
# ============================================================

plt.figure(figsize=(8, 4))

plt.plot(months, sales)

plt.show()

# ============================================================
# USING NUMPY ARRAYS
# ============================================================

import numpy as np

x = np.array([1, 2, 3, 4, 5])

y = np.array([10, 20, 30, 40, 50])

plt.plot(x, y)

plt.show()

# ============================================================
# PRACTICAL EXAMPLE 1
# MONTHLY SALES
# ============================================================

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May"
]

sales = [
    1000,
    1200,
    1500,
    1800,
    2000
]

plt.plot(
    months,
    sales,
    marker="o"
)

plt.title("Monthly Sales Report")

plt.xlabel("Months")
plt.ylabel("Sales")

plt.grid(True)

plt.show()

# ============================================================
# PRACTICAL EXAMPLE 2
# TEMPERATURE CHANGES
# ============================================================

days = [1, 2, 3, 4, 5]

temperature = [
    30,
    32,
    35,
    33,
    31
]

plt.plot(
    days,
    temperature,
    marker="o"
)

plt.title("Temperature Changes")

plt.xlabel("Days")
plt.ylabel("Temperature")

plt.show()

# ============================================================
# PRACTICAL EXAMPLE 3
# STUDENT MARKS PROGRESS
# ============================================================

tests = [
    "Test1",
    "Test2",
    "Test3",
    "Test4"
]

marks = [
    70,
    75,
    85,
    90
]

plt.plot(
    tests,
    marks,
    marker="o"
)

plt.title("Student Progress")

plt.xlabel("Tests")
plt.ylabel("Marks")

plt.show()

# ============================================================
# MOST COMMON LINE PLOT STRUCTURE
# ============================================================

x = [1, 2, 3, 4]
y = [10, 20, 15, 30]

plt.plot(
    x,
    y,
    marker="o"
)

plt.title("Line Plot")

plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.grid(True)

plt.show()

# ============================================================
# SUMMARY
# ============================================================

print("""
LINE PLOT SUMMARY

Function:

plt.plot(x, y)

Important Parameters:

marker=
color=
linestyle=
linewidth=
label=

Useful Functions:

plt.title()
plt.xlabel()
plt.ylabel()
plt.legend()
plt.grid()
plt.show()

Line Styles:

-   Solid
--  Dashed
:   Dotted
-.  Dash-Dot

Uses:

✔ Trends Over Time
✔ Sales Analysis
✔ Temperature Tracking
✔ Stock Prices
✔ Performance Monitoring

Benefits:

✔ Easy Visualization
✔ Trend Detection
✔ Professional Reports
✔ Essential for Data Analysis
""")
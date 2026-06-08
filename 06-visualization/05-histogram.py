# ============================================================
# HISTOGRAM IN MATPLOTLIB
# ============================================================

# A Histogram is used to show the distribution of data.
#
# It groups values into intervals called Bins.
#
# Examples:
# ✔ Student Marks Distribution
# ✔ Age Distribution
# ✔ Salary Distribution
# ✔ Exam Scores

# Install:
# pip install matplotlib

import matplotlib.pyplot as plt

# ============================================================
# SIMPLE HISTOGRAM
# ============================================================

data = [10, 20, 20, 30, 30, 30, 40, 40, 50]

plt.hist(data)

plt.show()

# ============================================================
# ADDING TITLE
# ============================================================

plt.hist(data)

plt.title("Simple Histogram")

plt.show()

# ============================================================
# ADDING AXIS LABELS
# ============================================================

plt.hist(data)

plt.title("Histogram Example")

plt.xlabel("Values")
plt.ylabel("Frequency")

plt.show()

# ============================================================
# CHANGING NUMBER OF BINS
# ============================================================

plt.hist(
    data,
    bins=5
)

plt.show()

# ============================================================
# CHANGING BAR COLOR
# ============================================================

plt.hist(
    data,
    color="green"
)

plt.show()

# ============================================================
# ADDING EDGE COLOR
# ============================================================

plt.hist(
    data,
    edgecolor="black"
)

plt.show()

# ============================================================
# CHANGING TRANSPARENCY
# ============================================================

plt.hist(
    data,
    alpha=0.7
)

plt.show()

# ============================================================
# COMBINING OPTIONS
# ============================================================

plt.hist(
    data,
    bins=5,
    color="blue",
    edgecolor="black",
    alpha=0.7
)

plt.show()

# ============================================================
# ADDING GRID
# ============================================================

plt.hist(data)

plt.grid(True)

plt.show()

# ============================================================
# FIGURE SIZE
# ============================================================

plt.figure(figsize=(8, 4))

plt.hist(data)

plt.show()

# ============================================================
# USING NUMPY RANDOM DATA
# ============================================================

import numpy as np

data = np.random.normal(
    50,
    10,
    1000
)

plt.hist(data)

plt.show()

# ============================================================
# HISTOGRAM WITH DENSITY
# ============================================================

data = np.random.normal(
    50,
    10,
    1000
)

plt.hist(
    data,
    density=True
)

plt.show()

# ============================================================
# MULTIPLE HISTOGRAMS
# ============================================================

data1 = np.random.normal(
    50,
    10,
    500
)

data2 = np.random.normal(
    60,
    10,
    500
)

plt.hist(
    data1,
    alpha=0.5,
    label="Group A"
)

plt.hist(
    data2,
    alpha=0.5,
    label="Group B"
)

plt.legend()

plt.show()

# ============================================================
# PRACTICAL EXAMPLE 1
# STUDENT MARKS
# ============================================================

marks = [
    50, 60, 70, 80, 90,
    85, 75, 65, 95, 55
]

plt.hist(
    marks,
    bins=5,
    edgecolor="black"
)

plt.title("Marks Distribution")

plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()

# ============================================================
# PRACTICAL EXAMPLE 2
# AGE DISTRIBUTION
# ============================================================

ages = [
    18, 19, 20, 21, 22,
    23, 24, 25, 20, 22
]

plt.hist(
    ages,
    bins=4,
    edgecolor="black"
)

plt.title("Age Distribution")

plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()

# ============================================================
# PRACTICAL EXAMPLE 3
# EMPLOYEE SALARIES
# ============================================================

salary = [
    25000, 30000, 35000,
    40000, 45000, 50000,
    55000, 60000
]

plt.hist(
    salary,
    bins=5,
    edgecolor="black"
)

plt.title("Salary Distribution")

plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.show()

# ============================================================
# MOST COMMON HISTOGRAM STRUCTURE
# ============================================================

data = [10, 15, 20, 25, 30, 35, 40]

plt.hist(
    data,
    bins=5,
    edgecolor="black"
)

plt.title("Histogram")

plt.xlabel("Values")
plt.ylabel("Frequency")

plt.grid(True)

plt.show()

# ============================================================
# SUMMARY
# ============================================================

print("""
HISTOGRAM SUMMARY

Function:

plt.hist()

Important Parameters:

bins=
color=
edgecolor=
alpha=
density=

Useful Functions:

plt.title()
plt.xlabel()
plt.ylabel()
plt.legend()
plt.grid()
plt.show()

Uses:

✔ Data Distribution
✔ Exam Scores
✔ Salary Analysis
✔ Age Distribution
✔ Frequency Analysis

Benefits:

✔ Understand Data Spread
✔ Detect Outliers
✔ Identify Patterns
✔ Essential for Data Analysis
""")
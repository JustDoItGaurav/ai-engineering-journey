# ============================================================
# MATPLOTLIB BASICS IN PYTHON
# ============================================================

# Matplotlib is a Python library used for:
#
# ✔ Data Visualization
# ✔ Creating Graphs
# ✔ Charts
# ✔ Plots
#
# Install:
# pip install matplotlib

import matplotlib.pyplot as plt

# ============================================================
# FIRST PLOT
# ============================================================

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

plt.plot(x, y)

plt.show()

# ============================================================
# ADDING TITLE
# ============================================================

x = [1, 2, 3]
y = [10, 20, 30]

plt.plot(x, y)

plt.title("Simple Line Plot")

plt.show()

# ============================================================
# X AND Y LABELS
# ============================================================

x = [1, 2, 3]
y = [10, 20, 30]

plt.plot(x, y)

plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()

# ============================================================
# LINE STYLE
# ============================================================

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.plot(
    x,
    y,
    linestyle="--"
)

plt.show()

# ============================================================
# LINE WIDTH
# ============================================================

plt.plot(
    x,
    y,
    linewidth=3
)

plt.show()

# ============================================================
# MARKERS
# ============================================================

plt.plot(
    x,
    y,
    marker="o"
)

plt.show()

# ============================================================
# COLOR
# ============================================================

plt.plot(
    x,
    y,
    color="red"
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
# MULTIPLE LINES
# ============================================================

x = [1, 2, 3, 4]

y1 = [10, 20, 30, 40]
y2 = [40, 30, 20, 10]

plt.plot(x, y1)

plt.plot(x, y2)

plt.show()

# ============================================================
# LEGEND
# ============================================================

plt.plot(
    x,
    y1,
    label="Sales"
)

plt.plot(
    x,
    y2,
    label="Expenses"
)

plt.legend()

plt.show()

# ============================================================
# GRID
# ============================================================

plt.plot(x, y1)

plt.grid(True)

plt.show()

# ============================================================
# FIGURE SIZE
# ============================================================

plt.figure(figsize=(8, 4))

plt.plot(x, y1)

plt.show()

# ============================================================
# SCATTER PLOT
# ============================================================

x = [1, 2, 3, 4, 5]
y = [20, 35, 25, 40, 50]

plt.scatter(x, y)

plt.show()

# ============================================================
# BAR CHART
# ============================================================

subjects = ["Math", "Science", "English"]

marks = [90, 85, 95]

plt.bar(subjects, marks)

plt.show()

# ============================================================
# HORIZONTAL BAR CHART
# ============================================================

plt.barh(subjects, marks)

plt.show()

# ============================================================
# HISTOGRAM
# ============================================================

data = [10, 20, 20, 30, 40, 40, 40, 50]

plt.hist(data)

plt.show()

# ============================================================
# PIE CHART
# ============================================================

labels = ["Python", "Java", "C++"]

sizes = [50, 30, 20]

plt.pie(
    sizes,
    labels=labels
)

plt.show()

# ============================================================
# PIE CHART WITH PERCENTAGE
# ============================================================

plt.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%"
)

plt.show()

# ============================================================
# SAVING GRAPH
# ============================================================

plt.plot(x, y1)

plt.savefig("graph.png")

plt.show()

# ============================================================
# USING NUMPY DATA
# ============================================================

import numpy as np

x = np.array([1, 2, 3, 4, 5])

y = np.array([10, 20, 30, 40, 50])

plt.plot(x, y)

plt.show()

# ============================================================
# PRACTICAL EXAMPLE 1
# STUDENT MARKS
# ============================================================

subjects = [
    "Math",
    "Science",
    "English"
]

marks = [90, 85, 95]

plt.bar(subjects, marks)

plt.title("Student Marks")

plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()

# ============================================================
# PRACTICAL EXAMPLE 2
# MONTHLY SALES
# ============================================================

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr"
]

sales = [1000, 1500, 1200, 1800]

plt.plot(
    months,
    sales,
    marker="o"
)

plt.title("Monthly Sales")

plt.show()

# ============================================================
# PRACTICAL EXAMPLE 3
# AGE DISTRIBUTION
# ============================================================

ages = [
    20, 21, 22, 22,
    23, 24, 24, 25
]

plt.hist(ages)

plt.title("Age Distribution")

plt.show()

# ============================================================
# COMMON PLOTS IN DATA SCIENCE
# ============================================================

# Line Plot
# Scatter Plot
# Bar Chart
# Histogram
# Pie Chart

# ============================================================
# SUMMARY
# ============================================================

print("""
MATPLOTLIB SUMMARY

Import:

import matplotlib.pyplot as plt

Line Plot:

plt.plot()

Scatter Plot:

plt.scatter()

Bar Chart:

plt.bar()

Histogram:

plt.hist()

Pie Chart:

plt.pie()

Labels:

plt.title()
plt.xlabel()
plt.ylabel()

Customization:

marker=
color=
linestyle=
linewidth=

Other Functions:

plt.legend()
plt.grid()
plt.figure()

Save Plot:

plt.savefig()

Display Plot:

plt.show()

Benefits:

✔ Data Visualization
✔ Easy Graph Creation
✔ Data Analysis
✔ Reporting
✔ Essential for Data Science
""")
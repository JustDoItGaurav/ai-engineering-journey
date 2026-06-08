# ============================================================
# BAR CHART IN MATPLOTLIB
# ============================================================

# A Bar Chart is used to compare values across categories.
#
# Examples:
# ✔ Student Marks
# ✔ Monthly Sales
# ✔ Product Revenue
# ✔ Population Comparison

# Install:
# pip install matplotlib

import matplotlib.pyplot as plt

# ============================================================
# SIMPLE BAR CHART
# ============================================================

subjects = ["Math", "Science", "English"]

marks = [90, 85, 95]

plt.bar(subjects, marks)

plt.show()

# ============================================================
# ADDING TITLE
# ============================================================

plt.bar(subjects, marks)

plt.title("Student Marks")

plt.show()

# ============================================================
# ADDING AXIS LABELS
# ============================================================

plt.bar(subjects, marks)

plt.title("Student Marks")

plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()

# ============================================================
# CHANGING BAR COLOR
# ============================================================

plt.bar(
    subjects,
    marks,
    color="green"
)

plt.show()

# ============================================================
# CHANGING BAR WIDTH
# ============================================================

plt.bar(
    subjects,
    marks,
    width=0.5
)

plt.show()

# ============================================================
# ADDING EDGE COLOR
# ============================================================

plt.bar(
    subjects,
    marks,
    edgecolor="black"
)

plt.show()

# ============================================================
# MULTIPLE COLORS
# ============================================================

colors = [
    "red",
    "blue",
    "green"
]

plt.bar(
    subjects,
    marks,
    color=colors
)

plt.show()

# ============================================================
# ADDING GRID
# ============================================================

plt.bar(subjects, marks)

plt.grid(True)

plt.show()

# ============================================================
# HORIZONTAL BAR CHART
# ============================================================

plt.barh(
    subjects,
    marks
)

plt.show()

# ============================================================
# MULTIPLE BAR CHART
# ============================================================

subjects = [
    "Math",
    "Science",
    "English"
]

boys_marks = [90, 85, 95]
girls_marks = [88, 92, 96]

x = range(len(subjects))

plt.bar(
    x,
    boys_marks,
    label="Boys"
)

plt.bar(
    x,
    girls_marks,
    label="Girls",
    alpha=0.5
)

plt.xticks(x, subjects)

plt.legend()

plt.show()

# ============================================================
# BAR CHART WITH VALUES
# ============================================================

subjects = ["Math", "Science", "English"]
marks = [90, 85, 95]

bars = plt.bar(subjects, marks)

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height(),
        str(bar.get_height()),
        ha="center"
    )

plt.show()

# ============================================================
# FIGURE SIZE
# ============================================================

plt.figure(figsize=(8, 4))

plt.bar(subjects, marks)

plt.show()

# ============================================================
# PRACTICAL EXAMPLE 1
# STUDENT MARKS
# ============================================================

subjects = [
    "Math",
    "Science",
    "English",
    "Computer"
]

marks = [
    90,
    85,
    95,
    98
]

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

sales = [
    1000,
    1500,
    1200,
    1800
]

plt.bar(months, sales)

plt.title("Monthly Sales")

plt.xlabel("Months")
plt.ylabel("Sales")

plt.show()

# ============================================================
# PRACTICAL EXAMPLE 3
# PRODUCT REVENUE
# ============================================================

products = [
    "Laptop",
    "Phone",
    "Tablet"
]

revenue = [
    50000,
    40000,
    30000
]

plt.bar(products, revenue)

plt.title("Product Revenue")

plt.xlabel("Products")
plt.ylabel("Revenue")

plt.show()

# ============================================================
# MOST COMMON BAR CHART STRUCTURE
# ============================================================

categories = [
    "A",
    "B",
    "C"
]

values = [
    10,
    20,
    30
]

plt.bar(
    categories,
    values
)

plt.title("Bar Chart")

plt.xlabel("Categories")
plt.ylabel("Values")

plt.show()

# ============================================================
# SUMMARY
# ============================================================

print("""
BAR CHART SUMMARY

Function:

plt.bar()

Horizontal Bar:

plt.barh()

Important Parameters:

color=
width=
edgecolor=
label=

Useful Functions:

plt.title()
plt.xlabel()
plt.ylabel()
plt.legend()
plt.grid()
plt.show()

Uses:

✔ Compare Categories
✔ Student Marks
✔ Sales Analysis
✔ Product Revenue
✔ Population Comparison

Benefits:

✔ Easy Comparison
✔ Clear Visualization
✔ Professional Reports
✔ Essential for Data Analysis
""")
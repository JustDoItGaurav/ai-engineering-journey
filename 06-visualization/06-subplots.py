# ============================================================
# SUBPLOTS IN MATPLOTLIB
# ============================================================

# Subplots allow multiple plots in a single figure.
#
# Benefits:
# ✔ Compare Multiple Graphs
# ✔ Better Visualization
# ✔ Dashboard Creation
# ✔ Data Analysis Reports

# Install:
# pip install matplotlib

import matplotlib.pyplot as plt

# ============================================================
# BASIC SUBPLOT
# ============================================================

# Syntax:
#
# plt.subplot(rows, columns, position)

plt.subplot(1, 2, 1)

plt.plot([1, 2, 3], [10, 20, 30])

plt.subplot(1, 2, 2)

plt.plot([1, 2, 3], [30, 20, 10])

plt.show()

# ============================================================
# UNDERSTANDING SUBPLOT PARAMETERS
# ============================================================

# subplot(2, 2, 1)
#
# 2 Rows
# 2 Columns
# Plot Position 1

plt.subplot(2, 2, 1)
plt.plot([1, 2, 3], [10, 20, 30])

plt.subplot(2, 2, 2)
plt.plot([1, 2, 3], [30, 20, 10])

plt.subplot(2, 2, 3)
plt.plot([1, 2, 3], [15, 25, 35])

plt.subplot(2, 2, 4)
plt.plot([1, 2, 3], [35, 25, 15])

plt.show()

# ============================================================
# ADDING TITLES TO SUBPLOTS
# ============================================================

plt.subplot(1, 2, 1)

plt.plot([1, 2, 3], [10, 20, 30])

plt.title("Plot 1")

plt.subplot(1, 2, 2)

plt.plot([1, 2, 3], [30, 20, 10])

plt.title("Plot 2")

plt.show()

# ============================================================
# MAIN FIGURE TITLE
# ============================================================

plt.subplot(1, 2, 1)

plt.plot([1, 2, 3], [10, 20, 30])

plt.subplot(1, 2, 2)

plt.plot([1, 2, 3], [30, 20, 10])

plt.suptitle("Main Figure Title")

plt.show()

# ============================================================
# SUBPLOTS WITH DIFFERENT CHARTS
# ============================================================

plt.subplot(2, 2, 1)

plt.plot([1, 2, 3], [10, 20, 30])

plt.title("Line Plot")

plt.subplot(2, 2, 2)

plt.bar(
    ["A", "B", "C"],
    [10, 20, 15]
)

plt.title("Bar Chart")

plt.subplot(2, 2, 3)

plt.scatter(
    [1, 2, 3],
    [15, 25, 20]
)

plt.title("Scatter Plot")

plt.subplot(2, 2, 4)

plt.hist(
    [10, 20, 20, 30, 40]
)

plt.title("Histogram")

plt.show()

# ============================================================
# USING FIGURE SIZE
# ============================================================

plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
plt.plot([1, 2, 3], [10, 20, 30])

plt.subplot(1, 2, 2)
plt.plot([1, 2, 3], [30, 20, 10])

plt.show()

# ============================================================
# USING tight_layout()
# ============================================================

plt.subplot(2, 2, 1)
plt.plot([1, 2, 3], [10, 20, 30])

plt.subplot(2, 2, 2)
plt.plot([1, 2, 3], [30, 20, 10])

plt.subplot(2, 2, 3)
plt.plot([1, 2, 3], [15, 25, 35])

plt.subplot(2, 2, 4)
plt.plot([1, 2, 3], [35, 25, 15])

plt.tight_layout()

plt.show()

# ============================================================
# MODERN METHOD USING plt.subplots()
# ============================================================

fig, ax = plt.subplots(
    1,
    2
)

ax[0].plot(
    [1, 2, 3],
    [10, 20, 30]
)

ax[0].set_title("Plot 1")

ax[1].plot(
    [1, 2, 3],
    [30, 20, 10]
)

ax[1].set_title("Plot 2")

plt.show()

# ============================================================
# 2x2 SUBPLOTS USING plt.subplots()
# ============================================================

fig, ax = plt.subplots(
    2,
    2,
    figsize=(8, 6)
)

ax[0, 0].plot(
    [1, 2, 3],
    [10, 20, 30]
)

ax[0, 0].set_title("Plot 1")

ax[0, 1].plot(
    [1, 2, 3],
    [30, 20, 10]
)

ax[0, 1].set_title("Plot 2")

ax[1, 0].plot(
    [1, 2, 3],
    [15, 25, 35]
)

ax[1, 0].set_title("Plot 3")

ax[1, 1].plot(
    [1, 2, 3],
    [35, 25, 15]
)

ax[1, 1].set_title("Plot 4")

plt.tight_layout()

plt.show()

# ============================================================
# PRACTICAL EXAMPLE 1
# SALES DASHBOARD
# ============================================================

fig, ax = plt.subplots(
    1,
    2,
    figsize=(10, 4)
)

ax[0].plot(
    ["Jan", "Feb", "Mar"],
    [1000, 1500, 1200]
)

ax[0].set_title("Sales Trend")

ax[1].bar(
    ["A", "B", "C"],
    [500, 700, 600]
)

ax[1].set_title("Product Sales")

plt.tight_layout()

plt.show()

# ============================================================
# PRACTICAL EXAMPLE 2
# STUDENT ANALYSIS
# ============================================================

fig, ax = plt.subplots(
    2,
    1
)

ax[0].plot(
    ["Test1", "Test2", "Test3"],
    [70, 80, 90]
)

ax[0].set_title("Marks Progress")

ax[1].bar(
    ["Math", "Science", "English"],
    [90, 85, 95]
)

ax[1].set_title("Subject Marks")

plt.tight_layout()

plt.show()

# ============================================================
# PRACTICAL EXAMPLE 3
# MULTIPLE VISUALIZATIONS
# ============================================================

fig, ax = plt.subplots(
    2,
    2,
    figsize=(8, 6)
)

ax[0, 0].plot(
    [1, 2, 3],
    [10, 20, 30]
)

ax[0, 1].bar(
    ["A", "B", "C"],
    [10, 20, 15]
)

ax[1, 0].scatter(
    [1, 2, 3],
    [15, 25, 20]
)

ax[1, 1].hist(
    [10, 20, 20, 30, 40]
)

plt.tight_layout()

plt.show()

# ============================================================
# SUMMARY
# ============================================================

print("""
SUBPLOTS SUMMARY

Old Method:

plt.subplot(rows, cols, position)

Examples:

subplot(1,2,1)
subplot(2,2,3)

Modern Method:

fig, ax = plt.subplots()

Examples:

plt.subplots(1,2)

plt.subplots(2,2)

Useful Functions:

plt.figure()
plt.tight_layout()
plt.suptitle()

Uses:

✔ Dashboards
✔ Multiple Graph Comparison
✔ Data Analysis Reports
✔ Business Reporting

Benefits:

✔ Better Visualization
✔ Organized Layout
✔ Professional Charts
✔ Essential for Data Analysis
""")
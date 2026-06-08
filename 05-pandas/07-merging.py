# ============================================================
# PANDAS MERGING IN PYTHON
# ============================================================

# Merging is used to combine multiple DataFrames.
#
# Similar to SQL JOIN operations.
#
# Types:
# ✔ Inner Join
# ✔ Left Join
# ✔ Right Join
# ✔ Outer Join

# Install Pandas:
# pip install pandas

import pandas as pd

# ============================================================
# SAMPLE DATAFRAMES
# ============================================================

students = pd.DataFrame({
    "Student_ID": [1, 2, 3, 4],
    "Name": ["Amit", "Rahul", "Priya", "Neha"]
})

marks = pd.DataFrame({
    "Student_ID": [1, 2, 3],
    "Marks": [90, 85, 95]
})

print("Students DataFrame")
print(students)

print("\nMarks DataFrame")
print(marks)

# ============================================================
# BASIC MERGE
# ============================================================

result = pd.merge(
    students,
    marks,
    on="Student_ID"
)

print(result)

# Default:
# Inner Join

# ============================================================
# INNER JOIN
# ============================================================

result = pd.merge(
    students,
    marks,
    on="Student_ID",
    how="inner"
)

print(result)

# Only matching records

# ============================================================
# LEFT JOIN
# ============================================================

result = pd.merge(
    students,
    marks,
    on="Student_ID",
    how="left"
)

print(result)

# All records from left DataFrame

# ============================================================
# RIGHT JOIN
# ============================================================

result = pd.merge(
    students,
    marks,
    on="Student_ID",
    how="right"
)

print(result)

# All records from right DataFrame

# ============================================================
# OUTER JOIN
# ============================================================

result = pd.merge(
    students,
    marks,
    on="Student_ID",
    how="outer"
)

print(result)

# All records from both DataFrames

# ============================================================
# MERGING ON DIFFERENT COLUMN NAMES
# ============================================================

students = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Amit", "Rahul", "Priya"]
})

marks = pd.DataFrame({
    "Student_ID": [1, 2, 3],
    "Marks": [90, 85, 95]
})

result = pd.merge(
    students,
    marks,
    left_on="ID",
    right_on="Student_ID"
)

print(result)

# ============================================================
# MERGING MULTIPLE COLUMNS
# ============================================================

df1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Amit", "Rahul", "Priya"],
    "City": ["Mumbai", "Pune", "Delhi"]
})

df2 = pd.DataFrame({
    "ID": [1, 2, 3],
    "City": ["Mumbai", "Pune", "Delhi"],
    "Marks": [90, 85, 95]
})

result = pd.merge(
    df1,
    df2,
    on=["ID", "City"]
)

print(result)

# ============================================================
# CUSTOM SUFFIXES
# ============================================================

df1 = pd.DataFrame({
    "ID": [1, 2],
    "Salary": [50000, 60000]
})

df2 = pd.DataFrame({
    "ID": [1, 2],
    "Salary": [55000, 65000]
})

result = pd.merge(
    df1,
    df2,
    on="ID",
    suffixes=("_Old", "_New")
)

print(result)

# ============================================================
# CHECKING SOURCE OF RECORDS
# ============================================================

result = pd.merge(
    students,
    marks,
    left_on="ID",
    right_on="Student_ID",
    how="outer",
    indicator=True
)

print(result)

# _merge column added

# ============================================================
# CONCATENATION (ROW-WISE)
# ============================================================

df1 = pd.DataFrame({
    "Name": ["Amit", "Rahul"]
})

df2 = pd.DataFrame({
    "Name": ["Priya", "Neha"]
})

result = pd.concat([df1, df2])

print(result)

# ============================================================
# CONCATENATION (COLUMN-WISE)
# ============================================================

df1 = pd.DataFrame({
    "Name": ["Amit", "Rahul"]
})

df2 = pd.DataFrame({
    "Marks": [90, 85]
})

result = pd.concat(
    [df1, df2],
    axis=1
)

print(result)

# ============================================================
# IGNORING INDEX
# ============================================================

df1 = pd.DataFrame({
    "Name": ["Amit", "Rahul"]
})

df2 = pd.DataFrame({
    "Name": ["Priya", "Neha"]
})

result = pd.concat(
    [df1, df2],
    ignore_index=True
)

print(result)

# ============================================================
# JOIN METHOD
# ============================================================

df1 = pd.DataFrame({
    "Name": ["Amit", "Rahul"]
}, index=[1, 2])

df2 = pd.DataFrame({
    "Marks": [90, 85]
}, index=[1, 2])

result = df1.join(df2)

print(result)

# ============================================================
# PRACTICAL EXAMPLE 1
# STUDENTS + MARKS
# ============================================================

students = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Amit", "Rahul", "Priya"]
})

marks = pd.DataFrame({
    "ID": [1, 2, 3],
    "Marks": [90, 85, 95]
})

report = pd.merge(
    students,
    marks,
    on="ID"
)

print(report)

# ============================================================
# PRACTICAL EXAMPLE 2
# EMPLOYEE + DEPARTMENT
# ============================================================

employees = pd.DataFrame({
    "Emp_ID": [1, 2, 3],
    "Name": ["John", "Sara", "Mike"]
})

departments = pd.DataFrame({
    "Emp_ID": [1, 2, 3],
    "Department": ["IT", "HR", "Sales"]
})

result = pd.merge(
    employees,
    departments,
    on="Emp_ID"
)

print(result)

# ============================================================
# PRACTICAL EXAMPLE 3
# SALES DATA
# ============================================================

sales = pd.DataFrame({
    "Product_ID": [1, 2, 3],
    "Sales": [1000, 1500, 2000]
})

products = pd.DataFrame({
    "Product_ID": [1, 2, 3],
    "Product": ["Laptop", "Phone", "Tablet"]
})

result = pd.merge(
    sales,
    products,
    on="Product_ID"
)

print(result)

# ============================================================
# SUMMARY
# ============================================================

print("""
PANDAS MERGING SUMMARY

Merge Function:

pd.merge()

Join Types:

Inner Join:
how="inner"

Left Join:
how="left"

Right Join:
how="right"

Outer Join:
how="outer"

Important Parameters:

on=
left_on=
right_on=
suffixes=
indicator=

Concatenation:

pd.concat()

Row-wise:
axis=0

Column-wise:
axis=1

Join Method:

df.join()

Benefits:

✔ Combine Multiple Tables
✔ SQL-Like Operations
✔ Data Integration
✔ Essential for Analysis
✔ Frequently Used in Projects
""")
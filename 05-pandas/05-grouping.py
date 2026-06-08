# ============================================================
# PANDAS GROUPING (GROUPBY) IN PYTHON
# ============================================================

# Grouping is used to split data into groups and perform
# calculations on each group.
#
# Similar to SQL:
#
# GROUP BY

# Install Pandas:
# pip install pandas

import pandas as pd

# ============================================================
# SAMPLE DATAFRAME
# ============================================================

data = {
    "Department": ["IT", "HR", "IT", "HR", "Sales", "IT"],
    "Employee": ["John", "Sara", "Mike", "Emma", "David", "Tom"],
    "Salary": [50000, 45000, 60000, 47000, 55000, 65000]
}

df = pd.DataFrame(data)

print(df)

# ============================================================
# BASIC GROUPBY
# ============================================================

group = df.groupby("Department")

print(group)

# Output:
# GroupBy Object

# ============================================================
# SUM OF EACH GROUP
# ============================================================

result = df.groupby("Department")["Salary"].sum()

print(result)

# ============================================================
# MEAN OF EACH GROUP
# ============================================================

result = df.groupby("Department")["Salary"].mean()

print(result)

# ============================================================
# COUNT OF EACH GROUP
# ============================================================

result = df.groupby("Department")["Salary"].count()

print(result)

# ============================================================
# MAXIMUM VALUE IN EACH GROUP
# ============================================================

result = df.groupby("Department")["Salary"].max()

print(result)

# ============================================================
# MINIMUM VALUE IN EACH GROUP
# ============================================================

result = df.groupby("Department")["Salary"].min()

print(result)

# ============================================================
# MULTIPLE AGGREGATIONS
# ============================================================

result = df.groupby("Department")["Salary"].agg(
    ["sum", "mean", "max", "min"]
)

print(result)

# ============================================================
# GROUPING BY MULTIPLE COLUMNS
# ============================================================

data = {
    "Department": ["IT", "IT", "HR", "HR"],
    "Gender": ["M", "F", "M", "F"],
    "Salary": [50000, 60000, 45000, 55000]
}

df = pd.DataFrame(data)

result = df.groupby(
    ["Department", "Gender"]
)["Salary"].mean()

print(result)

# ============================================================
# GROUPING MULTIPLE COLUMNS
# ============================================================

data = {
    "Department": ["IT", "HR", "IT"],
    "Salary": [50000, 45000, 60000],
    "Bonus": [5000, 4000, 6000]
}

df = pd.DataFrame(data)

result = df.groupby("Department")[
    ["Salary", "Bonus"]
].sum()

print(result)

# ============================================================
# USING as_index=False
# ============================================================

result = df.groupby(
    "Department",
    as_index=False
)["Salary"].sum()

print(result)

# ============================================================
# RESETTING INDEX
# ============================================================

result = df.groupby(
    "Department"
)["Salary"].sum().reset_index()

print(result)

# ============================================================
# ITERATING THROUGH GROUPS
# ============================================================

data = {
    "Department": ["IT", "HR", "IT"],
    "Salary": [50000, 45000, 60000]
}

df = pd.DataFrame(data)

groups = df.groupby("Department")

for name, group in groups:
    print("Group:", name)
    print(group)

# ============================================================
# GET SPECIFIC GROUP
# ============================================================

groups = df.groupby("Department")

print(groups.get_group("IT"))

# ============================================================
# SIZE OF EACH GROUP
# ============================================================

result = df.groupby("Department").size()

print(result)

# ============================================================
# VALUE COUNTS USING GROUPBY
# ============================================================

data = {
    "Department": ["IT", "HR", "IT", "Sales", "HR"]
}

df = pd.DataFrame(data)

print(
    df.groupby("Department").size()
)

# ============================================================
# CUSTOM AGGREGATION
# ============================================================

data = {
    "Department": ["IT", "HR", "IT"],
    "Salary": [50000, 45000, 60000]
}

df = pd.DataFrame(data)

result = df.groupby(
    "Department"
)["Salary"].agg(
    lambda x: max(x) - min(x)
)

print(result)

# ============================================================
# NAMED AGGREGATIONS
# ============================================================

data = {
    "Department": ["IT", "HR", "IT"],
    "Salary": [50000, 45000, 60000]
}

df = pd.DataFrame(data)

result = df.groupby("Department").agg(
    Total_Salary=("Salary", "sum"),
    Average_Salary=("Salary", "mean")
)

print(result)

# ============================================================
# PRACTICAL EXAMPLE 1
# STUDENT MARKS
# ============================================================

students = pd.DataFrame({
    "Class": ["A", "A", "B", "B"],
    "Marks": [80, 90, 85, 95]
})

result = students.groupby(
    "Class"
)["Marks"].mean()

print(result)

# ============================================================
# PRACTICAL EXAMPLE 2
# SALES DATA
# ============================================================

sales = pd.DataFrame({
    "Region": ["North", "South", "North", "South"],
    "Sales": [1000, 1500, 2000, 2500]
})

result = sales.groupby(
    "Region"
)["Sales"].sum()

print(result)

# ============================================================
# PRACTICAL EXAMPLE 3
# EMPLOYEE SALARY
# ============================================================

employees = pd.DataFrame({
    "Department": ["IT", "HR", "IT", "HR"],
    "Salary": [50000, 45000, 60000, 55000]
})

result = employees.groupby(
    "Department"
)["Salary"].mean()

print(result)

# ============================================================
# SUMMARY
# ============================================================

print("""
PANDAS GROUPBY SUMMARY

Purpose:

Split Data Into Groups
Apply Calculations
Combine Results

Syntax:

df.groupby("Column")

Common Aggregations:

sum()
mean()
count()
max()
min()
size()

Multiple Aggregations:

agg(["sum","mean","max"])

Multiple Grouping:

df.groupby(
    ["Column1","Column2"]
)

Useful Methods:

get_group()
reset_index()

Benefits:

✔ Data Summarization
✔ Faster Analysis
✔ SQL-Like Operations
✔ Powerful Reporting
✔ Essential for Data Science
""")
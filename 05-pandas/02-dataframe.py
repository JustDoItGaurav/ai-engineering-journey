# ============================================================
# PANDAS DATAFRAME IN PYTHON
# ============================================================

# A DataFrame is a two-dimensional data structure in Pandas.
#
# Think of it as a table with:
#
# Rows + Columns
#
# Similar to:
# ✔ Excel Sheet
# ✔ SQL Table
# ✔ CSV File

# Install Pandas:
# pip install pandas

import pandas as pd

# ============================================================
# CREATING A DATAFRAME
# ============================================================

data = {
    "Name": ["Gaurav", "Rahul", "Priya"],
    "Age": [21, 22, 20],
    "Marks": [95, 88, 92]
}

df = pd.DataFrame(data)

print(df)

# ============================================================
# DATAFRAME STRUCTURE
# ============================================================

data = {
    "Name": ["Amit", "Rahul"],
    "Age": [21, 22]
}

df = pd.DataFrame(data)

print(df)

# Output:
#
#    Name   Age
# 0  Amit   21
# 1 Rahul   22

# ============================================================
# CHECKING DATA TYPE
# ============================================================

df = pd.DataFrame({
    "A": [1, 2, 3]
})

print(type(df))

# Output:
# <class 'pandas.core.frame.DataFrame'>

# ============================================================
# DATAFRAME ATTRIBUTES
# ============================================================

df = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Marks": [80, 90, 95]
})

print("Shape :", df.shape)
print("Size  :", df.size)
print("Columns :", df.columns)
print("Index :", df.index)

# ============================================================
# VIEWING FIRST ROWS
# ============================================================

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D", "E"],
    "Marks": [80, 90, 95, 75, 85]
})

print(df.head())

# First 5 rows

# ============================================================
# VIEWING LAST ROWS
# ============================================================

print(df.tail())

# Last 5 rows

# ============================================================
# SPECIFIC NUMBER OF ROWS
# ============================================================

print(df.head(2))

print(df.tail(2))

# ============================================================
# ACCESSING A COLUMN
# ============================================================

df = pd.DataFrame({
    "Name": ["Amit", "Rahul", "Priya"],
    "Marks": [90, 85, 95]
})

print(df["Name"])

# ============================================================
# ACCESSING MULTIPLE COLUMNS
# ============================================================

print(df[["Name", "Marks"]])

# ============================================================
# ACCESSING ROWS USING iloc[]
# ============================================================

df = pd.DataFrame({
    "Name": ["Amit", "Rahul", "Priya"],
    "Marks": [90, 85, 95]
})

print(df.iloc[0])

print(df.iloc[1])

# ============================================================
# ACCESSING MULTIPLE ROWS
# ============================================================

print(df.iloc[0:2])

# ============================================================
# ACCESSING ROWS USING loc[]
# ============================================================

df = pd.DataFrame({
    "Name": ["Amit", "Rahul", "Priya"],
    "Marks": [90, 85, 95]
})

print(df.loc[0])

# ============================================================
# ACCESSING SPECIFIC VALUE
# ============================================================

print(df.loc[1, "Marks"])

# Output:
# 85

# ============================================================
# ADDING A NEW COLUMN
# ============================================================

df = pd.DataFrame({
    "Name": ["Amit", "Rahul"],
    "Marks": [90, 85]
})

df["Grade"] = ["A", "B"]

print(df)

# ============================================================
# MODIFYING A COLUMN
# ============================================================

df["Marks"] = [95, 88]

print(df)

# ============================================================
# ADDING A NEW ROW
# ============================================================

df.loc[len(df)] = ["Priya", 92, "A"]

print(df)

# ============================================================
# DELETING A COLUMN
# ============================================================

df = df.drop("Grade", axis=1)

print(df)

# ============================================================
# DELETING A ROW
# ============================================================

df = df.drop(0)

print(df)

# ============================================================
# DATAFRAME INFORMATION
# ============================================================

df = pd.DataFrame({
    "Name": ["Amit", "Rahul", "Priya"],
    "Age": [21, 22, 20]
})

print(df.info())

# ============================================================
# DESCRIBE DATA
# ============================================================

df = pd.DataFrame({
    "Marks": [80, 90, 95, 85, 75]
})

print(df.describe())

# ============================================================
# FILTERING DATA
# ============================================================

df = pd.DataFrame({
    "Name": ["Amit", "Rahul", "Priya"],
    "Marks": [90, 75, 95]
})

print(df[df["Marks"] > 80])

# ============================================================
# MULTIPLE CONDITIONS
# ============================================================

df = pd.DataFrame({
    "Name": ["Amit", "Rahul", "Priya"],
    "Marks": [90, 75, 95],
    "Age": [21, 22, 20]
})

print(df[(df["Marks"] > 80) & (df["Age"] < 22)])

# ============================================================
# SORTING VALUES
# ============================================================

df = pd.DataFrame({
    "Name": ["Amit", "Rahul", "Priya"],
    "Marks": [90, 75, 95]
})

print(df.sort_values("Marks"))

# ============================================================
# SORTING DESCENDING
# ============================================================

print(df.sort_values("Marks", ascending=False))

# ============================================================
# UNIQUE VALUES
# ============================================================

df = pd.DataFrame({
    "City": ["Mumbai", "Pune", "Mumbai", "Delhi"]
})

print(df["City"].unique())

# ============================================================
# VALUE COUNTS
# ============================================================

print(df["City"].value_counts())

# ============================================================
# RENAMING COLUMNS
# ============================================================

df = pd.DataFrame({
    "Name": ["Amit"],
    "Marks": [90]
})

df = df.rename(columns={"Marks": "Score"})

print(df)

# ============================================================
# CONVERT DATAFRAME TO NUMPY ARRAY
# ============================================================

df = pd.DataFrame({
    "A": [1, 2],
    "B": [3, 4]
})

print(df.to_numpy())

# ============================================================
# PRACTICAL EXAMPLE 1
# STUDENT DATABASE
# ============================================================

students = pd.DataFrame({
    "Name": ["Amit", "Rahul", "Priya"],
    "Marks": [90, 85, 95]
})

print(students)

print("Average Marks:", students["Marks"].mean())

# ============================================================
# PRACTICAL EXAMPLE 2
# SALES REPORT
# ============================================================

sales = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar"],
    "Sales": [1000, 1500, 1800]
})

print(sales)

print("Total Sales:", sales["Sales"].sum())

# ============================================================
# PRACTICAL EXAMPLE 3
# EMPLOYEE DATA
# ============================================================

employees = pd.DataFrame({
    "Name": ["John", "Sara", "Mike"],
    "Salary": [50000, 60000, 55000]
})

print(employees)

print("Highest Salary:",
      employees["Salary"].max())

# ============================================================
# SUMMARY
# ============================================================

print("""
PANDAS DATAFRAME SUMMARY

Definition:

Two-Dimensional Data Structure

Creation:

pd.DataFrame(data)

Access Methods:

df["Column"]
df.iloc[]
df.loc[]

Attributes:

shape
size
columns
index

Useful Functions:

head()
tail()
info()
describe()

Operations:

Add Column
Delete Column
Add Row
Delete Row
Filter Data
Sort Data

Statistics:

mean()
sum()
max()
min()

Conversion:

to_numpy()

Benefits:

✔ Table-Like Structure
✔ Easy Data Analysis
✔ Fast Data Processing
✔ Built-in Statistics
✔ Most Important Pandas Object
""")
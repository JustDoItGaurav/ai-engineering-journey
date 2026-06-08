# ============================================================
# READING FILES IN PANDAS
# ============================================================

# Pandas can read data from many file formats:
#
# ✔ CSV Files
# ✔ Excel Files
# ✔ JSON Files
# ✔ Text Files
# ✔ SQL Databases
#
# Most commonly used:
# CSV and Excel

# Install Pandas:
# pip install pandas

import pandas as pd

# ============================================================
# READING CSV FILE
# ============================================================

# students.csv

# Name,Age,Marks
# Amit,21,90
# Rahul,22,85
# Priya,20,95

df = pd.read_csv("students.csv")

print(df)

# ============================================================
# VIEW FIRST ROWS
# ============================================================

df = pd.read_csv("students.csv")

print(df.head())

# First 5 rows

# ============================================================
# VIEW LAST ROWS
# ============================================================

print(df.tail())

# Last 5 rows

# ============================================================
# READ SPECIFIC NUMBER OF ROWS
# ============================================================

df = pd.read_csv("students.csv")

print(df.head(2))

# First 2 rows

# ============================================================
# READ ONLY FEW ROWS
# ============================================================

df = pd.read_csv(
    "students.csv",
    nrows=2
)

print(df)

# ============================================================
# CHECK FILE INFORMATION
# ============================================================

df = pd.read_csv("students.csv")

print(df.info())

# ============================================================
# CHECK DATA TYPES
# ============================================================

df = pd.read_csv("students.csv")

print(df.dtypes)

# ============================================================
# READING EXCEL FILE
# ============================================================

# Install:
# pip install openpyxl

df = pd.read_excel("students.xlsx")

print(df)

# ============================================================
# READ SPECIFIC SHEET
# ============================================================

df = pd.read_excel(
    "students.xlsx",
    sheet_name="Sheet1"
)

print(df)

# ============================================================
# READ MULTIPLE SHEETS
# ============================================================

sheets = pd.read_excel(
    "students.xlsx",
    sheet_name=None
)

print(sheets)

# ============================================================
# READING JSON FILE
# ============================================================

df = pd.read_json("students.json")

print(df)

# ============================================================
# READING TEXT FILE
# ============================================================

df = pd.read_csv(
    "students.txt",
    delimiter=","
)

print(df)

# ============================================================
# READING TAB SEPARATED FILE
# ============================================================

df = pd.read_csv(
    "students.tsv",
    sep="\t"
)

print(df)

# ============================================================
# READING FILE WITHOUT HEADER
# ============================================================

df = pd.read_csv(
    "students.csv",
    header=None
)

print(df)

# ============================================================
# ADDING CUSTOM COLUMN NAMES
# ============================================================

df = pd.read_csv(
    "students.csv",
    names=["Name", "Age", "Marks"]
)

print(df)

# ============================================================
# SELECT SPECIFIC COLUMNS
# ============================================================

df = pd.read_csv(
    "students.csv",
    usecols=["Name", "Marks"]
)

print(df)

# ============================================================
# SKIP ROWS
# ============================================================

df = pd.read_csv(
    "students.csv",
    skiprows=1
)

print(df)

# ============================================================
# HANDLE MISSING VALUES
# ============================================================

df = pd.read_csv(
    "students.csv",
    na_values=["NA", "null"]
)

print(df)

# ============================================================
# CHECK MISSING VALUES
# ============================================================

df = pd.read_csv("students.csv")

print(df.isnull())

# ============================================================
# COUNT MISSING VALUES
# ============================================================

print(df.isnull().sum())

# ============================================================
# DISPLAY SHAPE
# ============================================================

df = pd.read_csv("students.csv")

print(df.shape)

# Output:
# (rows, columns)

# ============================================================
# DISPLAY COLUMN NAMES
# ============================================================

print(df.columns)

# ============================================================
# DISPLAY INDEX
# ============================================================

print(df.index)

# ============================================================
# DISPLAY SUMMARY STATISTICS
# ============================================================

print(df.describe())

# ============================================================
# LOADING LARGE FILES
# ============================================================

df = pd.read_csv(
    "large_file.csv",
    chunksize=1000
)

for chunk in df:
    print(chunk.head())

# ============================================================
# PRACTICAL EXAMPLE 1
# STUDENT DATA
# ============================================================

students = pd.read_csv("students.csv")

print(students.head())

print("Average Marks:",
      students["Marks"].mean())

# ============================================================
# PRACTICAL EXAMPLE 2
# SALES DATA
# ============================================================

sales = pd.read_excel("sales.xlsx")

print(sales.head())

print("Total Sales:",
      sales["Sales"].sum())

# ============================================================
# PRACTICAL EXAMPLE 3
# EMPLOYEE DATA
# ============================================================

employees = pd.read_json("employees.json")

print(employees.head())

# ============================================================
# COMMON ERRORS
# ============================================================

# File Not Found

# pd.read_csv("wrong_file.csv")

# Error:
# FileNotFoundError

# Solution:
# Check file path

# ============================================================
# USING FULL FILE PATH
# ============================================================

df = pd.read_csv(
    r"C:\Users\Gaurav\Documents\students.csv"
)

print(df)

# ============================================================
# SUMMARY
# ============================================================

print("""
PANDAS READING FILES SUMMARY

CSV Files:

pd.read_csv("file.csv")

Excel Files:

pd.read_excel("file.xlsx")

JSON Files:

pd.read_json("file.json")

Text Files:

pd.read_csv("file.txt")

Useful Parameters:

head()
tail()

nrows=
usecols=
skiprows=
header=
names=
sep=
sheet_name=

Data Inspection:

info()
describe()
shape
columns
dtypes

Missing Values:

isnull()
isnull().sum()

Benefits:

✔ Quick File Loading
✔ Supports Multiple Formats
✔ Easy Data Analysis
✔ Handles Large Datasets
✔ Essential for Data Science
""")
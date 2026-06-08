# ============================================================
# DATA CLEANING IN PANDAS
# ============================================================

# Data Cleaning is the process of fixing or removing:
#
# ✔ Missing Values
# ✔ Duplicate Data
# ✔ Incorrect Data Types
# ✔ Extra Spaces
# ✔ Invalid Values
# ✔ Outliers
#
# Data Cleaning is one of the most important steps in
# Data Analysis and Machine Learning.

# Install Pandas:
# pip install pandas

import pandas as pd
import numpy as np

# ============================================================
# SAMPLE DIRTY DATASET
# ============================================================

data = {
    "Name": ["Amit", " Rahul ", "Priya", "Amit"],
    "Age": [21, np.nan, 20, 21],
    "Marks": [90, 85, np.nan, 90]
}

df = pd.DataFrame(data)

print(df)

# ============================================================
# CHECK BASIC INFORMATION
# ============================================================

print(df.info())

# ============================================================
# CHECK MISSING VALUES
# ============================================================

print(df.isnull())

# ============================================================
# COUNT MISSING VALUES
# ============================================================

print(df.isnull().sum())

# ============================================================
# REMOVE ROWS WITH MISSING VALUES
# ============================================================

clean_df = df.dropna()

print(clean_df)

# ============================================================
# FILL MISSING VALUES WITH 0
# ============================================================

filled_df = df.fillna(0)

print(filled_df)

# ============================================================
# FILL MISSING VALUES WITH MEAN
# ============================================================

df["Age"] = df["Age"].fillna(
    df["Age"].mean()
)

df["Marks"] = df["Marks"].fillna(
    df["Marks"].mean()
)

print(df)

# ============================================================
# FILL MISSING VALUES WITH MEDIAN
# ============================================================

df["Age"] = df["Age"].fillna(
    df["Age"].median()
)

print(df)

# ============================================================
# FILL MISSING VALUES WITH MODE
# ============================================================

df["Age"] = df["Age"].fillna(
    df["Age"].mode()[0]
)

print(df)

# ============================================================
# CHECK DUPLICATE ROWS
# ============================================================

print(df.duplicated())

# ============================================================
# COUNT DUPLICATES
# ============================================================

print(df.duplicated().sum())

# ============================================================
# REMOVE DUPLICATES
# ============================================================

df = df.drop_duplicates()

print(df)

# ============================================================
# REMOVE EXTRA SPACES
# ============================================================

df["Name"] = df["Name"].str.strip()

print(df)

# ============================================================
# CONVERT TO UPPERCASE
# ============================================================

df["Name"] = df["Name"].str.upper()

print(df)

# ============================================================
# CONVERT TO LOWERCASE
# ============================================================

df["Name"] = df["Name"].str.lower()

print(df)

# ============================================================
# REPLACE VALUES
# ============================================================

df["Name"] = df["Name"].replace(
    "amit",
    "Amit Kumar"
)

print(df)

# ============================================================
# CHECK DATA TYPES
# ============================================================

print(df.dtypes)

# ============================================================
# CHANGE DATA TYPE
# ============================================================

df["Age"] = df["Age"].astype(int)

print(df.dtypes)

# ============================================================
# RENAME COLUMNS
# ============================================================

df = df.rename(
    columns={
        "Marks": "Score"
    }
)

print(df)

# ============================================================
# FIND UNIQUE VALUES
# ============================================================

print(df["Name"].unique())

# ============================================================
# COUNT UNIQUE VALUES
# ============================================================

print(df["Name"].nunique())

# ============================================================
# REMOVE INVALID VALUES
# ============================================================

data = {
    "Age": [20, 25, -10, 30]
}

df = pd.DataFrame(data)

df = df[df["Age"] >= 0]

print(df)

# ============================================================
# DETECT OUTLIERS
# ============================================================

data = {
    "Salary": [30000, 35000, 40000, 45000, 500000]
}

df = pd.DataFrame(data)

print(df)

# ============================================================
# IQR METHOD FOR OUTLIERS
# ============================================================

Q1 = df["Salary"].quantile(0.25)

Q3 = df["Salary"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

clean_df = df[
    (df["Salary"] >= lower_limit) &
    (df["Salary"] <= upper_limit)
]

print(clean_df)

# ============================================================
# REMOVE NULL ROWS IN SPECIFIC COLUMN
# ============================================================

data = {
    "Name": ["Amit", None, "Priya"]
}

df = pd.DataFrame(data)

df = df.dropna(
    subset=["Name"]
)

print(df)

# ============================================================
# FORWARD FILL
# ============================================================

data = {
    "Marks": [90, np.nan, np.nan, 95]
}

df = pd.DataFrame(data)

print(df.ffill())

# ============================================================
# BACKWARD FILL
# ============================================================

print(df.bfill())

# ============================================================
# CHECK FINAL DATASET
# ============================================================

print(df.info())

print(df.describe())

# ============================================================
# PRACTICAL EXAMPLE 1
# STUDENT DATA CLEANING
# ============================================================

students = pd.DataFrame({
    "Marks": [80, 90, np.nan, 95]
})

students["Marks"] = students["Marks"].fillna(
    students["Marks"].mean()
)

print(students)

# ============================================================
# PRACTICAL EXAMPLE 2
# EMPLOYEE DATA CLEANING
# ============================================================

employees = pd.DataFrame({
    "Name": ["John", " John ", "Sara"]
})

employees["Name"] = employees["Name"].str.strip()

employees = employees.drop_duplicates()

print(employees)

# ============================================================
# PRACTICAL EXAMPLE 3
# SALES DATA CLEANING
# ============================================================

sales = pd.DataFrame({
    "Sales": [1000, 1200, np.nan, 1500]
})

sales["Sales"] = sales["Sales"].fillna(
    sales["Sales"].mean()
)

print(sales)

# ============================================================
# DATA CLEANING WORKFLOW
# ============================================================

# 1. Read Data
# 2. Check Missing Values
# 3. Handle Missing Values
# 4. Remove Duplicates
# 5. Fix Data Types
# 6. Clean Text Data
# 7. Handle Outliers
# 8. Validate Data

# ============================================================
# SUMMARY
# ============================================================

print("""
DATA CLEANING SUMMARY

Missing Values:

isnull()
dropna()
fillna()

Duplicates:

duplicated()
drop_duplicates()

String Cleaning:

str.strip()
str.upper()
str.lower()

Replace Values:

replace()

Data Types:

astype()

Rename Columns:

rename()

Unique Values:

unique()
nunique()

Outlier Handling:

quantile()
IQR Method

Useful Functions:

info()
describe()

Data Cleaning Workflow:

Read Data
↓
Check Missing Values
↓
Handle Missing Values
↓
Remove Duplicates
↓
Fix Data Types
↓
Clean Text
↓
Handle Outliers
↓
Analyze Data

Benefits:

✔ Better Data Quality
✔ Accurate Analysis
✔ Better ML Models
✔ Fewer Errors
✔ Professional Data Processing
""")
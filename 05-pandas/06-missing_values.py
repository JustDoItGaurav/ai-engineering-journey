# ============================================================
# PANDAS MISSING VALUES IN PYTHON
# ============================================================

# Missing Values are empty or unavailable data in a dataset.
#
# Missing values may appear as:
#
# NaN
# None
# Null
#
# Handling missing values is one of the most important
# steps in Data Cleaning.

# Install Pandas:
# pip install pandas

import pandas as pd
import numpy as np

# ============================================================
# CREATING DATAFRAME WITH MISSING VALUES
# ============================================================

data = {
    "Name": ["Amit", "Rahul", "Priya", None],
    "Age": [21, np.nan, 20, 22],
    "Marks": [90, 85, np.nan, 95]
}

df = pd.DataFrame(data)

print(df)

# ============================================================
# CHECKING MISSING VALUES
# ============================================================

print(df.isnull())

# Output:
# True  -> Missing Value
# False -> Available Value

# ============================================================
# CHECKING MISSING VALUES USING isna()
# ============================================================

print(df.isna())

# Same as isnull()

# ============================================================
# COUNT MISSING VALUES
# ============================================================

print(df.isnull().sum())

# Missing values in each column

# ============================================================
# TOTAL MISSING VALUES
# ============================================================

print(df.isnull().sum().sum())

# Total missing values in DataFrame

# ============================================================
# CHECKING NON-MISSING VALUES
# ============================================================

print(df.notnull())

# Output:
# True -> Data Exists
# False -> Missing

# ============================================================
# DISPLAY ROWS WITH MISSING VALUES
# ============================================================

print(df[df.isnull().any(axis=1)])

# Rows containing at least one missing value

# ============================================================
# DISPLAY ROWS WITHOUT MISSING VALUES
# ============================================================

print(df.dropna())

# Removes rows containing missing values

# ============================================================
# DROPPING ROWS WITH MISSING VALUES
# ============================================================

clean_df = df.dropna()

print(clean_df)

# ============================================================
# DROPPING COLUMNS WITH MISSING VALUES
# ============================================================

clean_df = df.dropna(axis=1)

print(clean_df)

# axis=1 -> Columns

# ============================================================
# DROPPING ROWS ONLY IF ALL VALUES ARE MISSING
# ============================================================

clean_df = df.dropna(how="all")

print(clean_df)

# ============================================================
# DROPPING ROWS IF ANY VALUE IS MISSING
# ============================================================

clean_df = df.dropna(how="any")

print(clean_df)

# ============================================================
# FILLING MISSING VALUES
# ============================================================

filled_df = df.fillna(0)

print(filled_df)

# ============================================================
# FILLING WITH CUSTOM VALUE
# ============================================================

filled_df = df.fillna("Unknown")

print(filled_df)

# ============================================================
# FILLING SPECIFIC COLUMN
# ============================================================

df["Age"] = df["Age"].fillna(18)

print(df)

# ============================================================
# FILLING USING MEAN
# ============================================================

data = {
    "Marks": [90, 85, np.nan, 95]
}

df = pd.DataFrame(data)

df["Marks"] = df["Marks"].fillna(
    df["Marks"].mean()
)

print(df)

# ============================================================
# FILLING USING MEDIAN
# ============================================================

data = {
    "Marks": [90, 85, np.nan, 95]
}

df = pd.DataFrame(data)

df["Marks"] = df["Marks"].fillna(
    df["Marks"].median()
)

print(df)

# ============================================================
# FILLING USING MODE
# ============================================================

data = {
    "Marks": [90, 85, 85, np.nan]
}

df = pd.DataFrame(data)

df["Marks"] = df["Marks"].fillna(
    df["Marks"].mode()[0]
)

print(df)

# ============================================================
# FORWARD FILL (ffill)
# ============================================================

data = {
    "Marks": [90, np.nan, np.nan, 95]
}

df = pd.DataFrame(data)

print(df.ffill())

# Previous value fills missing values

# ============================================================
# BACKWARD FILL (bfill)
# ============================================================

data = {
    "Marks": [90, np.nan, np.nan, 95]
}

df = pd.DataFrame(data)

print(df.bfill())

# Next value fills missing values

# ============================================================
# REPLACING MISSING VALUES
# ============================================================

df = pd.DataFrame({
    "Marks": [90, np.nan, 85]
})

df.replace(np.nan, 0, inplace=True)

print(df)

# ============================================================
# CHECKING PERCENTAGE OF MISSING VALUES
# ============================================================

data = {
    "A": [1, np.nan, 3],
    "B": [np.nan, np.nan, 5]
}

df = pd.DataFrame(data)

percentage = (
    df.isnull().sum() / len(df)
) * 100

print(percentage)

# ============================================================
# PRACTICAL EXAMPLE 1
# STUDENT DATA
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
# EMPLOYEE DATA
# ============================================================

employees = pd.DataFrame({
    "Salary": [50000, np.nan, 60000]
})

employees["Salary"] = employees["Salary"].fillna(
    employees["Salary"].median()
)

print(employees)

# ============================================================
# PRACTICAL EXAMPLE 3
# SALES DATA
# ============================================================

sales = pd.DataFrame({
    "Sales": [1000, np.nan, 1500]
})

sales["Sales"] = sales["Sales"].ffill()

print(sales)

# ============================================================
# SUMMARY
# ============================================================

print("""
PANDAS MISSING VALUES SUMMARY

Checking Missing Values:

isnull()
isna()

Checking Available Values:

notnull()

Counting Missing Values:

df.isnull().sum()

Removing Missing Values:

dropna()

axis=0 -> Rows
axis=1 -> Columns

Filling Missing Values:

fillna()

Methods:

Mean:
fillna(df.mean())

Median:
fillna(df.median())

Mode:
fillna(df.mode()[0])

Forward Fill:

ffill()

Backward Fill:

bfill()

Replacing Values:

replace()

Benefits:

✔ Cleaner Data
✔ Better Analysis
✔ Improved ML Models
✔ Prevents Errors
✔ Essential Data Cleaning Step
""")
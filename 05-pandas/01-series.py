# ============================================================
# PANDAS SERIES IN PYTHON
# ============================================================

# A Series is a one-dimensional labeled array in Pandas.
#
# It can store:
# ✔ Integers
# ✔ Floats
# ✔ Strings
# ✔ Objects
#
# Think of Series as:
#
# Index + Values

# Install Pandas:
# pip install pandas

import pandas as pd

# ============================================================
# CREATING A SERIES
# ============================================================

data = [10, 20, 30, 40, 50]

series = pd.Series(data)

print(series)

# ============================================================
# SERIES STRUCTURE
# ============================================================

data = [100, 200, 300]

series = pd.Series(data)

print(series)

# Output:
#
# 0    100
# 1    200
# 2    300
# dtype: int64

# ============================================================
# ACCESSING VALUES
# ============================================================

series = pd.Series([10, 20, 30, 40])

print(series[0])
print(series[2])

# Output:
# 10
# 30

# ============================================================
# CUSTOM INDEX
# ============================================================

series = pd.Series(
    [90, 85, 95],
    index=["Math", "Science", "English"]
)

print(series)

# ============================================================
# ACCESSING USING LABELS
# ============================================================

series = pd.Series(
    [90, 85, 95],
    index=["Math", "Science", "English"]
)

print(series["Math"])
print(series["English"])

# ============================================================
# SERIES FROM DICTIONARY
# ============================================================

student = {
    "Name": "Gaurav",
    "Age": 21,
    "Marks": 95
}

series = pd.Series(student)

print(series)

# ============================================================
# CHECKING DATA TYPE
# ============================================================

series = pd.Series([10, 20, 30])

print(series.dtype)

# ============================================================
# SERIES ATTRIBUTES
# ============================================================

series = pd.Series([10, 20, 30, 40])

print("Size :", series.size)
print("Shape:", series.shape)
print("Index:", series.index)

# ============================================================
# SLICING SERIES
# ============================================================

series = pd.Series([10, 20, 30, 40, 50])

print(series[1:4])

# Output:
# 20
# 30
# 40

# ============================================================
# NEGATIVE INDEXING
# ============================================================

series = pd.Series([10, 20, 30, 40, 50])

print(series[-1])

# Note:
# In newer pandas versions use:
# series.iloc[-1]

# ============================================================
# USING iloc[]
# ============================================================

series = pd.Series([10, 20, 30, 40, 50])

print(series.iloc[0])
print(series.iloc[3])

# ============================================================
# USING loc[]
# ============================================================

series = pd.Series(
    [90, 80, 95],
    index=["Math", "Science", "English"]
)

print(series.loc["Math"])
print(series.loc["English"])

# ============================================================
# MODIFYING VALUES
# ============================================================

series = pd.Series([10, 20, 30])

series[1] = 100

print(series)

# ============================================================
# ADDING NEW ELEMENT
# ============================================================

series = pd.Series(
    [90, 80],
    index=["Math", "Science"]
)

series["English"] = 95

print(series)

# ============================================================
# DELETING ELEMENT
# ============================================================

series = pd.Series(
    [90, 80, 95],
    index=["Math", "Science", "English"]
)

series = series.drop("Science")

print(series)

# ============================================================
# SERIES MATHEMATICAL OPERATIONS
# ============================================================

series = pd.Series([10, 20, 30])

print(series + 10)
print(series * 2)

# ============================================================
# SERIES STATISTICS
# ============================================================

series = pd.Series([10, 20, 30, 40, 50])

print("Sum    :", series.sum())
print("Mean   :", series.mean())
print("Max    :", series.max())
print("Min    :", series.min())

# ============================================================
# FILTERING SERIES
# ============================================================

series = pd.Series([10, 20, 30, 40, 50])

print(series[series > 25])

# Output:
# 30
# 40
# 50

# ============================================================
# CHECKING CONDITIONS
# ============================================================

series = pd.Series([10, 20, 30, 40])

print(series > 20)

# ============================================================
# SORTING VALUES
# ============================================================

series = pd.Series([50, 10, 40, 20, 30])

print(series.sort_values())

# ============================================================
# SORTING INDEX
# ============================================================

series = pd.Series(
    [90, 80, 95],
    index=["Math", "Science", "English"]
)

print(series.sort_index())

# ============================================================
# UNIQUE VALUES
# ============================================================

series = pd.Series([10, 20, 10, 30, 20])

print(series.unique())

# ============================================================
# VALUE COUNTS
# ============================================================

series = pd.Series([10, 20, 10, 30, 20, 10])

print(series.value_counts())

# ============================================================
# CONVERT SERIES TO LIST
# ============================================================

series = pd.Series([10, 20, 30])

print(series.tolist())

# ============================================================
# CONVERT SERIES TO NUMPY ARRAY
# ============================================================

series = pd.Series([10, 20, 30])

print(series.to_numpy())

# ============================================================
# PRACTICAL EXAMPLE 1
# STUDENT MARKS
# ============================================================

marks = pd.Series(
    [85, 90, 95],
    index=["Math", "Science", "English"]
)

print(marks)

print("Average:", marks.mean())

# ============================================================
# PRACTICAL EXAMPLE 2
# MONTHLY SALES
# ============================================================

sales = pd.Series(
    [1000, 1200, 1500],
    index=["Jan", "Feb", "Mar"]
)

print(sales)

print("Total Sales:", sales.sum())

# ============================================================
# PRACTICAL EXAMPLE 3
# TEMPERATURE DATA
# ============================================================

temperature = pd.Series(
    [30, 32, 35, 31, 29]
)

print("Maximum Temp:", temperature.max())

print("Minimum Temp:", temperature.min())

# ============================================================
# SUMMARY
# ============================================================

print("""
PANDAS SERIES SUMMARY

Definition:

One-Dimensional Labeled Array

Creation:

pd.Series(data)

Access Methods:

series[0]
series.iloc[0]
series.loc["Label"]

Attributes:

size
shape
index
dtype

Common Functions:

sum()
mean()
max()
min()
unique()
value_counts()

Operations:

Slicing
Filtering
Sorting
Modification

Conversion:

tolist()
to_numpy()

Benefits:

✔ Easy Data Handling
✔ Labels with Data
✔ Fast Operations
✔ Built-in Statistics
✔ Foundation of Pandas DataFrames
""")
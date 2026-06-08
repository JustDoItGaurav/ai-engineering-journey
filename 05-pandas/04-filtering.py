# ============================================================
# PANDAS FILTERING IN PYTHON
# ============================================================

# Filtering is used to select specific rows from a DataFrame
# based on conditions.

# Install Pandas:
# pip install pandas

import pandas as pd

# ============================================================
# SAMPLE DATAFRAME
# ============================================================

data = {
    "Name": ["Amit", "Rahul", "Priya", "Neha", "Karan"],
    "Age": [21, 22, 20, 23, 19],
    "Marks": [90, 75, 95, 85, 70]
}

df = pd.DataFrame(data)

print(df)

# ============================================================
# FILTERING SINGLE CONDITION
# ============================================================

print(df[df["Marks"] > 80])

# Output:
# Students having marks greater than 80

# ============================================================
# FILTERING AGE
# ============================================================

print(df[df["Age"] >= 21])

# Output:
# Students age 21 or above

# ============================================================
# FILTERING LESS THAN CONDITION
# ============================================================

print(df[df["Marks"] < 80])

# Output:
# Students with marks below 80

# ============================================================
# EQUAL TO CONDITION
# ============================================================

print(df[df["Name"] == "Priya"])

# Output:
# Row containing Priya

# ============================================================
# NOT EQUAL TO CONDITION
# ============================================================

print(df[df["Name"] != "Rahul"])

# Output:
# All rows except Rahul

# ============================================================
# MULTIPLE CONDITIONS USING &
# ============================================================

print(
    df[
        (df["Marks"] > 80) &
        (df["Age"] < 23)
    ]
)

# Output:
# Students with marks > 80 and age < 23

# ============================================================
# MULTIPLE CONDITIONS USING |
# ============================================================

print(
    df[
        (df["Marks"] > 90) |
        (df["Age"] < 20)
    ]
)

# Output:
# Marks > 90 OR age < 20

# ============================================================
# USING NOT (~)
# ============================================================

print(
    df[
        ~(df["Marks"] > 80)
    ]
)

# Output:
# Marks NOT greater than 80

# ============================================================
# FILTERING SPECIFIC COLUMNS
# ============================================================

print(
    df.loc[
        df["Marks"] > 80,
        ["Name", "Marks"]
    ]
)

# ============================================================
# FILTERING WITH loc[]
# ============================================================

result = df.loc[df["Marks"] > 80]

print(result)

# ============================================================
# FILTERING USING isin()
# ============================================================

print(
    df[
        df["Name"].isin(
            ["Amit", "Priya"]
        )
    ]
)

# Output:
# Rows containing Amit or Priya

# ============================================================
# FILTERING USING BETWEEN
# ============================================================

print(
    df[
        df["Marks"].between(80, 95)
    ]
)

# Output:
# Marks between 80 and 95

# ============================================================
# FILTERING STRINGS
# ============================================================

print(
    df[
        df["Name"].str.startswith("P")
    ]
)

# Output:
# Names starting with P

# ============================================================
# CONTAINS STRING
# ============================================================

print(
    df[
        df["Name"].str.contains("a")
    ]
)

# Output:
# Names containing "a"

# ============================================================
# FILTERING NULL VALUES
# ============================================================

data = {
    "Name": ["Amit", "Rahul", None],
    "Marks": [90, None, 95]
}

df = pd.DataFrame(data)

print(df)

print(df[df["Marks"].isnull()])

# Rows with missing marks

# ============================================================
# FILTERING NON-NULL VALUES
# ============================================================

print(df[df["Marks"].notnull()])

# Rows having marks

# ============================================================
# FILTERING TOP SCORERS
# ============================================================

data = {
    "Name": ["Amit", "Rahul", "Priya"],
    "Marks": [90, 75, 95]
}

df = pd.DataFrame(data)

print(df[df["Marks"] == df["Marks"].max()])

# ============================================================
# FILTERING MULTIPLE COLUMNS
# ============================================================

data = {
    "Name": ["Amit", "Rahul", "Priya"],
    "Marks": [90, 75, 95],
    "Age": [21, 22, 20]
}

df = pd.DataFrame(data)

print(
    df[
        ["Name", "Marks"]
    ]
)

# ============================================================
# QUERY METHOD
# ============================================================

df = pd.DataFrame({
    "Name": ["Amit", "Rahul", "Priya"],
    "Marks": [90, 75, 95]
})

print(
    df.query("Marks > 80")
)

# ============================================================
# FILTERING USING MULTIPLE QUERY CONDITIONS
# ============================================================

df = pd.DataFrame({
    "Name": ["Amit", "Rahul", "Priya"],
    "Marks": [90, 75, 95],
    "Age": [21, 22, 20]
})

print(
    df.query(
        "Marks > 80 and Age < 22"
    )
)

# ============================================================
# PRACTICAL EXAMPLE 1
# STUDENT FILTERING
# ============================================================

students = pd.DataFrame({
    "Name": ["Amit", "Rahul", "Priya"],
    "Marks": [90, 75, 95]
})

top_students = students[
    students["Marks"] > 80
]

print(top_students)

# ============================================================
# PRACTICAL EXAMPLE 2
# EMPLOYEE DATA
# ============================================================

employees = pd.DataFrame({
    "Name": ["John", "Sara", "Mike"],
    "Salary": [50000, 70000, 60000]
})

high_salary = employees[
    employees["Salary"] > 55000
]

print(high_salary)

# ============================================================
# PRACTICAL EXAMPLE 3
# SALES DATA
# ============================================================

sales = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar"],
    "Sales": [1000, 2000, 1500]
})

print(
    sales[
        sales["Sales"] > 1200
    ]
)

# ============================================================
# SUMMARY
# ============================================================

print("""
PANDAS FILTERING SUMMARY

Basic Filtering:

df[df["Marks"] > 80]

Comparison Operators:

>
<
>=
<=
==
!=

Multiple Conditions:

&
|
~

Useful Methods:

isin()
between()
query()

String Filtering:

str.startswith()
str.contains()

Null Filtering:

isnull()
notnull()

Column Selection:

df[["Name","Marks"]]

Benefits:

✔ Extract Specific Data
✔ Easy Data Cleaning
✔ Better Data Analysis
✔ Essential for Data Science
✔ Frequently Used in Projects
""")
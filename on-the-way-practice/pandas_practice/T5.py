"""Task 5: CSV Cleaning Project

Create a CSV manually:


Questions
Read the CSV.
Detect missing values.
Fill missing age with average age.
Fill missing city with "Unknown".
Save cleaned data to a new CSV.

Concepts: Reading Files, Missing Values, Data Cleaning"""

import pandas as pd

df=pd.read_csv("students.csv")

print(df)

print(df.isna())

print(df.isna().sum())

df["Age"]=df["Age"].fillna(df["Age"].mean())
df["City"]=df["City"].fillna("Unknown")

print(df)

df.to_csv("students.csv",index=False)
"""Task 2: Student Marks

Create:

students = {
    "Name": ["A", "B", "C", "D", "E"],
    "Math": [90, 75, 85, 60, 95],
    "Science": [80, 70, 88, 65, 92]
}
Questions
Create a column Total.
Create a column Percentage.
Find students with percentage above 80.
Sort students by percentage descending.

Concepts: DataFrame operations, Filtering, Sorting"""

import pandas as pd

students = {
    "Name": ["A", "B", "C", "D", "E"],
    "Math": [90, 75, 85, 60, 95],
    "Science": [80, 70, 88, 65, 92]
}

df=pd.DataFrame(students)
print(df)

df["Total"]=df["Math"]+df["Science"]
df["Percentage"]=(df["Total"]/200)*100

print(df)

print(df[df["Percentage"]>80])

print(df.sort_values(by="Percentage", ascending=False,ignore_index=True))
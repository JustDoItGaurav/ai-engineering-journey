"""Task 9: Advanced Filtering

Questions
Employees age > 30.
Employees salary between 60k and 80k.
Employees age > 30 and salary > 70k.
Employees age < 30 or salary > 80k.

Concepts: Boolean Filtering"""

import pandas as pd

employees = {
    "Name": ["John", "Alice", "Bob", "Emma", "Mike"],
    "Age": [25, 32, 28, 45, 38],
    "Salary": [50000, 70000, 60000, 90000, 75000]
}

df=pd.DataFrame(employees)

print(df)

print(df[df["Age"]>30])

print(df[(df["Salary"] > 60000) & (df["Salary"] < 80000)])

print(df[(df["Age"]>30) & (df["Salary"]>70000)])

print(df[(df["Age"]<30) | (df["Salary"]>80000)])
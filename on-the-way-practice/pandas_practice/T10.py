"""Task 10: Mini End-to-End Project 🚀

Questions
Read both files.
Merge them.
Find average salary by department.
Find highest-paid employee.
Add Bonus column (10% of salary).
Check for missing values.
Save final report as CSV.

Concepts Covered: Reading Files + Merge + GroupBy + Filtering + Cleaning"""

import pandas as pd

emp_df=pd.read_csv("employees.csv")
dept_df=pd.read_csv("department.csv")

merged=pd.merge(
    emp_df,
    dept_df,
    on="DeptID"
)

print(merged)

merged["Average Salary"]=(merged.groupby("Department")["Salary"].transform("mean"))

print(merged)

print(merged.loc[merged["Salary"].idxmax(),"Name"])

merged["Bonus"]=merged["Salary"]*0.1

print(merged)

print(merged.isna())

merged.to_csv("final_report.csv",index=False)


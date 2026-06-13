"""Task 8: E-commerce Analysis

Questions
Total revenue.
Revenue by category.
Highest earning category.
Percentage contribution of each category.

Concepts: GroupBy, Calculations"""

import pandas as pd

orders = {
    "Category": ["Electronics", "Clothing", "Electronics",
                 "Furniture", "Clothing"],
    "Amount": [500, 100, 800, 300, 150]
}

df=pd.DataFrame(orders)
print(df)

print(f"Total Revenue:{df["Amount"].sum()}")

print(df.groupby("Category")["Amount"].sum())

print(df.groupby("Category")["Amount"].sum().idxmax())

heyhey=df.groupby("Category")["Amount"].sum().reset_index()

heyhey["Percentage"]=((heyhey["Amount"]/heyhey["Amount"].sum())*100).round(2)

print(heyhey)





"""Task 6: Customer Orders (Merge)

Questions
Merge both DataFrames.
Calculate total spending per customer.
Find highest spending customer.

Concepts: Merging, GroupBy"""

import pandas as pd

df_customers=pd.read_csv("customers.csv")
df_orders=pd.read_csv("orders.csv")

print(df_customers)
print(df_orders)

merged=pd.merge(
    df_customers,
    df_orders,
    on="CustomerID"
)

print(merged)

totalspending=merged.groupby("Name")["OrderAmount"].sum()
print(totalspending)

print(totalspending.idxmax())
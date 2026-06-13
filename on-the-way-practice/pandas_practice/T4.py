"""Task 4: Sales Analysis

Questions
Total sales by product.
Total sales by region.
Product with highest sales.
Average sales per product.

Concepts: GroupBy"""

import pandas as pd

sales = {
    "Product": ["Laptop", "Phone", "Laptop", "Tablet", "Phone"],
    "Region": ["East", "West", "East", "North", "West"],
    "Sales": [1000, 500, 1500, 800, 700]
}

df=pd.DataFrame(sales)

print(df.groupby("Product")["Sales"].sum())
print(df.groupby("Region")["Sales"].sum())

product_sales = df.groupby("Product")["Sales"].sum()

print(product_sales)
print("\nProduct with highest sales:")
print(product_sales.idxmax())

print(df.groupby("Product")["Sales"].mean())
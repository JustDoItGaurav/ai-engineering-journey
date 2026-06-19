"""Data
categories = ["Food", "Rent", "Transport", "Shopping", "Entertainment"]
expenses = [12000, 25000, 5000, 8000, 4000]
Requirements
Create a bar chart.
Use different colors for bars.
Display expense values on top.
Concepts Practiced

✅ Bar Chart
✅ Text Annotations"""

import matplotlib.pyplot as plt

categories = ["Food", "Rent", "Transport", "Shopping", "Entertainment"]
expenses = [12000, 25000, 5000, 8000, 4000]

colours=["red","green","blue","yellow","pink"]

bars=plt.bar(
    categories,
    expenses,
    color=colours,
    edgecolor="black"
)

plt.title("Total Expenditure")
plt.xlabel("Categories")
plt.ylabel("Expenses")

for bar in bars:
    height=bar.get_height()
    plt.text(
        bar.get_x()+bar.get_width()/2,
        height+300,
        str(height),
        ha="center"
    )


plt.show()
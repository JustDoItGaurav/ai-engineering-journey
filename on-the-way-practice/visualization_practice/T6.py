"""Data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [200, 250, 300, 280, 350, 400]
profit = [50, 60, 80, 75, 100, 120]
Requirements

Create 2 subplots:

Sales line chart
Profit bar chart
Concepts Practiced

✅ Subplots
✅ Line Plot
✅ Bar Chart"""

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [200, 250, 300, 280, 350, 400]
profit = [50, 60, 80, 75, 100, 120]

plt.subplot(1,2,1)

plt.plot(
    months,
    sales,
    linewidth=2,
    linestyle="--",
    color="red",
    marker="o"
)

plt.title("Sales Chart")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.subplot(1,2,2)

plt.bar(
    months,
    profit,
    color="green",
    edgecolor="black"
)

plt.title("Profit Chart")
plt.xlabel("Months")
plt.ylabel("Profit")

plt.suptitle("Subplots")

plt.tight_layout()

plt.show()


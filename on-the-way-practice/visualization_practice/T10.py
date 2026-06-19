"""Task 10: Mini Data Analytics Dashboard (Project)

Generate:

import numpy as np

days = np.arange(1, 31)

temperature = np.random.randint(20, 40, 30)
sales = np.random.randint(100, 500, 30)
customers = np.random.randint(50, 200, 30)
Requirements

Create a 2x2 subplot dashboard:

Temperature Line Plot
Sales Bar Chart
Customers Histogram
Sales vs Customers Scatter Plot

Add:

Figure title
Axis labels
Grid where needed
Tight layout
Concepts Practiced

✅ Everything you've learned"""

import matplotlib.pyplot as plt

import numpy as np

days = np.arange(1, 31)

temperature = np.random.randint(20, 40, 30)
sales = np.random.randint(100, 500, 30)
customers = np.random.randint(50, 200, 30)

plt.subplot(2,2,1)

plt.plot(
    days,
    temperature,
    color="red",
    linestyle="--"
)

plt.title("Temperature Chart")
plt.xlabel("Days")
plt.ylabel("Temperature")

plt.subplot(2,2,2)

plt.bar(
    days,
    sales,
    color="orange",
    edgecolor="black"
)

plt.title("Sales Chart")
plt.xlabel("Days")
plt.ylabel("Sales")

plt.grid(True)

plt.subplot(2,2,3)

plt.hist(
    customers,
    bins=15,
    color="yellow",
    edgecolor="black"
)

plt.title("Customers Chart")
plt.xlabel("Customers")
plt.ylabel("Frequency")

plt.grid(True)

plt.subplot(2,2,4)

plt.scatter(
    customers,
    sales,
    marker="o",
    color="purple"
)

plt.title("Distribution Chart")
plt.xlabel("Customers")
plt.ylabel("Sales")

plt.suptitle("Mini Project Dashboard",fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.95])

plt.show()
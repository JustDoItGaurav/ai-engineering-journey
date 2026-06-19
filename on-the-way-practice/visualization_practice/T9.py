"""Task 9: Sales Data Explorer

Generate data:

import numpy as np

sales = np.random.randint(100, 1000, 100)
Requirements

Create a figure with:

Histogram of sales
Line plot of sales trend
Bar chart of first 10 sales
Concepts Practiced

✅ Histogram
✅ Line Plot
✅ Bar Chart
✅ Subplots"""

import numpy as np
import matplotlib.pyplot as plt

sales = np.random.randint(100, 1000, 100)

plt.subplot(2,2,1)

plt.hist(
    sales,
    bins=15,
    edgecolor="black"
    )

plt.subplot(2,2,2)

plt.plot(sales)

plt.subplot(2,2,3)

plt.bar(range(10),sales[:10])

plt.tight_layout()

plt.show()


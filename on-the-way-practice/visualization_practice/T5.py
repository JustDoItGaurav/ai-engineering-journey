"""Generate random heights:

import numpy as np

heights = np.random.normal(170, 10, 500)
Requirements
Create a histogram.
Use 15 bins.
Add grid.
Display title.
Concepts Practiced

✅ Histogram
✅ Understanding Distribution"""

import numpy as np
import matplotlib.pyplot as plt

heights = np.random.normal(170, 10, 500)

plt.hist(heights,
         bins=15,
         edgecolor="black"
         )

plt.grid(True)

plt.title("Random Heights")

plt.show()
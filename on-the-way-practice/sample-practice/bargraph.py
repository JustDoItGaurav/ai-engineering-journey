import matplotlib.pyplot as plt
import numpy as np

subjects = ["Math", "Science", "English"]
boys_marks = [90, 85, 95]
girls_marks = [88, 92, 96]

x = np.arange(len(subjects))
width = 0.35

plt.bar(x - width/2, boys_marks, width, label="Boys")
plt.bar(x + width/2, girls_marks, width, label="Girls")

plt.xticks(x, subjects)
plt.legend()
plt.show()
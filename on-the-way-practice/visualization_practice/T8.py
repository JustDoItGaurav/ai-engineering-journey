"""Data
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

steps = [5000, 7000, 8000, 6500, 9000, 12000, 10000]
calories = [220, 250, 300, 240, 350, 450, 400]
Requirements

Create 2 subplots:

Steps (Line Plot)
Calories Burned (Bar Chart)
Bonus

Share x-axis between subplots.

Concepts Practiced

✅ Subplots
✅ Line Plot
✅ Bar Chart"""

import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

steps = [5000, 7000, 8000, 6500, 9000, 12000, 10000]
calories = [220, 250, 300, 240, 350, 450, 400]

plt.subplot(2,1,1)

plt.plot(
    days,
    steps,
)

plt.subplot(2,1,2)

plt.bar(
    days,
    calories
)

plt.tight_layout()

plt.show()
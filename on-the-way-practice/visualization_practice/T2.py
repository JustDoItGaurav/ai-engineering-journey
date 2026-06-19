"""Data
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temp = [28, 30, 31, 29, 33, 35, 32]
Requirements
Create a line plot.
Use markers.
Add grid.
Change line style.
Concepts Practiced

✅ Line Plot
✅ Customizations"""

import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temp = [28, 30, 31, 29, 33, 35, 32]

markers=plt.plot(
    days,
    temp,
    linestyle="--",
    linewidth=2,
    color="green",
    marker="*"
)

plt.grid(True)

for day, temperature in zip(days, temp):
    plt.text(
        day,
        temperature + 0.5,
        str(temperature),
        ha="center"
    )

plt.tight_layout()


plt.show()
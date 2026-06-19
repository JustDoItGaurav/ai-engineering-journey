"""Data
subjects = ["Math", "Science", "English", "History", "Computer"]
marks = [85, 92, 78, 88, 95]
Requirements
Create a bar chart.
Add title.
Add x-axis and y-axis labels.
Show marks above each bar.
Concepts Practiced

✅ Matplotlib Basics
✅ Bar Chart"""

import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English", "History", "Computer"]
marks = [85, 92, 78, 88, 95]

bars=plt.bar(
    subjects,
    marks,
    edgecolor="black"
)

plt.title("Students Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

for bar in bars:
    height=bar.get_height()
    plt.text(
        bar.get_x()+bar.get_width()/2,
        height+1,
        str(height),
        ha="center"
    )

plt.show()
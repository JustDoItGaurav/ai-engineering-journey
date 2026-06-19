"""Data
    study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
    scores = [45, 50, 55, 60, 68, 75, 85, 92]
    Requirements
    Create a scatter plot.
    Customize marker size.
    Add title and labels.
    Observe the relationship.
    Concepts Practiced

    ✅ Scatter Plot
    ✅ Data Relationships"""

import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [45, 50, 55, 60, 68, 75, 85, 92]

plt.scatter(
    study_hours,
    scores,
    s=200,
    marker="s",
    color="green"
)

plt.title("Study Hour Relationship")
plt.xlabel("Study Hours")
plt.ylabel("Scores")

plt.show()
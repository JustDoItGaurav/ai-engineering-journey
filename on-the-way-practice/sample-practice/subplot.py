import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 180, 170, 220, 250]

subjects = ["Math", "Science", "English", "History"]
marks = [90, 85, 95, 80]

scores = [45, 50, 55, 60, 62, 65, 68, 70, 72, 75,
          78, 80, 82, 85, 88, 90, 92, 95, 98]

study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
marks1 = [40, 50, 55, 65, 70, 78, 85, 92]

plt.subplot(2,2,1)

plt.plot(
    months,
    sales,
    color="red",
    linestyle="--"
)

plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Line Chart")

plt.subplot(2,2,2)

plt.bar(
    subjects,
    marks,
    color="green"
)

plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Bar Chart")

plt.subplot(2,2,3)

plt.hist(
    scores,
    bins=5,
    edgecolor="black"
)
plt.xlabel("x-axis")
plt.ylabel("Scores")
plt.title("Histogram")

plt.subplot(2,2,4)

plt.scatter(
    study_hours,
    marks1,
    marker="*",
    color="yellow"
)

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Scatter Plot")

plt.tight_layout()

plt.show()








import matplotlib.pyplot as plt


def line_and_scatter():
    x = [1, 2, 3, 4, 5, 6, 7]
    y = [2, 5, 10, 17, 26, 37, 50]

    plt.plot(
        x,
        y,
        color="red",
        linewidth=4,
        linestyle="--",
        marker="o",
        label="Quadratic Growth"
    )

    plt.scatter(x, y)

    plt.title("Gaurav Imagination")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.legend()
    plt.grid(True)

    plt.show()


def bar_chart():
    subjects = ["Math", "Science", "English"]
    marks = [90, 85, 95]

    plt.barh(subjects, marks)

    plt.title("Student Marks")
    plt.xlabel("Marks")
    plt.ylabel("Subjects")

    plt.show()


def histogram():
    data = [10, 20, 20, 30, 40, 40, 40, 50]

    plt.hist(
        data,
        bins=5,
        edgecolor="black"
    )

    plt.title("Histogram Example")
    plt.xlabel("Values")
    plt.ylabel("Frequency")

    plt.show()


def pie_chart():
    labels = ["Python", "Java", "C++"]
    sizes = [50, 30, 20]

    plt.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%"
    )

    plt.title("Programming Language Usage")

    plt.savefig("pie.png")
    plt.show()


# Run whichever chart you want
pie_chart()
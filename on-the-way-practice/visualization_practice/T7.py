"""Data
followers = [100, 150, 250, 400, 600, 850]
posts = [5, 8, 12, 20, 25, 30]
Requirements
Create scatter plot.
Add annotations showing follower counts.
Use custom marker colors.
Concepts Practiced

✅ Scatter Plot
✅ Annotations"""

import matplotlib.pyplot as plt

followers = [100, 150, 250, 400, 600, 850]
posts = [5, 8, 12, 20, 25, 30]

colors = ["red", "blue", "green", "orange", "purple", "brown"]

plt.scatter(
    followers,
    posts,
    color=colors,
    s=100
)

# Add annotations showing follower counts
for x, y in zip(followers, posts):
    plt.annotate(
        str(x),
        (x, y),
        textcoords="offset points",
        xytext=(5, 5)
    )

plt.title("Followers vs Posts")
plt.xlabel("Followers")
plt.ylabel("Posts")

plt.show()
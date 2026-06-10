import numpy as np

students = np.array([
    [85, 90, 78],
    [88, 76, 95],
    [92, 89, 80],
    [70, 65, 75],
    [95, 98, 92]
])

print(students.mean(axis=1))
print(students.mean(axis=0))

student_avg=students.mean(axis=1)
print(student_avg.argmax())

subject_avg=students.mean(axis=0)
print(subject_avg.argmax())

overall_avg=student_avg.mean()
highscore=student_avg[student_avg>overall_avg]
print(highscore)



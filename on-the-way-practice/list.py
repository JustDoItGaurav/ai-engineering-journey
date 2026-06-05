marks=[]
students=int(input("Enter number of students:"))
for i in range (1,students+1):
    mark=int(input(f"Enter marks of student {i}:"))
    marks.append(mark)



sum=0
maximum=0
minimum=100

for mark in marks:
    sum=sum+mark
    maximum=max(mark,maximum)
    minimum=min(mark,minimum)

print(marks)

print(f"max:{maximum}|min:{minimum}|average:{sum/students}")

print("Passed students:")
count=0
for mark in marks:
    if mark>=40:
        print(mark)
        count+=1

print(f"Total passed students:{count}")

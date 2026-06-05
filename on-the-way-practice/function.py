"""def area(length,breadth):
    return length*breadth


def perimeter(length,breadth):
    return 2 * (length + breadth)

def is_square(length,breadth):
    if(length==breadth):
        print("Its is a square")
    else:
        print("It is not a square")

l=int(input("Enter length of rectangle:"))
b=int(input("Enter breadth of rectangle:"))

print("Area of rectangle is",area(l,b))
print("Perimeter of rectangle is",perimeter(l,b))
is_square(l,b)
def list_average(numbers):
    sum=0
    for num in numbers:
        sum+=num
    return sum/len(numbers)


numbers=[10,20,30,40,50]

print("Average of the list is",list_average(numbers))"""

def average_marks(marks):
    return sum(marks)/len(marks)

def highest_marks(marks):
    return max(marks)

def passed_students(marks):
    passed=[]
    for mark in marks:
        if mark>=40:
            passed.append(mark)
    
    return passed

def grade(marks):
    i=1
    for mark in marks:
        if mark>=90:
            print(f" Student {i} got grade A with {mark} marks")
        elif mark>=70:
            print(f" Student {i} got grade B with {mark} marks")
        else:
            print(f" Student {i} got grade C with {mark} marks")
    i+=1

marks=[]

for i in range(1,5+1):
    mark=int(input(f"Enter marks of student {i}: "))
    marks.append(mark)

print("Marks of students:",marks)
print("Average marks:",average_marks(marks))
print("Highest marks:",highest_marks(marks))
print("Passed students:",passed_students(marks))
grade(marks)



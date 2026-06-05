age=int(input("Enter your age:"))

if age==0 or age<0:
    print("Invalid age")
elif age<13:
    print("Child Ticket")
elif age>13 and age<60:
    print("Adult Ticket")
else:
    print("Senior Citizen Ticket")
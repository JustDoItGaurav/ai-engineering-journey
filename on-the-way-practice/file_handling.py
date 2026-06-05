"""file=open("students.txt","x")
file.close()"""

"""with open("students.txt","w") as file:
    file.write("Gaurav-43")
    file.write("\n")
    file.write("Ujwal-46")"""

"""with open("students.txt","a") as file:
    file.write("\n")
    file.write("Dheeraj-23")"""

"""with open("students.txt","r") as file:
    content=file.read()
    print(content)"""

with open ("students.txt","r") as file:
    content=file.readline()
    print(content)
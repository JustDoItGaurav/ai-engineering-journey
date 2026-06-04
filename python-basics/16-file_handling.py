# ============================================================
# FILE HANDLING IN PYTHON
# ============================================================

# File handling is used to:
# - Create files
# - Read files
# - Write files
# - Append data to files

# ============================================================
# OPENING A FILE
# ============================================================

# Syntax:
# open("filename", "mode")

# Common Modes:
# "r" -> Read
# "w" -> Write (overwrites file)
# "a" -> Append
# "x" -> Create file
# "r+" -> Read and Write

# ============================================================
# WRITING TO A FILE
# ============================================================

file = open("sample.txt", "w")

file.write("Hello World\n")
file.write("Welcome to Python File Handling")

file.close()

print("Data written successfully.")

# ============================================================
# READING A FILE
# ============================================================

file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()

# ============================================================
# READING LINE BY LINE
# ============================================================

file = open("sample.txt", "r")

print(file.readline())
print(file.readline())

file.close()

# ============================================================
# READING ALL LINES
# ============================================================

file = open("sample.txt", "r")

lines = file.readlines()

print(lines)

file.close()

# ============================================================
# APPENDING DATA
# ============================================================

file = open("sample.txt", "a")

file.write("\nThis line was appended.")

file.close()

print("Data appended successfully.")

# ============================================================
# USING WITH STATEMENT (RECOMMENDED)
# ============================================================

# Automatically closes the file

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# ============================================================
# CREATING A NEW FILE
# ============================================================

# Uncomment to create a file

# file = open("newfile.txt", "x")
# file.close()

# ============================================================
# WRITING MULTIPLE LINES
# ============================================================

data = [
    "Python\n",
    "AI\n",
    "Machine Learning\n"
]

with open("topics.txt", "w") as file:
    file.writelines(data)

print("Multiple lines written successfully.")

# ============================================================
# PRACTICAL EXAMPLE 1
# SAVE USER DETAILS
# ============================================================

name = "Gaurav"
age = 21

with open("user.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")

print("User details saved.")

# ============================================================
# PRACTICAL EXAMPLE 2
# READ USER DETAILS
# ============================================================

with open("user.txt", "r") as file:
    print(file.read())

# ============================================================
# PRACTICAL EXAMPLE 3
# STORE MARKS
# ============================================================

marks = [85, 90, 78, 95]

with open("marks.txt", "w") as file:

    for mark in marks:
        file.write(f"{mark}\n")

print("Marks saved successfully.")

# ============================================================
# SUMMARY
# ============================================================

print("""
File Modes:

r  -> Read
w  -> Write
a  -> Append
x  -> Create
r+ -> Read and Write

Common Methods:

read()       -> Read entire file
readline()   -> Read one line
readlines()  -> Read all lines
write()      -> Write text
writelines() -> Write multiple lines

Best Practice:

with open("file.txt", "r") as file:
    data = file.read()

This automatically closes the file.
""")
# ============================================================
# CONTROL FLOW IN PYTHON
# ============================================================

# Control flow determines the order in which code executes.
# The main control flow statements are:
# 1. if, elif, else
# 2. for loop
# 3. while loop
# 4. break
# 5. continue

# ============================================================
# IF, ELIF, ELSE
# ============================================================

age = 21

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# ------------------------------------------------------------

marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")

# ============================================================
# FOR LOOPS
# ============================================================

# Looping through a range

for i in range(5):
    print(i)

# Output:
# 0 1 2 3 4

# ------------------------------------------------------------

# Looping through a list

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)

# ------------------------------------------------------------

# Looping through a string

for character in "Python":
    print(character)

# ------------------------------------------------------------

# Looping through a dictionary

student = {
    "name": "Gaurav",
    "age": 21
}

for key, value in student.items():
    print(key, ":", value)

# ============================================================
# WHILE LOOPS
# ============================================================

count = 1

while count <= 5:
    print(count)
    count += 1

# ============================================================
# BREAK
# ============================================================

for number in range(10):

    if number == 5:
        break

    print(number)

# Output:
# 0 1 2 3 4

# ============================================================
# CONTINUE
# ============================================================

for number in range(5):

    if number == 2:
        continue

    print(number)

# Output:
# 0 1 3 4

# ============================================================
# NESTED LOOPS
# ============================================================

for i in range(3):

    for j in range(2):

        print(f"i = {i}, j = {j}")

# ============================================================
# PRACTICAL EXAMPLES
# ============================================================

# Example 1: Print Even Numbers

for number in range(1, 11):

    if number % 2 == 0:
        print(number)

# ------------------------------------------------------------

# Example 2: Sum of Numbers

total = 0

for number in range(1, 6):
    total += number

print("Sum =", total)

# ------------------------------------------------------------

# Example 3: Password Check

password = "python123"

if password == "python123":
    print("Access Granted")
else:
    print("Access Denied")

# ============================================================
# SUMMARY
# ============================================================

print("""
Control Flow Statements:

if      -> Execute code if condition is True
elif    -> Check additional conditions
else    -> Execute when all conditions are False

for     -> Iterate over a sequence
while   -> Repeat while condition is True

break   -> Exit the loop immediately
continue-> Skip current iteration

range() -> Generate a sequence of numbers
""")
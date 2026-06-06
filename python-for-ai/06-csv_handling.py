# ============================================================
# CSV HANDLING IN PYTHON
# ============================================================

# CSV = Comma Separated Values
#
# CSV files are commonly used to store tabular data.
#
# Example:
#
# name,age,city
# Gaurav,21,Mumbai
# Rahul,22,Pune
#
# Python provides a built-in csv module to work with CSV files.

import csv

# ============================================================
# WRITING TO A CSV FILE
# ============================================================

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    # Header
    writer.writerow(["Name", "Age", "City"])

    # Data Rows
    writer.writerow(["Gaurav", 21, "Mumbai"])
    writer.writerow(["Rahul", 22, "Pune"])
    writer.writerow(["Priya", 20, "Delhi"])

print("CSV file created successfully.")

# ============================================================
# READING A CSV FILE
# ============================================================

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)

# ============================================================
# SKIPPING THE HEADER
# ============================================================

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    next(reader)  # Skip header row

    for row in reader:
        print(row)

# ============================================================
# ACCESSING INDIVIDUAL VALUES
# ============================================================

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    next(reader)

    for row in reader:

        name = row[0]
        age = row[1]
        city = row[2]

        print(name, age, city)

# ============================================================
# WRITING MULTIPLE ROWS
# ============================================================

students = [
    ["Amit", 23, "Mumbai"],
    ["Neha", 22, "Pune"],
    ["Riya", 21, "Delhi"]
]

with open("students_data.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "City"])

    writer.writerows(students)

print("Multiple rows written successfully.")

# ============================================================
# USING DICTIONARIES
# ============================================================

with open("employees.csv", "w", newline="") as file:

    fieldnames = ["Name", "Age", "Department"]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    writer.writerow({
        "Name": "Gaurav",
        "Age": 21,
        "Department": "Engineering"
    })

    writer.writerow({
        "Name": "Rahul",
        "Age": 22,
        "Department": "IT"
    })

print("Dictionary CSV created.")

# ============================================================
# READING CSV AS DICTIONARY
# ============================================================

with open("employees.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        print(row["Name"])
        print(row["Department"])

# ============================================================
# PRACTICAL EXAMPLE
# CALCULATE AVERAGE MARKS
# ============================================================

with open("marks.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name", "Marks"])

    writer.writerow(["Gaurav", 85])
    writer.writerow(["Rahul", 90])
    writer.writerow(["Priya", 95])

total_marks = 0
count = 0

with open("marks.csv", "r") as file:

    reader = csv.reader(file)

    next(reader)

    for row in reader:

        total_marks += int(row[1])
        count += 1

average = total_marks / count

print("Average Marks:", average)

# ============================================================
# SUMMARY
# ============================================================

print("""
CSV Module Functions:

csv.reader()      -> Read CSV files
csv.writer()      -> Write CSV files

csv.DictReader()  -> Read as dictionary
csv.DictWriter()  -> Write using dictionary

Common Methods:

writerow()   -> Write one row
writerows()  -> Write multiple rows

Best Practice:

with open("file.csv", "r") as file:
    reader = csv.reader(file)

with open("file.csv", "w", newline="") as file:
    writer = csv.writer(file)
""")
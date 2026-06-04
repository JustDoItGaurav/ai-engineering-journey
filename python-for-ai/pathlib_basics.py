# ============================================================
# PATHLIB BASICS IN PYTHON
# ============================================================

# pathlib is the modern way to work with files and folders.
# It provides an object-oriented approach for handling paths.

from pathlib import Path

# ============================================================
# CREATE A PATH OBJECT
# ============================================================

file_path = Path("data.txt")

print(file_path)
print(type(file_path))

# ============================================================
# CURRENT WORKING DIRECTORY
# ============================================================

current_directory = Path.cwd()

print(current_directory)

# ============================================================
# HOME DIRECTORY
# ============================================================

home_directory = Path.home()

print(home_directory)

# ============================================================
# CHECK IF FILE EXISTS
# ============================================================

file_path = Path("data.txt")

print(file_path.exists())

# Output:
# True or False

# ============================================================
# CHECK IF PATH IS A FILE
# ============================================================

print(file_path.is_file())

# ============================================================
# CHECK IF PATH IS A DIRECTORY
# ============================================================

folder_path = Path("my_folder")

print(folder_path.is_dir())

# ============================================================
# GET FILE NAME
# ============================================================

file_path = Path("documents/report.pdf")

print(file_path.name)

# Output:
# report.pdf

# ============================================================
# GET FILE STEM
# ============================================================

print(file_path.stem)

# Output:
# report

# ============================================================
# GET FILE EXTENSION
# ============================================================

print(file_path.suffix)

# Output:
# .pdf

# ============================================================
# GET PARENT DIRECTORY
# ============================================================

print(file_path.parent)

# Output:
# documents

# ============================================================
# JOIN PATHS
# ============================================================

folder = Path("data")

file = folder / "students.csv"

print(file)

# Output:
# data/students.csv

# ============================================================
# CREATE A DIRECTORY
# ============================================================

new_folder = Path("new_folder")

new_folder.mkdir(exist_ok=True)

print("Folder created successfully.")

# ============================================================
# CREATE NESTED DIRECTORIES
# ============================================================

nested_folder = Path("projects/python/data")

nested_folder.mkdir(
    parents=True,
    exist_ok=True
)

print("Nested folders created.")

# ============================================================
# CREATE A FILE
# ============================================================

file_path = Path("sample.txt")

file_path.touch(exist_ok=True)

print("File created.")

# ============================================================
# WRITE TO A FILE
# ============================================================

file_path = Path("sample.txt")

file_path.write_text(
    "Hello World"
)

print("Text written successfully.")

# ============================================================
# READ FROM A FILE
# ============================================================

content = file_path.read_text()

print(content)

# ============================================================
# LIST FILES IN CURRENT DIRECTORY
# ============================================================

current_directory = Path(".")

for item in current_directory.iterdir():
    print(item)

# ============================================================
# FIND ALL PYTHON FILES
# ============================================================

for file in Path(".").glob("*.py"):
    print(file)

# ============================================================
# RECURSIVE SEARCH
# ============================================================

for file in Path(".").rglob("*.py"):
    print(file)

# ============================================================
# DELETE A FILE
# ============================================================

temp_file = Path("temp.txt")

temp_file.touch(exist_ok=True)

temp_file.unlink()

print("File deleted.")

# ============================================================
# PRACTICAL EXAMPLE 1
# CREATE PROJECT STRUCTURE
# ============================================================

project_folder = Path("my_project")

project_folder.mkdir(exist_ok=True)

(project_folder / "data").mkdir(exist_ok=True)
(project_folder / "models").mkdir(exist_ok=True)
(project_folder / "logs").mkdir(exist_ok=True)

print("Project structure created.")

# ============================================================
# PRACTICAL EXAMPLE 2
# SAVE LOG FILE
# ============================================================

log_file = Path("logs.txt")

log_file.write_text(
    "Application Started"
)

print(log_file.read_text())

# ============================================================
# PRACTICAL EXAMPLE 3
# CHECK DATASET FILE
# ============================================================

dataset = Path("dataset.csv")

if dataset.exists():
    print("Dataset Found")
else:
    print("Dataset Not Found")

# ============================================================
# SUMMARY
# ============================================================

print("""
Common Pathlib Methods:

Path()
Path.cwd()
Path.home()

exists()
is_file()
is_dir()

mkdir()
touch()

write_text()
read_text()

iterdir()
glob()
rglob()

unlink()

Useful Properties:

name
stem
suffix
parent

Benefits:

✔ Modern File Handling
✔ Cross Platform
✔ Cleaner Syntax
✔ Widely Used in AI/Data Science
""")
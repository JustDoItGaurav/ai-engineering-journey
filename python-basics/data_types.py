# ============================================================
# PYTHON DATA TYPES
# ============================================================

# ------------------------------------------------------------
# INTEGER (int)
# Whole numbers
# ------------------------------------------------------------

user_age = 21

print(user_age)
print(type(user_age))

# ------------------------------------------------------------
# FLOAT (float)
# Decimal numbers
# ------------------------------------------------------------

user_height = 5.8

print(user_height)
print(type(user_height))

# ------------------------------------------------------------
# STRING (str)
# Text enclosed in quotes
# ------------------------------------------------------------

user_name = "Gaurav"

print(user_name)
print(type(user_name))

# ------------------------------------------------------------
# BOOLEAN (bool)
# True or False values
# ------------------------------------------------------------

is_student = True

print(is_student)
print(type(is_student))

# ------------------------------------------------------------
# USING VARIABLES TOGETHER
# ------------------------------------------------------------

print("Name:", user_name)
print("Age:", user_age)
print("Height:", user_height)
print("Student:", is_student)

# ------------------------------------------------------------
# F-STRING FORMATTING
# Modern way to combine variables and text
# ------------------------------------------------------------

message = f"Hello, I am {user_name} and I am {user_age} years old."

print(message)
print(type(message))

# ------------------------------------------------------------
# TYPE CONVERSION (CASTING)
# Converting one data type to another
# ------------------------------------------------------------

age_string = "21"

print(age_string)
print(type(age_string))

converted_age = int(age_string)

print(converted_age)
print(type(converted_age))

# Integer to Float
number = 10

float_number = float(number)

print(float_number)
print(type(float_number))

# Integer to String
number_text = str(number)

print(number_text)
print(type(number_text))

# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

print("""
Common Data Types:

int   -> Whole numbers
float -> Decimal numbers
str   -> Text/String
bool  -> True or False
""")
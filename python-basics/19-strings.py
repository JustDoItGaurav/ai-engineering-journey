# ============================================================
# PYTHON STRING METHODS CHEAT SHEET
# A single file demonstrating commonly used string operations
# ============================================================

# Original string
text = "Gaurav is 21 years old. He is in Pillai College of Engineering."

# ------------------------------------------------------------
# PRINTING THE STRING
# ------------------------------------------------------------

print("Original String:")
print(text)

# ------------------------------------------------------------
# CHANGING CASE
# ------------------------------------------------------------

print("\n--- Case Conversion ---")

print(text.upper())       # Convert all characters to uppercase
print(text.lower())       # Convert all characters to lowercase
print(text.capitalize())  # Capitalize only the first character
print(text.title())       # Capitalize the first letter of every word
print(text.swapcase())    # Convert uppercase to lowercase and vice versa

# ------------------------------------------------------------
# REPLACING TEXT
# ------------------------------------------------------------

print("\n--- Replace ---")

print(text.replace("21", "20"))  # Replace "21" with "20"

# ------------------------------------------------------------
# STRING LENGTH
# ------------------------------------------------------------

print("\n--- Length ---")

print(len(text))  # Total number of characters including spaces

# ------------------------------------------------------------
# SPLITTING STRINGS
# ------------------------------------------------------------

print("\n--- Split ---")

# Split the string into words using spaces
words = text.split()

print(words)

# ------------------------------------------------------------
# JOINING STRINGS
# ------------------------------------------------------------

print("\n--- Join ---")

word_list = ["Python", "AI", "Machine", "Learning"]

joined_text = " ".join(word_list)

print(joined_text)

# ------------------------------------------------------------
# FINDING TEXT
# ------------------------------------------------------------

print("\n--- Find ---")

# Returns the index of first occurrence
print(text.find("21"))

# Returns -1 if not found
print(text.find("100"))

# ------------------------------------------------------------
# COUNTING OCCURRENCES
# ------------------------------------------------------------

print("\n--- Count ---")

sample = "apple apple banana apple"

print(sample.count("apple"))

# ------------------------------------------------------------
# REMOVING SPACES
# ------------------------------------------------------------

print("\n--- Strip ---")

name = "   Gaurav   "

print(name.strip())   # Remove spaces from both sides
print(name.lstrip())  # Remove spaces from left side
print(name.rstrip())  # Remove spaces from right side

# ------------------------------------------------------------
# CHECKING STRING CONTENTS
# ------------------------------------------------------------

print("\n--- Validation Methods ---")

print("123".isdigit())     # True if all characters are digits
print("Gaurav".isalpha())  # True if all characters are letters
print("abc123".isalnum())  # True if letters and numbers only
print("HELLO".isupper())   # True if all uppercase
print("hello".islower())   # True if all lowercase

# ------------------------------------------------------------
# STARTS WITH / ENDS WITH
# ------------------------------------------------------------

print("\n--- Startswith / Endswith ---")

print(text.startswith("Gaurav"))
print(text.endswith("Engineering."))

# ------------------------------------------------------------
# STRING INDEXING
# ------------------------------------------------------------

print("\n--- Indexing ---")

name = "Gaurav"

print(name[0])   # First character
print(name[1])   # Second character
print(name[-1])  # Last character

# ------------------------------------------------------------
# STRING SLICING
# ------------------------------------------------------------

print("\n--- Slicing ---")

print(name[0:3])   # Characters from index 0 to 2
print(name[:4])    # First 4 characters
print(name[2:])    # From index 2 to end
print(name[::-1])  # Reverse the string

# ------------------------------------------------------------
# F-STRINGS (MOST COMMON IN MODERN PYTHON)
# ------------------------------------------------------------

print("\n--- f-Strings ---")

person_name = "Gaurav"
age = 21

message = f"{person_name} is {age} years old."

print(message)

# ------------------------------------------------------------
# PRACTICAL DATA CLEANING EXAMPLE
# ------------------------------------------------------------

print("\n--- Data Cleaning Example ---")

raw_text = "   Machine Learning Is Awesome   "

clean_text = raw_text.strip().lower()

print(clean_text)

# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

print("\n--- Commonly Used Methods ---")

print("""
.upper()       -> Convert to uppercase
.lower()       -> Convert to lowercase
.capitalize()  -> Capitalize first character
.title()       -> Capitalize every word
.replace()     -> Replace text
.find()        -> Find index of substring
.count()       -> Count occurrences
.strip()       -> Remove spaces
.split()       -> Convert string to list
.join()        -> Convert list to string
.startswith() -> Check beginning
.endswith()   -> Check ending
len()          -> Length of string
""")
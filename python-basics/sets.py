# ============================================================
# SETS IN PYTHON
# ============================================================

# A set is an unordered collection of unique elements.
# Sets do not allow duplicate values.

# ------------------------------------------------------------
# Creating a Set
# ------------------------------------------------------------

fruits = {"Apple", "Banana", "Mango"}

print(fruits)
print(type(fruits))

# ------------------------------------------------------------
# Duplicate Values Are Removed Automatically
# ------------------------------------------------------------

numbers = {1, 2, 3, 1, 2, 3, 4}

print(numbers)

# Output:
# {1, 2, 3, 4}

# ------------------------------------------------------------
# Adding Elements
# ------------------------------------------------------------

fruits.add("Orange")

print(fruits)

# ------------------------------------------------------------
# Adding Multiple Elements
# ------------------------------------------------------------

fruits.update(["Grapes", "Pineapple"])

print(fruits)

# ------------------------------------------------------------
# Removing Elements
# ------------------------------------------------------------

fruits.remove("Banana")

print(fruits)

# ------------------------------------------------------------
# Discarding Elements
# No error if item doesn't exist
# ------------------------------------------------------------

fruits.discard("Watermelon")

print(fruits)

# ------------------------------------------------------------
# Removing a Random Element
# ------------------------------------------------------------

fruits.pop()

print(fruits)

# ------------------------------------------------------------
# Length of a Set
# ------------------------------------------------------------

print(len(fruits))

# ------------------------------------------------------------
# Checking if an Item Exists
# ------------------------------------------------------------

print("Apple" in fruits)
print("Kiwi" in fruits)

# ------------------------------------------------------------
# Looping Through a Set
# ------------------------------------------------------------

for fruit in fruits:
    print(fruit)

# ------------------------------------------------------------
# Union (Combine Sets)
# ------------------------------------------------------------

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))

# OR

print(set1 | set2)

# ------------------------------------------------------------
# Intersection (Common Elements)
# ------------------------------------------------------------

print(set1.intersection(set2))

# OR

print(set1 & set2)

# ------------------------------------------------------------
# Difference
# Elements present in set1 but not in set2
# ------------------------------------------------------------

print(set1.difference(set2))

# OR

print(set1 - set2)

# ------------------------------------------------------------
# Symmetric Difference
# Elements present in either set but not both
# ------------------------------------------------------------

print(set1.symmetric_difference(set2))

# OR

print(set1 ^ set2)

# ------------------------------------------------------------
# Copying a Set
# ------------------------------------------------------------

new_set = set1.copy()

print(new_set)

# ------------------------------------------------------------
# Clearing a Set
# ------------------------------------------------------------

temp_set = {1, 2, 3}

temp_set.clear()

print(temp_set)

# ------------------------------------------------------------
# Converting a List to a Set
# Removes Duplicates
# ------------------------------------------------------------

numbers = [1, 2, 3, 1, 2, 4, 5]

unique_numbers = set(numbers)

print(unique_numbers)

# ------------------------------------------------------------
# AI/Data Science Example
# ------------------------------------------------------------

tags = [
    "AI",
    "Python",
    "Machine Learning",
    "AI",
    "Python"
]

unique_tags = set(tags)

print(unique_tags)

# ------------------------------------------------------------
# Summary
# ------------------------------------------------------------

print("""
Common Set Methods:

add()                  -> Add one item
update()               -> Add multiple items
remove()               -> Remove item
discard()              -> Remove safely
pop()                  -> Remove random item
union()                -> Combine sets
intersection()         -> Common elements
difference()           -> Unique elements
symmetric_difference() -> Non-common elements
clear()                -> Remove all items

Set Features:

{}             -> Create a set
Unique Values  -> No duplicates
Mutable        -> Can be modified
Unordered      -> No indexing
""")
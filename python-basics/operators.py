# ============================================================
# OPERATORS IN PYTHON
# ============================================================

# Operators are symbols used to perform operations on values
# and variables.

# ------------------------------------------------------------
# ARITHMETIC OPERATORS
# ------------------------------------------------------------

a = 10
b = 3

print("Addition:", a + b)          # 13
print("Subtraction:", a - b)       # 7
print("Multiplication:", a * b)    # 30
print("Division:", a / b)          # 3.333...
print("Floor Division:", a // b)   # 3
print("Modulus:", a % b)           # 1
print("Exponent:", a ** b)         # 1000

# ------------------------------------------------------------
# COMPARISON OPERATORS
# ------------------------------------------------------------

x = 10
y = 20

print("Equal To:", x == y)
print("Not Equal To:", x != y)
print("Greater Than:", x > y)
print("Less Than:", x < y)
print("Greater Than or Equal To:", x >= y)
print("Less Than or Equal To:", x <= y)

# ------------------------------------------------------------
# LOGICAL OPERATORS
# ------------------------------------------------------------

age = 21
is_student = True

print("AND:", age >= 18 and is_student)
print("OR:", age >= 18 or is_student)
print("NOT:", not is_student)

# ------------------------------------------------------------
# ASSIGNMENT OPERATORS
# ------------------------------------------------------------

num = 10

print("Original Value:", num)

num += 5      # num = num + 5
print("After += :", num)

num -= 3      # num = num - 3
print("After -= :", num)

num *= 2      # num = num * 2
print("After *= :", num)

num /= 4      # num = num / 4
print("After /= :", num)

num //= 2     # num = num // 2
print("After //= :", num)

num %= 3      # num = num % 3
print("After %= :", num)

# ------------------------------------------------------------
# MEMBERSHIP OPERATORS
# ------------------------------------------------------------

fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits)
print("Orange" in fruits)

print("Orange" not in fruits)

# ------------------------------------------------------------
# IDENTITY OPERATORS
# ------------------------------------------------------------

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)

print("list1 is not list3:", list1 is not list3)

# ------------------------------------------------------------
# BITWISE OPERATORS
# (Optional for Beginners)
# ------------------------------------------------------------

a = 5   # 0101
b = 3   # 0011

print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)

# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

print("""
Operator Categories:

Arithmetic:
+  -  *  /  //  %  **

Comparison:
==  !=  >  <  >=  <=

Logical:
and  or  not

Assignment:
=  +=  -=  *=  /=  //=  %=

Membership:
in  not in

Identity:
is  is not

Bitwise:
&  |  ^  ~  <<  >>
""")
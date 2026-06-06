# ============================================================
# DATETIME BASICS IN PYTHON
# ============================================================

# The datetime module is used to work with:
# - Dates
# - Times
# - Date & Time together

import datetime

# ============================================================
# CURRENT DATE AND TIME
# ============================================================

current_datetime = datetime.datetime.now()

print(current_datetime)

# Example Output:
# 2025-07-08 14:30:25.123456

# ============================================================
# CURRENT DATE
# ============================================================

today = datetime.date.today()

print(today)

# Example Output:
# 2025-07-08

# ============================================================
# CURRENT TIME
# ============================================================

current_time = datetime.datetime.now().time()

print(current_time)

# Example Output:
# 14:30:25.123456

# ============================================================
# ACCESSING DATE COMPONENTS
# ============================================================

now = datetime.datetime.now()

print("Year :", now.year)
print("Month:", now.month)
print("Day  :", now.day)

# ============================================================
# ACCESSING TIME COMPONENTS
# ============================================================

print("Hour       :", now.hour)
print("Minute     :", now.minute)
print("Second     :", now.second)
print("Microsecond:", now.microsecond)

# ============================================================
# CREATING A CUSTOM DATE
# ============================================================

birth_date = datetime.date(2004, 5, 10)

print(birth_date)

# ============================================================
# CREATING A CUSTOM DATETIME
# ============================================================

meeting = datetime.datetime(
    2025,
    12,
    25,
    10,
    30,
    0
)

print(meeting)

# ============================================================
# DATE FORMATTING (strftime)
# ============================================================

now = datetime.datetime.now()

print(now.strftime("%d-%m-%Y"))
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%B %d, %Y"))

# Example:
# 08-07-2025
# 08/07/2025
# July 08, 2025

# ============================================================
# COMMON FORMAT CODES
# ============================================================

print(now.strftime("%Y"))  # Year
print(now.strftime("%m"))  # Month Number
print(now.strftime("%B"))  # Month Name
print(now.strftime("%d"))  # Day

print(now.strftime("%H"))  # Hour (24-hour)
print(now.strftime("%I"))  # Hour (12-hour)
print(now.strftime("%M"))  # Minute
print(now.strftime("%S"))  # Second

# ============================================================
# STRING TO DATETIME (strptime)
# ============================================================

date_string = "10-05-2004"

date_object = datetime.datetime.strptime(
    date_string,
    "%d-%m-%Y"
)

print(date_object)

# ============================================================
# DATE DIFFERENCE
# ============================================================

date1 = datetime.date(2025, 1, 1)
date2 = datetime.date(2025, 12, 31)

difference = date2 - date1

print(difference)
print(difference.days)

# ============================================================
# ADDING DAYS
# ============================================================

today = datetime.date.today()

future_date = today + datetime.timedelta(days=30)

print(future_date)

# ============================================================
# SUBTRACTING DAYS
# ============================================================

past_date = today - datetime.timedelta(days=7)

print(past_date)

# ============================================================
# PRACTICAL EXAMPLE 1
# AGE CALCULATION
# ============================================================

birth_year = 2004

current_year = datetime.datetime.now().year

age = current_year - birth_year

print("Age:", age)

# ============================================================
# PRACTICAL EXAMPLE 2
# DIGITAL CLOCK
# ============================================================

current_time = datetime.datetime.now()

print(
    current_time.strftime("%H:%M:%S")
)

# ============================================================
# PRACTICAL EXAMPLE 3
# FILE TIMESTAMP
# ============================================================

timestamp = datetime.datetime.now().strftime(
    "%Y-%m-%d_%H-%M-%S"
)

print(timestamp)

# Example:
# 2025-07-08_14-30-25

# ============================================================
# SUMMARY
# ============================================================

print("""
Common Functions:

datetime.now()
date.today()

strftime()
strptime()

timedelta()

Common Format Codes:

%Y -> Year
%m -> Month Number
%B -> Month Name
%d -> Day

%H -> Hour (24-hour)
%I -> Hour (12-hour)
%M -> Minute
%S -> Second
""")
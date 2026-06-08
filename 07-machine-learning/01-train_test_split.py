# ============================================================
# TRAIN TEST SPLIT IN MACHINE LEARNING
# ============================================================

# Train-Test Split is used to divide data into:
#
# 1. Training Data → Used to train the model
# 2. Testing Data  → Used to evaluate the model
#
# Why?
#
# ✔ Prevent Overfitting
# ✔ Evaluate Model Performance
# ✔ Simulate Real-World Predictions
# ✔ Essential ML Workflow

# Install:
# pip install scikit-learn pandas

from sklearn.model_selection import train_test_split

# ============================================================
# BASIC EXAMPLE
# ============================================================

# Features (X)

X = [
    [10],
    [20],
    [30],
    [40],
    [50]
]

# Target (y)

y = [1, 2, 3, 4, 5]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y
)

print("X Train:", X_train)
print("X Test :", X_test)

print("y Train:", y_train)
print("y Test :", y_test)

# ============================================================
# UNDERSTANDING THE OUTPUT
# ============================================================

# X_train → Training features
# X_test  → Testing features
#
# y_train → Training labels
# y_test  → Testing labels

# ============================================================
# USING test_size
# ============================================================

# test_size determines how much data
# goes into testing.

X = [[1], [2], [3], [4], [5], [6], [7], [8]]

y = [10, 20, 30, 40, 50, 60, 70, 80]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25
)

print("\nTest Size Example")

print("Training Samples:", len(X_train))
print("Testing Samples :", len(X_test))

# ============================================================
# USING random_state
# ============================================================

# random_state makes results reproducible.

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

print("\nRandom State Example")

print("X Train:", X_train)
print("X Test :", X_test)

# ============================================================
# WITHOUT random_state
# ============================================================

# Every run gives different results.

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25
)

print("\nWithout Random State")

print("X Train:", X_train)
print("X Test :", X_test)

# ============================================================
# USING train_size
# ============================================================

# Specify training data size directly.

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    train_size=0.75,
    random_state=42
)

print("\nTrain Size Example")

print("Training Samples:", len(X_train))
print("Testing Samples :", len(X_test))

# ============================================================
# SHUFFLING DATA
# ============================================================

# shuffle=True is default.

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    shuffle=True,
    random_state=42
)

print("\nShuffle Example")

print("X Train:", X_train)
print("X Test :", X_test)

# ============================================================
# WITHOUT SHUFFLING
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    shuffle=False
)

print("\nWithout Shuffle")

print("X Train:", X_train)
print("X Test :", X_test)

# ============================================================
# USING STRATIFY
# ============================================================

# Keeps class distribution balanced.

X = [
    [1], [2], [3], [4],
    [5], [6], [7], [8]
]

y = [
    0, 0, 0, 0,
    1, 1, 1, 1
]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    stratify=y,
    random_state=42
)

print("\nStratify Example")

print("y Train:", y_train)
print("y Test :", y_test)

# ============================================================
# USING PANDAS DATAFRAME
# ============================================================

import pandas as pd

data = pd.DataFrame({
    "Age": [20, 25, 30, 35, 40],
    "Salary": [30000, 40000, 50000, 60000, 70000],
    "Purchased": [0, 0, 1, 1, 1]
})

X = data[["Age", "Salary"]]

y = data["Purchased"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nPandas Example")

print("X Train")
print(X_train)

print("\nX Test")
print(X_test)

# ============================================================
# PRACTICAL EXAMPLE 1
# STUDENT MARKS
# ============================================================

students = pd.DataFrame({
    "StudyHours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [35, 40, 50, 55, 65, 75, 85, 95]
})

X = students[["StudyHours"]]

y = students["Marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

print("\nStudent Dataset")

print("Training Data")
print(X_train)

print("\nTesting Data")
print(X_test)

# ============================================================
# PRACTICAL EXAMPLE 2
# HOUSE PRICE PREDICTION
# ============================================================

houses = pd.DataFrame({
    "Area": [800, 1000, 1200, 1400, 1600, 1800],
    "Price": [20, 25, 30, 35, 40, 45]
})

X = houses[["Area"]]

y = houses["Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.33,
    random_state=42
)

print("\nHouse Dataset")

print("X Train")
print(X_train)

print("\nX Test")
print(X_test)

# ============================================================
# PRACTICAL EXAMPLE 3
# CUSTOMER PURCHASE DATA
# ============================================================

customers = pd.DataFrame({
    "Age": [18, 22, 25, 30, 35, 40, 45, 50],
    "Purchased": [0, 0, 0, 1, 1, 1, 1, 1]
})

X = customers[["Age"]]

y = customers["Purchased"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    stratify=y,
    random_state=42
)

print("\nCustomer Dataset")

print("Training Labels")
print(y_train)

print("\nTesting Labels")
print(y_test)

# ============================================================
# COMMON PARAMETERS
# ============================================================

# test_size
# train_size
# random_state
# shuffle
# stratify

# ============================================================
# SUMMARY
# ============================================================

print("""
TRAIN TEST SPLIT SUMMARY

Import:

from sklearn.model_selection import train_test_split

Basic Syntax:

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y
)

Common Parameters:

test_size=0.2
train_size=0.8
random_state=42
shuffle=True
stratify=y

Outputs:

X_train
X_test
y_train
y_test

Uses:

✔ Machine Learning
✔ Data Preparation
✔ Model Training
✔ Model Evaluation

Benefits:

✔ Prevent Overfitting
✔ Better Generalization
✔ Reliable Testing
✔ Essential ML Practice
""")
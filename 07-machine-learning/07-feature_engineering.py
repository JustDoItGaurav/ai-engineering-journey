# ============================================================
# FEATURE ENGINEERING IN MACHINE LEARNING
# ============================================================

# Feature Engineering is the process of
# creating, transforming, and selecting
# features (columns) to improve model performance.
#
# Why Feature Engineering?
#
# ✔ Improve Accuracy
# ✔ Better Predictions
# ✔ Reduce Noise
# ✔ Faster Training
#
# Examples:
#
# Age → Age Group
# Date → Month, Year
# Salary → Salary Category
#
# Feature Engineering is often more important
# than choosing a complex algorithm.

# Install:
# pip install pandas scikit-learn numpy

import pandas as pd
import numpy as np

# ============================================================
# SAMPLE DATASET
# ============================================================

data = pd.DataFrame({
    "Age": [18, 25, 35, 45, 55],
    "Salary": [20000, 35000, 50000, 70000, 90000]
})

print("Original Dataset")

print(data)

# ============================================================
# CREATING NEW FEATURES
# ============================================================

# Create Age Squared Feature

data["Age_Squared"] = data["Age"] ** 2

print("\nAge Squared Feature")

print(data)

# ============================================================
# COMBINING FEATURES
# ============================================================

data["Age_Salary_Ratio"] = (
    data["Salary"] / data["Age"]
)

print("\nCombined Feature")

print(data)

# ============================================================
# BINNING (CATEGORIZATION)
# ============================================================

data["Age_Group"] = pd.cut(
    data["Age"],
    bins=[0, 20, 40, 60],
    labels=[
        "Young",
        "Adult",
        "Senior"
    ]
)

print("\nAge Groups")

print(data)

# ============================================================
# HANDLING DATE FEATURES
# ============================================================

data = pd.DataFrame({
    "Date": pd.to_datetime([
        "2024-01-10",
        "2024-02-15",
        "2024-03-20"
    ])
})

data["Year"] = data["Date"].dt.year

data["Month"] = data["Date"].dt.month

data["Day"] = data["Date"].dt.day

print("\nDate Features")

print(data)

# ============================================================
# EXTRACTING WEEKDAY
# ============================================================

data["Weekday"] = (
    data["Date"].dt.day_name()
)

print("\nWeekday Feature")

print(data)

# ============================================================
# ONE HOT ENCODING
# ============================================================

data = pd.DataFrame({
    "City": [
        "Mumbai",
        "Delhi",
        "Pune"
    ]
})

encoded = pd.get_dummies(
    data,
    columns=["City"]
)

print("\nOne Hot Encoding")

print(encoded)

# ============================================================
# LABEL ENCODING
# ============================================================

from sklearn.preprocessing import LabelEncoder

data = pd.DataFrame({
    "Grade": [
        "A",
        "B",
        "C",
        "A"
    ]
})

encoder = LabelEncoder()

data["Grade_Encoded"] = encoder.fit_transform(
    data["Grade"]
)

print("\nLabel Encoding")

print(data)

# ============================================================
# FEATURE SCALING
# ============================================================

from sklearn.preprocessing import StandardScaler

data = pd.DataFrame({
    "Salary": [
        20000,
        30000,
        40000,
        50000
    ]
})

scaler = StandardScaler()

data["Scaled_Salary"] = scaler.fit_transform(
    data[["Salary"]]
)

print("\nFeature Scaling")

print(data)

# ============================================================
# NORMALIZATION
# ============================================================

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

data["Normalized_Salary"] = scaler.fit_transform(
    data[["Salary"]]
)

print("\nNormalization")

print(data)

# ============================================================
# LOG TRANSFORMATION
# ============================================================

data = pd.DataFrame({
    "Income": [
        1000,
        5000,
        10000,
        50000
    ]
})

data["Log_Income"] = np.log(
    data["Income"]
)

print("\nLog Transformation")

print(data)

# ============================================================
# HANDLING MISSING VALUES
# ============================================================

data = pd.DataFrame({
    "Age": [20, 25, np.nan, 35]
})

data["Age"] = data["Age"].fillna(
    data["Age"].mean()
)

print("\nMissing Values Handled")

print(data)

# ============================================================
# FEATURE SELECTION
# ============================================================

from sklearn.feature_selection import VarianceThreshold

X = pd.DataFrame({
    "A": [1, 1, 1, 1],
    "B": [1, 2, 3, 4],
    "C": [5, 6, 7, 8]
})

selector = VarianceThreshold()

selected = selector.fit_transform(X)

print("\nSelected Features")

print(selected)

# ============================================================
# PRACTICAL EXAMPLE 1
# STUDENT DATASET
# ============================================================

students = pd.DataFrame({
    "Math": [80, 70, 90],
    "Science": [75, 65, 95]
})

students["Total"] = (
    students["Math"]
    + students["Science"]
)

students["Average"] = (
    students["Total"] / 2
)

print("\nStudent Features")

print(students)

# ============================================================
# PRACTICAL EXAMPLE 2
# SALES DATASET
# ============================================================

sales = pd.DataFrame({
    "Price": [100, 200, 300],
    "Quantity": [2, 3, 4]
})

sales["Revenue"] = (
    sales["Price"]
    * sales["Quantity"]
)

print("\nSales Features")

print(sales)

# ============================================================
# PRACTICAL EXAMPLE 3
# CUSTOMER DATASET
# ============================================================

customers = pd.DataFrame({
    "Age": [22, 35, 48],
    "Salary": [25000, 60000, 90000]
})

customers["Salary_Per_Age"] = (
    customers["Salary"]
    / customers["Age"]
)

print("\nCustomer Features")

print(customers)

# ============================================================
# ADVANCED FEATURE ENGINEERING
# ============================================================

# Polynomial Features

from sklearn.preprocessing import PolynomialFeatures

X = [[1], [2], [3]]

poly = PolynomialFeatures(
    degree=2
)

result = poly.fit_transform(X)

print("\nPolynomial Features")

print(result)

# ============================================================
# IMPORTANT TECHNIQUES
# ============================================================

# Feature Creation
# Feature Transformation
# Feature Encoding
# Feature Scaling
# Feature Selection
# Missing Value Handling

# ============================================================
# ADVANTAGES
# ============================================================

# ✔ Improves Accuracy
# ✔ Better Generalization
# ✔ Faster Learning
# ✔ Better Insights

# ============================================================
# LIMITATIONS
# ============================================================

# ✘ Time Consuming
# ✘ Requires Domain Knowledge
# ✘ Wrong Features Reduce Accuracy
# ✘ Can Cause Overfitting

# ============================================================
# SUMMARY
# ============================================================

print("""
FEATURE ENGINEERING SUMMARY

What is Feature Engineering?

Creating and transforming features
to improve machine learning models.

Common Techniques

✔ Feature Creation
✔ Feature Transformation
✔ Encoding
✔ Scaling
✔ Normalization
✔ Feature Selection

Encoding Methods

LabelEncoder()
pd.get_dummies()

Scaling Methods

StandardScaler()
MinMaxScaler()

Transformations

Log Transformation
Polynomial Features

Uses

✔ Improve Accuracy
✔ Better Predictions
✔ Faster Models
✔ Cleaner Data

Benefits

✔ More Informative Features
✔ Better Model Performance
✔ Reduced Noise
✔ Essential ML Skill
""")
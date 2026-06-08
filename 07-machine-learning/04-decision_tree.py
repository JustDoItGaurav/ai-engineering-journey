# ============================================================
# DECISION TREE IN MACHINE LEARNING
# ============================================================

# Decision Tree is a Supervised Learning Algorithm.
#
# It can be used for:
#
# ✔ Classification
# ✔ Regression
#
# It works by splitting data into branches
# based on conditions.
#
# Example:
#
# Age > 30 ?
#      |
#   Yes/No
#
# Purchased ?
#
# It looks like an upside-down tree.

# Install:
# pip install scikit-learn pandas matplotlib

from sklearn.tree import DecisionTreeClassifier

# ============================================================
# BASIC EXAMPLE
# ============================================================

X = [
    [20],
    [25],
    [30],
    [35],
    [40],
    [45]
]

y = [0, 0, 0, 1, 1, 1]

model = DecisionTreeClassifier()

model.fit(X, y)

prediction = model.predict([[32]])

print("Prediction =", prediction)

# ============================================================
# UNDERSTANDING fit()
# ============================================================

# fit() trains the tree

X = [
    [10],
    [20],
    [30],
    [40]
]

y = [0, 0, 1, 1]

model = DecisionTreeClassifier()

model.fit(X, y)

print("\nModel Trained Successfully")

# ============================================================
# UNDERSTANDING predict()
# ============================================================

prediction = model.predict([[25]])

print("\nPrediction =", prediction)

# ============================================================
# PREDICTING PROBABILITY
# ============================================================

probability = model.predict_proba([[25]])

print("\nProbability")

print(probability)

# ============================================================
# CLASS LABELS
# ============================================================

print("\nClasses")

print(model.classes_)

# ============================================================
# FEATURE IMPORTANCE
# ============================================================

print("\nFeature Importance")

print(model.feature_importances_)

# ============================================================
# USING PANDAS DATAFRAME
# ============================================================

import pandas as pd

data = pd.DataFrame({
    "Age": [20, 25, 30, 35, 40, 45],
    "Purchased": [0, 0, 0, 1, 1, 1]
})

X = data[["Age"]]

y = data["Purchased"]

model = DecisionTreeClassifier()

model.fit(X, y)

prediction = model.predict([[32]])

print("\nPandas Example")

print("Prediction =", prediction)

# ============================================================
# TRAIN TEST SPLIT
# ============================================================

from sklearn.model_selection import train_test_split

X = data[["Age"]]

y = data["Purchased"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

model = DecisionTreeClassifier()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("\nTest Predictions")

print(predictions)

# ============================================================
# MODEL ACCURACY
# ============================================================

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(
    y_test,
    predictions
)

print("\nAccuracy =", accuracy)

# ============================================================
# CONFUSION MATRIX
# ============================================================

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(
    y_test,
    predictions
)

print("\nConfusion Matrix")

print(cm)

# ============================================================
# CLASSIFICATION REPORT
# ============================================================

from sklearn.metrics import classification_report

report = classification_report(
    y_test,
    predictions
)

print("\nClassification Report")

print(report)

# ============================================================
# VISUALIZING DECISION TREE
# ============================================================

import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

X = data[["Age"]]

y = data["Purchased"]

model = DecisionTreeClassifier()

model.fit(X, y)

plt.figure(figsize=(8, 5))

plot_tree(
    model,
    feature_names=["Age"],
    class_names=["No", "Yes"],
    filled=True
)

plt.show()

# ============================================================
# PRACTICAL EXAMPLE 1
# STUDENT PASS / FAIL
# ============================================================

students = pd.DataFrame({
    "Hours": [1, 2, 3, 4, 5, 6],
    "Pass": [0, 0, 0, 1, 1, 1]
})

X = students[["Hours"]]

y = students["Pass"]

model = DecisionTreeClassifier()

model.fit(X, y)

prediction = model.predict([[4.5]])

print("\nStudent Example")

print("Pass Prediction =", prediction)

# ============================================================
# PRACTICAL EXAMPLE 2
# CUSTOMER PURCHASE PREDICTION
# ============================================================

customers = pd.DataFrame({
    "Age": [18, 22, 25, 30, 35, 40, 45, 50],
    "Purchased": [0, 0, 0, 1, 1, 1, 1, 1]
})

X = customers[["Age"]]

y = customers["Purchased"]

model = DecisionTreeClassifier()

model.fit(X, y)

prediction = model.predict([[28]])

print("\nCustomer Example")

print("Purchased =", prediction)

# ============================================================
# PRACTICAL EXAMPLE 3
# LOAN APPROVAL PREDICTION
# ============================================================

loan = pd.DataFrame({
    "Income": [20, 25, 30, 50, 60, 70],
    "Approved": [0, 0, 0, 1, 1, 1]
})

X = loan[["Income"]]

y = loan["Approved"]

model = DecisionTreeClassifier()

model.fit(X, y)

prediction = model.predict([[55]])

print("\nLoan Prediction")

print("Approved =", prediction)

# ============================================================
# MULTIPLE FEATURES
# ============================================================

data = pd.DataFrame({
    "Age": [20, 25, 30, 35, 40, 45],
    "Salary": [20000, 25000, 30000, 50000, 60000, 70000],
    "Purchased": [0, 0, 0, 1, 1, 1]
})

X = data[["Age", "Salary"]]

y = data["Purchased"]

model = DecisionTreeClassifier()

model.fit(X, y)

prediction = model.predict([
    [32, 45000]
])

print("\nMultiple Feature Example")

print("Prediction =", prediction)

# ============================================================
# CONTROLLING TREE DEPTH
# ============================================================

model = DecisionTreeClassifier(
    max_depth=3
)

model.fit(X, y)

print("\nTree Depth Controlled")

# ============================================================
# IMPORTANT PARAMETERS
# ============================================================

# max_depth
# min_samples_split
# min_samples_leaf
# criterion

# Example:

model = DecisionTreeClassifier(
    max_depth=4,
    criterion="gini"
)

# ============================================================
# ADVANTAGES
# ============================================================

# ✔ Easy to Understand
# ✔ Easy to Visualize
# ✔ Handles Non-Linear Data
# ✔ No Feature Scaling Required

# ============================================================
# LIMITATIONS
# ============================================================

# ✘ Can Overfit
# ✘ Sensitive to Small Data Changes
# ✘ Less Accurate than Ensembles
# ✘ Large Trees Become Complex

# ============================================================
# SUMMARY
# ============================================================

print("""
DECISION TREE SUMMARY

Import:

from sklearn.tree import DecisionTreeClassifier

Create Model:

model = DecisionTreeClassifier()

Train:

model.fit(X, y)

Predict:

model.predict([[value]])

Useful Attributes:

model.feature_importances_

Visualization:

plot_tree()

Important Parameters:

max_depth
min_samples_split
min_samples_leaf
criterion

Uses:

✔ Customer Prediction
✔ Loan Approval
✔ Medical Diagnosis
✔ Student Performance

Benefits:

✔ Simple
✔ Visual
✔ Powerful
✔ Handles Non-Linear Data
""")
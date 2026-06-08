# ============================================================
# RANDOM FOREST IN MACHINE LEARNING
# ============================================================

# Random Forest is a Supervised Learning Algorithm.
#
# It is an Ensemble Learning Method.
#
# Ensemble Learning:
#
# Multiple Models → One Strong Model
#
# Random Forest combines many
# Decision Trees together.
#
# Final Prediction:
#
# Classification → Majority Voting
# Regression → Average Prediction
#
# Uses:
#
# ✔ Customer Prediction
# ✔ Disease Prediction
# ✔ Fraud Detection
# ✔ Loan Approval
# ✔ Sales Prediction

# Install:
# pip install scikit-learn pandas matplotlib

from sklearn.ensemble import RandomForestClassifier

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

model = RandomForestClassifier()

model.fit(X, y)

prediction = model.predict([[32]])

print("Prediction =", prediction)

# ============================================================
# UNDERSTANDING fit()
# ============================================================

# fit() trains multiple trees

X = [
    [10],
    [20],
    [30],
    [40]
]

y = [0, 0, 1, 1]

model = RandomForestClassifier()

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
# NUMBER OF TREES
# ============================================================

print("\nNumber of Trees")

print(model.n_estimators)

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

model = RandomForestClassifier()

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

model = RandomForestClassifier()

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
# PRACTICAL EXAMPLE 1
# STUDENT PASS / FAIL
# ============================================================

students = pd.DataFrame({
    "Hours": [1, 2, 3, 4, 5, 6],
    "Pass": [0, 0, 0, 1, 1, 1]
})

X = students[["Hours"]]

y = students["Pass"]

model = RandomForestClassifier()

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

model = RandomForestClassifier()

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

model = RandomForestClassifier()

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

model = RandomForestClassifier()

model.fit(X, y)

prediction = model.predict([
    [32, 45000]
])

print("\nMultiple Feature Example")

print("Prediction =", prediction)

# ============================================================
# CONTROLLING NUMBER OF TREES
# ============================================================

model = RandomForestClassifier(
    n_estimators=100
)

model.fit(X, y)

print("\n100 Trees Created")

# ============================================================
# IMPORTANT PARAMETERS
# ============================================================

# n_estimators
# max_depth
# min_samples_split
# min_samples_leaf
# random_state

# Example

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=5,
    random_state=42
)

# ============================================================
# FEATURE IMPORTANCE EXAMPLE
# ============================================================

model.fit(X, y)

print("\nFeature Importance")

for feature, importance in zip(
    X.columns,
    model.feature_importances_
):
    print(feature, ":", importance)

# ============================================================
# ADVANTAGES
# ============================================================

# ✔ High Accuracy
# ✔ Reduces Overfitting
# ✔ Handles Large Datasets
# ✔ Works with Non-Linear Data
# ✔ Feature Importance Available

# ============================================================
# LIMITATIONS
# ============================================================

# ✘ Slower Than One Decision Tree
# ✘ More Memory Usage
# ✘ Harder To Interpret
# ✘ Large Models Can Be Slow

# ============================================================
# SUMMARY
# ============================================================

print("""
RANDOM FOREST SUMMARY

Import:

from sklearn.ensemble import RandomForestClassifier

Create Model:

model = RandomForestClassifier()

Train:

model.fit(X, y)

Predict:

model.predict([[value]])

Probability:

model.predict_proba([[value]])

Useful Attributes:

model.feature_importances_
model.n_estimators

Important Parameters:

n_estimators
max_depth
min_samples_split
min_samples_leaf
random_state

Uses:

✔ Fraud Detection
✔ Loan Approval
✔ Customer Prediction
✔ Medical Diagnosis
✔ Sales Forecasting

Benefits:

✔ Accurate
✔ Robust
✔ Less Overfitting
✔ Handles Complex Data
""")
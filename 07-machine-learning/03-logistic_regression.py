# ============================================================
# LOGISTIC REGRESSION IN MACHINE LEARNING
# ============================================================

# Logistic Regression is a Supervised Learning Algorithm.
#
# It is mainly used for Classification Problems.
#
# Examples:
#
# ✔ Spam Detection
# ✔ Disease Prediction
# ✔ Customer Purchase Prediction
# ✔ Pass / Fail Prediction
#
# Unlike Linear Regression,
# Logistic Regression predicts probabilities.
#
# Output:
#
# 0 = No
# 1 = Yes
#
# Example:
#
# Purchased = 1
# Not Purchased = 0

# Install:
# pip install scikit-learn pandas matplotlib

from sklearn.linear_model import LogisticRegression

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

model = LogisticRegression()

model.fit(X, y)

prediction = model.predict([[32]])

print("Prediction:", prediction)

# ============================================================
# UNDERSTANDING fit()
# ============================================================

# fit() trains the model

X = [
    [10],
    [20],
    [30],
    [40]
]

y = [0, 0, 1, 1]

model = LogisticRegression()

model.fit(X, y)

print("\nModel Trained Successfully")

# ============================================================
# UNDERSTANDING predict()
# ============================================================

prediction = model.predict([[25]])

print("\nPrediction for 25 =", prediction)

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
# MODEL COEFFICIENT
# ============================================================

print("\nCoefficient")

print(model.coef_)

# ============================================================
# MODEL INTERCEPT
# ============================================================

print("\nIntercept")

print(model.intercept_)

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

model = LogisticRegression()

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

model = LogisticRegression()

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
# VISUALIZING DATA
# ============================================================

import matplotlib.pyplot as plt

X = [20, 25, 30, 35, 40, 45]

y = [0, 0, 0, 1, 1, 1]

plt.scatter(X, y)

plt.title("Logistic Regression Dataset")

plt.xlabel("Age")

plt.ylabel("Purchased")

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

model = LogisticRegression()

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

model = LogisticRegression()

model.fit(X, y)

prediction = model.predict([[28]])

print("\nCustomer Example")

print("Purchased =", prediction)

# ============================================================
# PRACTICAL EXAMPLE 3
# DISEASE PREDICTION
# ============================================================

patients = pd.DataFrame({
    "SugarLevel": [80, 90, 100, 130, 150, 180],
    "Diabetes": [0, 0, 0, 1, 1, 1]
})

X = patients[["SugarLevel"]]

y = patients["Diabetes"]

model = LogisticRegression()

model.fit(X, y)

prediction = model.predict([[140]])

print("\nDisease Prediction")

print("Diabetes =", prediction)

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

model = LogisticRegression()

model.fit(X, y)

prediction = model.predict([
    [32, 45000]
])

print("\nMultiple Feature Example")

print("Prediction =", prediction)

# ============================================================
# ADVANTAGES
# ============================================================

# ✔ Simple and Fast
# ✔ Easy to Interpret
# ✔ Works Well for Binary Classification
# ✔ Provides Probabilities

# ============================================================
# LIMITATIONS
# ============================================================

# ✘ Assumes Linear Decision Boundary
# ✘ Sensitive to Outliers
# ✘ May Underperform on Complex Data
# ✘ Requires Feature Engineering

# ============================================================
# SUMMARY
# ============================================================

print("""
LOGISTIC REGRESSION SUMMARY

Import:

from sklearn.linear_model import LogisticRegression

Create Model:

model = LogisticRegression()

Train Model:

model.fit(X, y)

Predict:

model.predict([[value]])

Predict Probability:

model.predict_proba([[value]])

Evaluation Metrics:

accuracy_score()
confusion_matrix()
classification_report()

Uses:

✔ Spam Detection
✔ Disease Prediction
✔ Customer Purchase Prediction
✔ Pass / Fail Prediction

Output:

0 = No
1 = Yes

Benefits:

✔ Fast
✔ Simple
✔ Probabilistic Output
✔ Classification Focused
""")
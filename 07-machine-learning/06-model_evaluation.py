# ============================================================
# MODEL EVALUATION IN MACHINE LEARNING
# ============================================================

# Model Evaluation helps us measure
# how well a machine learning model performs.
#
# Why Evaluation?
#
# ✔ Check Accuracy
# ✔ Detect Errors
# ✔ Compare Models
# ✔ Improve Performance
#
# Common Metrics:
#
# Classification:
# ✔ Accuracy
# ✔ Precision
# ✔ Recall
# ✔ F1 Score
# ✔ Confusion Matrix
#
# Regression:
# ✔ MAE
# ✔ MSE
# ✔ RMSE
# ✔ R² Score

# Install:
# pip install scikit-learn pandas

# ============================================================
# SAMPLE CLASSIFICATION DATA
# ============================================================

y_true = [1, 0, 1, 1, 0, 1]

y_pred = [1, 0, 1, 0, 0, 1]

# ============================================================
# ACCURACY SCORE
# ============================================================

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(
    y_true,
    y_pred
)

print("Accuracy =", accuracy)

# ============================================================
# PRECISION SCORE
# ============================================================

from sklearn.metrics import precision_score

precision = precision_score(
    y_true,
    y_pred
)

print("\nPrecision =", precision)

# ============================================================
# RECALL SCORE
# ============================================================

from sklearn.metrics import recall_score

recall = recall_score(
    y_true,
    y_pred
)

print("\nRecall =", recall)

# ============================================================
# F1 SCORE
# ============================================================

from sklearn.metrics import f1_score

f1 = f1_score(
    y_true,
    y_pred
)

print("\nF1 Score =", f1)

# ============================================================
# CLASSIFICATION REPORT
# ============================================================

from sklearn.metrics import classification_report

report = classification_report(
    y_true,
    y_pred
)

print("\nClassification Report")

print(report)

# ============================================================
# CONFUSION MATRIX
# ============================================================

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(
    y_true,
    y_pred
)

print("\nConfusion Matrix")

print(cm)

# ============================================================
# UNDERSTANDING CONFUSION MATRIX
# ============================================================

#               Predicted
#
#             0         1
#
# Actual 0   TN        FP
#
# Actual 1   FN        TP

print("""
Confusion Matrix Terms

TP = True Positive
TN = True Negative
FP = False Positive
FN = False Negative
""")

# ============================================================
# VISUALIZING CONFUSION MATRIX
# ============================================================

import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

ConfusionMatrixDisplay(
    confusion_matrix=cm
).plot()

plt.show()

# ============================================================
# PRACTICAL EXAMPLE 1
# LOGISTIC REGRESSION EVALUATION
# ============================================================

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd

data = pd.DataFrame({
    "Age": [20, 25, 30, 35, 40, 45, 50, 55],
    "Purchased": [0, 0, 0, 1, 1, 1, 1, 1]
})

X = data[["Age"]]

y = data["Purchased"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

model = LogisticRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("\nLogistic Regression Accuracy")

print(
    accuracy_score(
        y_test,
        predictions
    )
)

# ============================================================
# SAMPLE REGRESSION DATA
# ============================================================

y_true = [100, 120, 130, 150]

y_pred = [105, 118, 128, 152]

# ============================================================
# MEAN ABSOLUTE ERROR (MAE)
# ============================================================

from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(
    y_true,
    y_pred
)

print("\nMAE =", mae)

# ============================================================
# MEAN SQUARED ERROR (MSE)
# ============================================================

from sklearn.metrics import mean_squared_error

mse = mean_squared_error(
    y_true,
    y_pred
)

print("\nMSE =", mse)

# ============================================================
# ROOT MEAN SQUARED ERROR (RMSE)
# ============================================================

import numpy as np

rmse = np.sqrt(mse)

print("\nRMSE =", rmse)

# ============================================================
# R² SCORE
# ============================================================

from sklearn.metrics import r2_score

r2 = r2_score(
    y_true,
    y_pred
)

print("\nR² Score =", r2)

# ============================================================
# PRACTICAL EXAMPLE 2
# LINEAR REGRESSION EVALUATION
# ============================================================

from sklearn.linear_model import LinearRegression

data = pd.DataFrame({
    "Hours": [1, 2, 3, 4, 5, 6],
    "Marks": [35, 45, 55, 65, 75, 85]
})

X = data[["Hours"]]

y = data["Marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("\nRegression Evaluation")

print(
    "MAE:",
    mean_absolute_error(
        y_test,
        predictions
    )
)

print(
    "MSE:",
    mean_squared_error(
        y_test,
        predictions
    )
)

print(
    "R²:",
    r2_score(
        y_test,
        predictions
    )
)

# ============================================================
# CROSS VALIDATION
# ============================================================

from sklearn.model_selection import cross_val_score

X = data[["Hours"]]

y = data["Marks"]

model = LinearRegression()

scores = cross_val_score(
    model,
    X,
    y,
    cv=3
)

print("\nCross Validation Scores")

print(scores)

print(
    "Average Score:",
    scores.mean()
)

# ============================================================
# PRACTICAL EXAMPLE 3
# RANDOM FOREST EVALUATION
# ============================================================

from sklearn.ensemble import RandomForestClassifier

data = pd.DataFrame({
    "Age": [20, 25, 30, 35, 40, 45, 50, 55],
    "Purchased": [0, 0, 0, 1, 1, 1, 1, 1]
})

X = data[["Age"]]

y = data["Purchased"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

model = RandomForestClassifier()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("\nRandom Forest Accuracy")

print(
    accuracy_score(
        y_test,
        predictions
    )
)

# ============================================================
# SUMMARY
# ============================================================

print("""
MODEL EVALUATION SUMMARY

Classification Metrics

accuracy_score()
precision_score()
recall_score()
f1_score()
confusion_matrix()
classification_report()

Regression Metrics

mean_absolute_error()
mean_squared_error()
r2_score()

Formula Concepts

Accuracy = Correct Predictions / Total Predictions

Precision = TP / (TP + FP)

Recall = TP / (TP + FN)

F1 Score =
2 × (Precision × Recall)
------------------------
 Precision + Recall

Regression Metrics

MAE  -> Average Error

MSE  -> Squared Error

RMSE -> Square Root of MSE

R²   -> Goodness of Fit

Advanced Evaluation

cross_val_score()

Uses

✔ Compare Models
✔ Measure Performance
✔ Detect Overfitting
✔ Improve Accuracy

Benefits

✔ Reliable Results
✔ Better Model Selection
✔ Professional Evaluation
✔ Essential ML Skill
""")
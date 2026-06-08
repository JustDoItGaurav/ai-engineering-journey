# ============================================================
# LINEAR REGRESSION IN MACHINE LEARNING
# ============================================================

# Linear Regression is one of the most popular
# supervised machine learning algorithms.
#
# It is used to predict continuous values.
#
# Examples:
#
# ✔ House Price Prediction
# ✔ Salary Prediction
# ✔ Sales Forecasting
# ✔ Temperature Prediction
#
# It finds the best-fit straight line:
#
# y = mx + c
#
# Where:
#
# y = Predicted Value
# m = Slope
# x = Input Feature
# c = Intercept

# Install:
# pip install scikit-learn pandas matplotlib

from sklearn.linear_model import LinearRegression

# ============================================================
# BASIC EXAMPLE
# ============================================================

# Feature

X = [
    [1],
    [2],
    [3],
    [4],
    [5]
]

# Target

y = [10, 20, 30, 40, 50]

model = LinearRegression()

model.fit(X, y)

prediction = model.predict([[6]])

print("Prediction for 6 =", prediction)

# ============================================================
# UNDERSTANDING fit()
# ============================================================

# fit() trains the model

X = [[1], [2], [3], [4]]

y = [5, 10, 15, 20]

model = LinearRegression()

model.fit(X, y)

print("\nModel Trained Successfully")

# ============================================================
# UNDERSTANDING predict()
# ============================================================

prediction = model.predict([[5]])

print("\nPrediction for 5 =", prediction)

# ============================================================
# MODEL COEFFICIENT (SLOPE)
# ============================================================

print("\nSlope =", model.coef_[0])

# ============================================================
# MODEL INTERCEPT
# ============================================================

print("Intercept =", model.intercept_)

# ============================================================
# LINEAR REGRESSION EQUATION
# ============================================================

# y = mx + c

m = model.coef_[0]

c = model.intercept_

print("\nEquation:")

print(f"y = {m:.2f}x + {c:.2f}")

# ============================================================
# MULTIPLE PREDICTIONS
# ============================================================

predictions = model.predict([
    [6],
    [7],
    [8]
])

print("\nMultiple Predictions")

print(predictions)

# ============================================================
# USING PANDAS DATAFRAME
# ============================================================

import pandas as pd

data = pd.DataFrame({
    "StudyHours": [1, 2, 3, 4, 5],
    "Marks": [35, 45, 55, 65, 75]
})

X = data[["StudyHours"]]

y = data["Marks"]

model = LinearRegression()

model.fit(X, y)

prediction = model.predict([[6]])

print("\nPandas Example")

print("Predicted Marks =", prediction)

# ============================================================
# TRAIN TEST SPLIT WITH LINEAR REGRESSION
# ============================================================

from sklearn.model_selection import train_test_split

X = data[["StudyHours"]]

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

print("\nTest Predictions")

print(predictions)

# ============================================================
# MODEL ACCURACY USING R² SCORE
# ============================================================

score = model.score(X_test, y_test)

print("\nR² Score =", score)

# ============================================================
# VISUALIZING LINEAR REGRESSION
# ============================================================

import matplotlib.pyplot as plt

X = [[1], [2], [3], [4], [5]]

y = [10, 20, 30, 40, 50]

model = LinearRegression()

model.fit(X, y)

predicted_line = model.predict(X)

plt.scatter(X, y)

plt.plot(X, predicted_line)

plt.title("Linear Regression Line")

plt.xlabel("X")

plt.ylabel("Y")

plt.show()

# ============================================================
# PRACTICAL EXAMPLE 1
# STUDENT MARKS PREDICTION
# ============================================================

students = pd.DataFrame({
    "Hours": [1, 2, 3, 4, 5, 6],
    "Marks": [30, 40, 50, 60, 70, 80]
})

X = students[["Hours"]]

y = students["Marks"]

model = LinearRegression()

model.fit(X, y)

predicted_marks = model.predict([[7]])

print("\nStudent Example")

print("Predicted Marks =", predicted_marks)

# ============================================================
# PRACTICAL EXAMPLE 2
# HOUSE PRICE PREDICTION
# ============================================================

houses = pd.DataFrame({
    "Area": [1000, 1200, 1400, 1600, 1800],
    "Price": [20, 25, 30, 35, 40]
})

X = houses[["Area"]]

y = houses["Price"]

model = LinearRegression()

model.fit(X, y)

predicted_price = model.predict([[2000]])

print("\nHouse Example")

print("Predicted Price =", predicted_price)

# ============================================================
# PRACTICAL EXAMPLE 3
# SALES FORECASTING
# ============================================================

sales = pd.DataFrame({
    "Month": [1, 2, 3, 4, 5],
    "Sales": [100, 120, 140, 160, 180]
})

X = sales[["Month"]]

y = sales["Sales"]

model = LinearRegression()

model.fit(X, y)

future_sales = model.predict([[6]])

print("\nSales Forecast")

print("Month 6 Sales =", future_sales)

# ============================================================
# MULTIPLE LINEAR REGRESSION
# ============================================================

data = pd.DataFrame({
    "Area": [1000, 1200, 1400, 1600],
    "Bedrooms": [2, 3, 3, 4],
    "Price": [20, 25, 30, 35]
})

X = data[["Area", "Bedrooms"]]

y = data["Price"]

model = LinearRegression()

model.fit(X, y)

prediction = model.predict([
    [1800, 4]
])

print("\nMultiple Linear Regression")

print("Predicted Price =", prediction)

# ============================================================
# ADVANTAGES
# ============================================================

# ✔ Simple to Understand
# ✔ Fast Training
# ✔ Easy Interpretation
# ✔ Works Well on Linear Data

# ============================================================
# LIMITATIONS
# ============================================================

# ✘ Assumes Linear Relationship
# ✘ Sensitive to Outliers
# ✘ Poor on Complex Data
# ✘ Can Underfit

# ============================================================
# SUMMARY
# ============================================================

print("""
LINEAR REGRESSION SUMMARY

Import:

from sklearn.linear_model import LinearRegression

Create Model:

model = LinearRegression()

Train Model:

model.fit(X, y)

Predict:

model.predict([[value]])

Important Attributes:

model.coef_
model.intercept_

Evaluation:

model.score(X_test, y_test)

Equation:

y = mx + c

Uses:

✔ House Price Prediction
✔ Salary Prediction
✔ Marks Prediction
✔ Sales Forecasting

Benefits:

✔ Simple
✔ Fast
✔ Easy to Interpret
✔ Beginner Friendly
""")
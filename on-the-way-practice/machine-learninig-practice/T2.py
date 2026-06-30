"""02. Linear Regression
Goal

Predict a continuous value.

Task 1

Dataset

Auto MPG

https://archive.ics.uci.edu/ml/datasets/auto+mpg

Target

mpg

Features

horsepower
weight
cylinders
displacement

Requirements

Train Linear Regression
Plot actual vs predicted
Find:
MAE
MSE
RMSE
R² Score
Task 2

Predict Student Marks

Dataset

https://www.kaggle.com/datasets/spscientist/students-performance-in-exams

Target

math score

Features

reading score
writing score

Questions

Which feature influences math score more?
Interpret coefficients.
Bonus

Implement Linear Regression using Gradient Descent from scratch."""

import pandas as pd

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_absolute_error,mean_squared_error

import numpy as np

columns = [
    "mpg",
    "cylinders",
    "displacement",
    "horsepower",
    "weight",
    "acceleration",
    "model_year",
    "origin",
    "car_name"
]

df = pd.read_csv(
    "data/auto-mpg.data",
    sep=r"\s+",
    names=columns,
    na_values="?"
)

print(df.head())

# Check for missing values
print(df.isnull().sum())

# Convert horsepower to numeric (if needed)
df["horsepower"] = pd.to_numeric(df["horsepower"], errors="coerce")

# Fill missing values with the median
df["horsepower"] = df["horsepower"].fillna(df["horsepower"].median())

X=df[["horsepower","weight","cylinders","displacement"]]
y=df["mpg"]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    random_state=5,
    train_size=0.8
)

print("X-Train",X_train.shape)
print("X-Test",X_test.shape)
print("Y-Train",y_train.shape)
print("Y-Test",y_test.shape)

model=LinearRegression()

model.fit(X_train,y_train)

print("Model Trained Successfully")

predictions=model.predict(X_test)

score=model.score(X_test,y_test)

mae=mean_absolute_error(y_test,predictions)

mse=mean_squared_error(y_test,predictions)

rmse=np.sqrt(mse)

print("R score:",score)
print("Mean Absolute Error:",mae)
print("Mean Squared Error:",mse)
print("Root Mean Square Error:",rmse)


plt.figure(figsize=(7,5))

plt.scatter(y_test, predictions)

plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    color="red"
)

plt.xlabel("Actual MPG")
plt.ylabel("Predicted MPG")
plt.title("Actual vs Predicted MPG")

plt.show()







"""
01. Train-Test Split
Goal

Understand why we split data and how overfitting happens.

Task 1 (Easy)

Predict house prices.

Dataset:
https://www.kaggle.com/datasets/harlfoxem/housesalesprediction

Columns:

bedrooms
bathrooms
sqft_living
floors
price (Target)
Requirements
Load dataset
Select 4-5 features
Split into:
70-30
80-20
90-10
Print shapes
Compare model performance for every split.

Questions

Which split gave the best result?
Why shouldn't we train on the whole dataset?
What happens if test size becomes too small?
Task 2

Shuffle=False

vs

Shuffle=True

Observe the difference.

"""

import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt

df=pd.read_csv("C:/Users/ADMIN/Desktop/ai-engineering-journey/on-the-way-practice/machine-learninig-practice/data/kc_house_data.csv")


X = df[[
    "bedrooms",
    "sqft_living",
    "sqft_lot",
    "sqft_above",
    "sqft_basement",
    "yr_built",
    "zipcode"
]]
y=df["price"]

X_train, X_test ,y_train ,y_test=train_test_split(
    X,
    y,
    train_size=0.75,
    random_state=15

)

print("Xtrain:",X_train.shape)
print("Xtest",X_test.shape)
print("ytrain",y_train.shape)
print("ytest",y_test.shape)

model=LinearRegression()

model.fit(X_train,y_train)

print("Model Trained sucessfulyy")

predictions=model.predict(X_test)

print("Predictions")
print(predictions[:10])
print(model.intercept_)
print(model.coef_[0])

score=model.score(X_test,y_test)
print(f"R² Score: {score:.2f}")

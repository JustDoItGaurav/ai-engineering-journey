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
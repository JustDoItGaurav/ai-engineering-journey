# ============================================================
# TRAINING LOOP IN PYTORCH
# ============================================================

# A Training Loop is the process through which
# a Neural Network learns from data.
#
# Every Deep Learning model follows:
#
# 1. Forward Pass
# 2. Calculate Loss
# 3. Backward Pass
# 4. Update Weights
# 5. Repeat
#
# Why?
#
# ✔ Learn Patterns
# ✔ Reduce Errors
# ✔ Improve Predictions
# ✔ Core of Deep Learning
#
# Install:
#
# pip install torch

import torch
import torch.nn as nn
import torch.optim as optim

# ============================================================
# SAMPLE DATASET
# ============================================================

# Study Hours → Marks

X = torch.tensor([
    [1.0],
    [2.0],
    [3.0],
    [4.0],
    [5.0]
])

y = torch.tensor([
    [30.0],
    [40.0],
    [50.0],
    [60.0],
    [70.0]
])

print("Input Shape :", X.shape)

print("Target Shape:", y.shape)

# ============================================================
# BUILDING A MODEL
# ============================================================

model = nn.Linear(
    in_features=1,
    out_features=1
)

print("\nModel")

print(model)

# ============================================================
# FORWARD PASS
# ============================================================

# Model makes predictions.

predictions = model(X)

print("\nPredictions Before Training")

print(predictions)

# ============================================================
# LOSS FUNCTION
# ============================================================

# Loss measures how wrong
# the model predictions are.
#
# Smaller Loss = Better Model

loss_function = nn.MSELoss()

loss = loss_function(
    predictions,
    y
)

print("\nInitial Loss")

print(loss.item())

# ============================================================
# OPTIMIZER
# ============================================================

# Optimizer updates model weights.

optimizer = optim.SGD(
    model.parameters(),
    lr=0.01
)

print("\nOptimizer")

print(optimizer)

# ============================================================
# BASIC TRAINING LOOP
# ============================================================

epochs = 10

for epoch in range(epochs):

    # Forward Pass

    predictions = model(X)

    # Calculate Loss

    loss = loss_function(
        predictions,
        y
    )

    # Clear Previous Gradients

    optimizer.zero_grad()

    # Backward Pass

    loss.backward()

    # Update Weights

    optimizer.step()

    print(
        f"Epoch {epoch+1} | Loss: {loss.item():.4f}"
    )

# ============================================================
# PREDICTIONS AFTER TRAINING
# ============================================================

predictions = model(X)

print("\nPredictions After Training")

print(predictions)

# ============================================================
# UNDERSTANDING GRADIENTS
# ============================================================

# Gradients tell us:
#
# Which direction to move weights
# to reduce the loss.

model = nn.Linear(1, 1)

predictions = model(X)

loss = loss_function(
    predictions,
    y
)

loss.backward()

print("\nGradients")

for parameter in model.parameters():

    print(parameter.grad)

# ============================================================
# TRAINING FOR MORE EPOCHS
# ============================================================

model = nn.Linear(1, 1)

optimizer = optim.SGD(
    model.parameters(),
    lr=0.01
)

epochs = 100

for epoch in range(epochs):

    predictions = model(X)

    loss = loss_function(
        predictions,
        y
    )

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

print("\nFinal Loss")

print(loss.item())

# ============================================================
# LEARNING RATE
# ============================================================

# Learning Rate controls
# how big each update step is.
#
# Small LR:
#
# Slow Learning
#
# Large LR:
#
# Can overshoot optimum

optimizer = optim.SGD(
    model.parameters(),
    lr=0.1
)

print("\nLearning Rate Example")

print(optimizer)

# ============================================================
# USING ADAM OPTIMIZER
# ============================================================

# Adam is the most popular optimizer.

optimizer = optim.Adam(
    model.parameters(),
    lr=0.01
)

print("\nAdam Optimizer")

print(optimizer)

# ============================================================
# PRACTICAL EXAMPLE 1
# STUDENT MARKS PREDICTION
# ============================================================

hours = torch.tensor([
    [2.0],
    [4.0],
    [6.0],
    [8.0]
])

marks = torch.tensor([
    [35.0],
    [50.0],
    [70.0],
    [90.0]
])

model = nn.Linear(1, 1)

optimizer = optim.SGD(
    model.parameters(),
    lr=0.01
)

loss_function = nn.MSELoss()

for epoch in range(100):

    predictions = model(hours)

    loss = loss_function(
        predictions,
        marks
    )

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

print("\nStudent Prediction")

print(model(
    torch.tensor([[5.0]])
))

# ============================================================
# PRACTICAL EXAMPLE 2
# HOUSE PRICE PREDICTION
# ============================================================

areas = torch.tensor([
    [1000.0],
    [1200.0],
    [1500.0],
    [1800.0]
])

prices = torch.tensor([
    [20.0],
    [25.0],
    [30.0],
    [40.0]
])

model = nn.Linear(1, 1)

optimizer = optim.Adam(
    model.parameters(),
    lr=0.01
)

for epoch in range(200):

    predictions = model(areas)

    loss = loss_function(
        predictions,
        prices
    )

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

print("\nHouse Price Prediction")

print(model(
    torch.tensor([[1600.0]])
))

# ============================================================
# PRACTICAL EXAMPLE 3
# SALES PREDICTION
# ============================================================

advertising = torch.tensor([
    [10.0],
    [20.0],
    [30.0],
    [40.0]
])

sales = torch.tensor([
    [100.0],
    [200.0],
    [300.0],
    [400.0]
])

model = nn.Linear(1, 1)

optimizer = optim.SGD(
    model.parameters(),
    lr=0.01
)

for epoch in range(100):

    predictions = model(advertising)

    loss = loss_function(
        predictions,
        sales
    )

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

print("\nSales Prediction")

print(model(
    torch.tensor([[25.0]])
))

# ============================================================
# COMMON LOSS FUNCTIONS
# ============================================================

# nn.MSELoss()
# nn.L1Loss()
# nn.CrossEntropyLoss()
# nn.BCELoss()

# ============================================================
# COMMON OPTIMIZERS
# ============================================================

# optim.SGD()
# optim.Adam()
# optim.RMSprop()

# ============================================================
# TRAINING LOOP STRUCTURE
# ============================================================

# predictions = model(X)
#
# loss = loss_function(
#     predictions,
#     y
# )
#
# optimizer.zero_grad()
#
# loss.backward()
#
# optimizer.step()

# ============================================================
# SUMMARY
# ============================================================

print("""
TRAINING LOOP SUMMARY

Forward Pass:

predictions = model(X)

Calculate Loss:

loss = loss_function(
    predictions,
    y
)

Clear Gradients:

optimizer.zero_grad()

Backward Pass:

loss.backward()

Update Weights:

optimizer.step()

Popular Loss Functions:

nn.MSELoss()
nn.CrossEntropyLoss()

Popular Optimizers:

optim.SGD()
optim.Adam()

Important Concepts:

✔ Forward Pass
✔ Loss Function
✔ Backpropagation
✔ Gradients
✔ Optimizer
✔ Learning Rate
✔ Epochs

Applications:

✔ Deep Learning
✔ Computer Vision
✔ NLP
✔ Recommendation Systems
✔ Generative AI

Benefits:

✔ Learns From Data
✔ Improves Predictions
✔ Reduces Error
✔ Foundation of AI Training
""")
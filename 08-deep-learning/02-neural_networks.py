# ============================================================
# NEURAL NETWORKS IN PYTORCH
# ============================================================

# A Neural Network is a machine learning model inspired by
# the human brain.
#
# It learns patterns from data using layers of neurons.
#
# Components:
#
# 1. Input Layer
# 2. Hidden Layer(s)
# 3. Output Layer
#
# Why Neural Networks?
#
# ✔ Learn Complex Patterns
# ✔ Power Deep Learning
# ✔ Used in AI Applications
# ✔ Foundation of Transformers
#
# Install:
#
# pip install torch

import torch
import torch.nn as nn

# ============================================================
# WHAT IS A NEURON?
# ============================================================

# Formula:
#
# output = (input × weight) + bias
#
# y = wx + b

x = torch.tensor([5.0])

weight = torch.tensor([2.0])

bias = torch.tensor([1.0])

output = (x * weight) + bias

print("Neuron Output:", output)

# ============================================================
# USING nn.Linear
# ============================================================

# nn.Linear automatically performs:
#
# y = wx + b

layer = nn.Linear(
    in_features=1,
    out_features=1
)

sample = torch.tensor([[10.0]])

prediction = layer(sample)

print("\nLinear Layer Output")

print(prediction)

# ============================================================
# UNDERSTANDING INPUT SHAPES
# ============================================================

# Shape:
#
# (batch_size, features)

batch = torch.tensor([
    [10.0],
    [20.0],
    [30.0]
])

print("\nInput Shape")

print(batch.shape)

# ============================================================
# MULTIPLE INPUT FEATURES
# ============================================================

# Example:
#
# Age
# Salary
# Experience

data = torch.tensor([
    [25.0, 30000.0, 2.0],
    [30.0, 50000.0, 5.0]
])

layer = nn.Linear(
    in_features=3,
    out_features=1
)

output = layer(data)

print("\nMultiple Features Output")

print(output)

# ============================================================
# SEQUENTIAL MODEL
# ============================================================

# Sequential allows stacking layers.

model = nn.Sequential(
    nn.Linear(2, 4),
    nn.Linear(4, 1)
)

sample = torch.tensor([
    [10.0, 20.0]
])

output = model(sample)

print("\nSequential Model Output")

print(output)

# ============================================================
# WHY HIDDEN LAYERS?
# ============================================================

# Hidden layers help learn complex relationships.

model = nn.Sequential(
    nn.Linear(2, 8),
    nn.Linear(8, 4),
    nn.Linear(4, 1)
)

sample = torch.tensor([
    [1.0, 2.0]
])

output = model(sample)

print("\nDeep Network Output")

print(output)

# ============================================================
# ACTIVATION FUNCTIONS
# ============================================================

# Without activation functions,
# neural networks behave like
# simple linear models.

# Popular Activations:
#
# ReLU
# Sigmoid
# Tanh

# ============================================================
# RELU ACTIVATION
# ============================================================

relu = nn.ReLU()

x = torch.tensor([
    -5.0,
    -2.0,
    0.0,
    5.0,
    10.0
])

print("\nReLU Output")

print(relu(x))

# ============================================================
# SIGMOID ACTIVATION
# ============================================================

sigmoid = nn.Sigmoid()

print("\nSigmoid Output")

print(sigmoid(x))

# ============================================================
# TANH ACTIVATION
# ============================================================

tanh = nn.Tanh()

print("\nTanh Output")

print(tanh(x))

# ============================================================
# BUILDING A SIMPLE NEURAL NETWORK
# ============================================================

class SimpleNN(nn.Module):

    def __init__(self):
        super().__init__()

        self.layer1 = nn.Linear(2, 8)

        self.relu = nn.ReLU()

        self.layer2 = nn.Linear(8, 1)

    def forward(self, x):

        x = self.layer1(x)

        x = self.relu(x)

        x = self.layer2(x)

        return x

model = SimpleNN()

sample = torch.tensor([
    [10.0, 20.0]
])

output = model(sample)

print("\nCustom Neural Network")

print(output)

# ============================================================
# VIEWING MODEL STRUCTURE
# ============================================================

print("\nModel Architecture")

print(model)

# ============================================================
# MODEL PARAMETERS
# ============================================================

print("\nModel Parameters")

for parameter in model.parameters():

    print(parameter.shape)

# ============================================================
# PRACTICAL EXAMPLE 1
# STUDENT PERFORMANCE
# ============================================================

# Inputs:
#
# Study Hours
# Attendance

students = torch.tensor([
    [2.0, 60.0],
    [4.0, 75.0],
    [6.0, 85.0],
    [8.0, 95.0]
])

model = nn.Sequential(
    nn.Linear(2, 8),
    nn.ReLU(),
    nn.Linear(8, 1)
)

predictions = model(students)

print("\nStudent Predictions")

print(predictions)

# ============================================================
# PRACTICAL EXAMPLE 2
# HOUSE PRICE FEATURES
# ============================================================

# Inputs:
#
# Area
# Bedrooms

houses = torch.tensor([
    [1000.0, 2.0],
    [1500.0, 3.0],
    [2000.0, 4.0]
])

predictions = model(houses)

print("\nHouse Predictions")

print(predictions)

# ============================================================
# PRACTICAL EXAMPLE 3
# CUSTOMER DATA
# ============================================================

# Inputs:
#
# Age
# Salary

customers = torch.tensor([
    [20.0, 25000.0],
    [30.0, 50000.0],
    [40.0, 80000.0]
])

predictions = model(customers)

print("\nCustomer Predictions")

print(predictions)

# ============================================================
# COMMON LAYERS
# ============================================================

# nn.Linear()
# nn.ReLU()
# nn.Sigmoid()
# nn.Tanh()
# nn.Sequential()

# ============================================================
# COMMON TERMS
# ============================================================

# Neuron
# Weight
# Bias
# Hidden Layer
# Output Layer
# Activation Function
# Forward Pass

# ============================================================
# SUMMARY
# ============================================================

print("""
NEURAL NETWORKS SUMMARY

Import:

import torch
import torch.nn as nn

Popular Layers:

nn.Linear()
nn.ReLU()
nn.Sigmoid()
nn.Tanh()

Build Model:

nn.Sequential()

or

class MyModel(nn.Module)

Core Concepts:

✔ Neuron
✔ Weight
✔ Bias
✔ Hidden Layer
✔ Output Layer
✔ Activation Function
✔ Forward Pass

Applications:

✔ Deep Learning
✔ Computer Vision
✔ NLP
✔ Recommendation Systems
✔ Generative AI

Benefits:

✔ Learns Complex Patterns
✔ Handles Large Data
✔ Foundation of Modern AI
✔ Used in Transformers
""")
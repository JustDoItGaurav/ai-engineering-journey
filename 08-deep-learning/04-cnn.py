# ============================================================
# CONVOLUTIONAL NEURAL NETWORKS (CNN)
# ============================================================

# CNN stands for:
#
# Convolutional Neural Network
#
# CNNs are mainly used for:
#
# 1. Image Classification
# 2. Object Detection
# 3. Face Recognition
# 4. Medical Imaging
# 5. Computer Vision
#
# Why CNN?
#
# ✔ Automatically Extract Features
# ✔ Excellent for Images
# ✔ Reduces Number of Parameters
# ✔ Learns Patterns Efficiently
#
# Install:
#
# pip install torch

import torch
import torch.nn as nn

# ============================================================
# IMAGES AS TENSORS
# ============================================================

# Images are represented as:
#
# (Channels, Height, Width)
#
# Example:
#
# RGB Image
#
# (3, 224, 224)

image = torch.rand(
    3,
    224,
    224
)

print("Image Shape")

print(image.shape)

# ============================================================
# BATCH OF IMAGES
# ============================================================

# Deep Learning models process
# multiple images together.
#
# Shape:
#
# (Batch Size, Channels, Height, Width)

batch = torch.rand(
    32,
    3,
    224,
    224
)

print("\nBatch Shape")

print(batch.shape)

# ============================================================
# WHAT IS A CONVOLUTION?
# ============================================================

# Convolution uses small filters
# to detect patterns.
#
# Examples:
#
# Edges
# Corners
# Shapes
# Textures

# ============================================================
# CONVOLUTION LAYER
# ============================================================

conv = nn.Conv2d(
    in_channels=3,
    out_channels=16,
    kernel_size=3
)

output = conv(batch)

print("\nConv Output Shape")

print(output.shape)

# ============================================================
# UNDERSTANDING PARAMETERS
# ============================================================

# in_channels
#
# Number of input channels
#
# RGB = 3
#
# Grayscale = 1
#
# out_channels
#
# Number of filters
#
# kernel_size
#
# Filter size

# ============================================================
# MULTIPLE FILTERS
# ============================================================

conv = nn.Conv2d(
    in_channels=3,
    out_channels=32,
    kernel_size=3
)

output = conv(batch)

print("\nMultiple Filters")

print(output.shape)

# ============================================================
# ACTIVATION FUNCTION
# ============================================================

relu = nn.ReLU()

activated = relu(output)

print("\nReLU Output")

print(activated.shape)

# ============================================================
# MAX POOLING
# ============================================================

# Pooling reduces image size.
#
# Benefits:
#
# Faster Training
# Less Memory
# Better Generalization

pool = nn.MaxPool2d(
    kernel_size=2
)

pooled = pool(activated)

print("\nPooled Shape")

print(pooled.shape)

# ============================================================
# COMPLETE CNN BLOCK
# ============================================================

cnn_block = nn.Sequential(

    nn.Conv2d(
        3,
        16,
        kernel_size=3
    ),

    nn.ReLU(),

    nn.MaxPool2d(2)

)

output = cnn_block(batch)

print("\nCNN Block Output")

print(output.shape)

# ============================================================
# FLATTENING
# ============================================================

# Before entering a fully connected layer,
# CNN outputs are flattened.

flatten = nn.Flatten()

flat_output = flatten(output)

print("\nFlattened Output")

print(flat_output.shape)

# ============================================================
# FULLY CONNECTED LAYER
# ============================================================

fc = nn.Linear(
    flat_output.shape[1],
    10
)

prediction = fc(flat_output)

print("\nFinal Prediction Shape")

print(prediction.shape)

# ============================================================
# BUILDING A SIMPLE CNN
# ============================================================

class SimpleCNN(nn.Module):

    def __init__(self):

        super().__init__()

        self.features = nn.Sequential(

            nn.Conv2d(
                3,
                16,
                kernel_size=3
            ),

            nn.ReLU(),

            nn.MaxPool2d(2),

            nn.Conv2d(
                16,
                32,
                kernel_size=3
            ),

            nn.ReLU(),

            nn.MaxPool2d(2)

        )

        self.flatten = nn.Flatten()

        self.classifier = nn.Linear(
            32 * 54 * 54,
            10
        )

    def forward(self, x):

        x = self.features(x)

        x = self.flatten(x)

        x = self.classifier(x)

        return x

# ============================================================
# MODEL CREATION
# ============================================================

model = SimpleCNN()

print("\nCNN Architecture")

print(model)

# ============================================================
# FORWARD PASS
# ============================================================

sample_images = torch.rand(
    8,
    3,
    224,
    224
)

predictions = model(sample_images)

print("\nPredictions Shape")

print(predictions.shape)

# ============================================================
# IMAGE CLASSIFICATION OUTPUT
# ============================================================

# Example:
#
# 10 Classes
#
# Output:
#
# [0.1, 0.8, 0.05, ...]

print("\nSample Prediction")

print(predictions[0])

# ============================================================
# PRACTICAL EXAMPLE 1
# CAT VS DOG CLASSIFIER
# ============================================================

images = torch.rand(
    16,
    3,
    224,
    224
)

labels = torch.randint(
    0,
    2,
    (16,)
)

print("\nCat vs Dog Dataset")

print("Images Shape:", images.shape)

print("Labels Shape:", labels.shape)

# ============================================================
# PRACTICAL EXAMPLE 2
# HANDWRITTEN DIGITS
# ============================================================

digits = torch.rand(
    32,
    1,
    28,
    28
)

print("\nMNIST Dataset")

print(digits.shape)

# ============================================================
# PRACTICAL EXAMPLE 3
# MEDICAL IMAGE DATA
# ============================================================

medical_images = torch.rand(
    64,
    1,
    256,
    256
)

print("\nMedical Images")

print(medical_images.shape)

# ============================================================
# COMMON CNN LAYERS
# ============================================================

# nn.Conv2d()
# nn.MaxPool2d()
# nn.ReLU()
# nn.Flatten()
# nn.Linear()

# ============================================================
# COMMON TERMS
# ============================================================

# Kernel
# Filter
# Feature Map
# Pooling
# Flattening
# Channels
# Convolution

# ============================================================
# CNN FLOW
# ============================================================

# Image
# ↓
# Conv Layer
# ↓
# ReLU
# ↓
# Pooling
# ↓
# Conv Layer
# ↓
# ReLU
# ↓
# Pooling
# ↓
# Flatten
# ↓
# Linear Layer
# ↓
# Prediction

# ============================================================
# SUMMARY
# ============================================================

print("""
CNN SUMMARY

Import:

import torch
import torch.nn as nn

Popular Layers:

nn.Conv2d()
nn.MaxPool2d()
nn.ReLU()
nn.Flatten()
nn.Linear()

Image Shape:

(Channels, Height, Width)

Batch Shape:

(Batch, Channels, Height, Width)

Important Concepts:

✔ Convolution
✔ Filters
✔ Feature Maps
✔ Pooling
✔ Flattening
✔ Image Classification

Applications:

✔ Face Recognition
✔ Object Detection
✔ Medical Imaging
✔ Self Driving Cars
✔ Computer Vision

Benefits:

✔ Automatic Feature Extraction
✔ High Accuracy
✔ Efficient Learning
✔ Industry Standard
""")
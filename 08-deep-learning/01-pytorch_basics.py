# ============================================================
# PYTORCH BASICS
# ============================================================

# PyTorch is one of the most popular Deep Learning libraries.
#
# It is used for:
#
# 1. Neural Networks
# 2. Computer Vision
# 3. Natural Language Processing
# 4. Transformers
# 5. Generative AI
#
# Why Learn PyTorch?
#
# ✔ Industry Standard
# ✔ Easy to Learn
# ✔ GPU Support
# ✔ Deep Learning Framework
# ✔ Used in AI Research
#
# Install:
#
# pip install torch

import torch

# ============================================================
# CHECK PYTORCH VERSION
# ============================================================

print("PyTorch Version:", torch.__version__)

# ============================================================
# CREATING A TENSOR
# ============================================================

# Tensor is the basic data structure in PyTorch.
#
# Similar to:
#
# List
# NumPy Array
#
# But optimized for Deep Learning.

tensor = torch.tensor([1, 2, 3, 4, 5])

print("\nBasic Tensor")
print(tensor)

# ============================================================
# TENSOR DATA TYPE
# ============================================================

print("\nTensor Data Type")

print(tensor.dtype)

# ============================================================
# TENSOR SHAPE
# ============================================================

print("\nTensor Shape")

print(tensor.shape)

# ============================================================
# SCALAR TENSOR (0D)
# ============================================================

scalar = torch.tensor(10)

print("\nScalar Tensor")

print(scalar)

print("Dimension:", scalar.ndim)

# ============================================================
# VECTOR TENSOR (1D)
# ============================================================

vector = torch.tensor([10, 20, 30])

print("\nVector Tensor")

print(vector)

print("Dimension:", vector.ndim)

# ============================================================
# MATRIX TENSOR (2D)
# ============================================================

matrix = torch.tensor([
    [1, 2],
    [3, 4]
])

print("\nMatrix Tensor")

print(matrix)

print("Dimension:", matrix.ndim)

# ============================================================
# 3D TENSOR
# ============================================================

tensor_3d = torch.tensor([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print("\n3D Tensor")

print(tensor_3d)

print("Dimension:", tensor_3d.ndim)

# ============================================================
# TENSOR ATTRIBUTES
# ============================================================

print("\nTensor Attributes")

print("Shape :", tensor_3d.shape)
print("Dtype :", tensor_3d.dtype)
print("Device:", tensor_3d.device)

# ============================================================
# ZEROS TENSOR
# ============================================================

zeros = torch.zeros((3, 3))

print("\nZeros Tensor")

print(zeros)

# ============================================================
# ONES TENSOR
# ============================================================

ones = torch.ones((3, 3))

print("\nOnes Tensor")

print(ones)

# ============================================================
# RANDOM TENSOR
# ============================================================

random_tensor = torch.rand((2, 3))

print("\nRandom Tensor")

print(random_tensor)

# ============================================================
# TENSOR ADDITION
# ============================================================

a = torch.tensor([1, 2, 3])

b = torch.tensor([4, 5, 6])

print("\nAddition")

print(a + b)

# ============================================================
# TENSOR SUBTRACTION
# ============================================================

print("\nSubtraction")

print(a - b)

# ============================================================
# TENSOR MULTIPLICATION
# ============================================================

print("\nMultiplication")

print(a * b)

# ============================================================
# MATRIX MULTIPLICATION
# ============================================================

matrix1 = torch.tensor([
    [1, 2],
    [3, 4]
])

matrix2 = torch.tensor([
    [5, 6],
    [7, 8]
])

print("\nMatrix Multiplication")

print(torch.matmul(matrix1, matrix2))

# ============================================================
# RESHAPING TENSORS
# ============================================================

x = torch.arange(12)

print("\nOriginal Tensor")

print(x)

reshaped = x.reshape(3, 4)

print("\nReshaped Tensor")

print(reshaped)

# ============================================================
# TENSOR INDEXING
# ============================================================

numbers = torch.tensor([
    [10, 20, 30],
    [40, 50, 60]
])

print("\nTensor Indexing")

print(numbers[0])

print(numbers[1])

print(numbers[0][1])

# ============================================================
# NUMPY TO TENSOR
# ============================================================

import numpy as np

arr = np.array([1, 2, 3])

tensor_from_numpy = torch.from_numpy(arr)

print("\nNumPy To Tensor")

print(tensor_from_numpy)

# ============================================================
# TENSOR TO NUMPY
# ============================================================

tensor = torch.tensor([5, 10, 15])

numpy_array = tensor.numpy()

print("\nTensor To NumPy")

print(numpy_array)

# ============================================================
# CPU VS GPU
# ============================================================

print("\nGPU Available?")

print(torch.cuda.is_available())

# ============================================================
# PRACTICAL EXAMPLE 1
# STUDENT MARKS
# ============================================================

study_hours = torch.tensor([
    [1],
    [2],
    [3],
    [4],
    [5]
])

marks = torch.tensor([
    [30],
    [40],
    [55],
    [70],
    [90]
])

print("\nStudent Dataset")

print("Study Hours")

print(study_hours)

print("Marks")

print(marks)

# ============================================================
# PRACTICAL EXAMPLE 2
# IMAGE REPRESENTATION
# ============================================================

image = torch.rand((224, 224, 3))

print("\nImage Tensor")

print(image.shape)

# ============================================================
# PRACTICAL EXAMPLE 3
# BATCH OF DATA
# ============================================================

batch = torch.rand((32, 10))

print("\nBatch Shape")

print(batch.shape)

# 32 samples
# 10 features

# ============================================================
# COMMON FUNCTIONS
# ============================================================

# torch.tensor()
# torch.zeros()
# torch.ones()
# torch.rand()
# torch.arange()
# torch.reshape()
# torch.matmul()
# torch.from_numpy()
# tensor.numpy()

# ============================================================
# SUMMARY
# ============================================================

print("""
PYTORCH BASICS SUMMARY

Import:

import torch

Create Tensor:

torch.tensor()

Common Functions:

torch.zeros()
torch.ones()
torch.rand()
torch.arange()
torch.reshape()
torch.matmul()

Important Concepts:

✔ Tensor
✔ Shape
✔ Dimension
✔ Data Type
✔ Indexing
✔ Reshaping
✔ Matrix Multiplication

Applications:

✔ Deep Learning
✔ Computer Vision
✔ NLP
✔ Transformers
✔ Generative AI

Benefits:

✔ Fast
✔ GPU Support
✔ Industry Standard
✔ Easy Integration
✔ Production Ready
""")
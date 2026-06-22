# ============================================================
# ATTENTION MECHANISM
# ============================================================

# Attention is the most important concept
# behind modern AI models.
#
# Used in:
#
# GPT
# Gemini
# Claude
# Llama
# DeepSeek
#
# Why Attention?
#
# Before Attention:
#
# RNN
# LSTM
#
# Problems:
#
# ✔ Forget long context
# ✔ Slow training
# ✔ Difficult scaling
#
# Attention solved these issues.
#
# Key Idea:
#
# Focus on the most important information.

import torch
import torch.nn.functional as F

# ============================================================
# UNDERSTANDING ATTENTION
# ============================================================

# Imagine:
#
# "The cat sat on the mat because it was tired."
#
# What does "it" refer to?
#
# Attention helps the model focus on:
#
# cat
#
# instead of every word equally.

# ============================================================
# QUERY KEY VALUE
# ============================================================

# Every token produces:
#
# Query (Q)
# Key   (K)
# Value (V)
#
# Think:
#
# Query:
# What am I looking for?
#
# Key:
# What information do I contain?
#
# Value:
# Actual information to return.

# ============================================================
# SIMPLE EXAMPLE
# ============================================================

query = torch.tensor([
    [1.0, 0.0]
])

key = torch.tensor([
    [1.0, 0.0]
])

value = torch.tensor([
    [10.0, 20.0]
])

print("Query")
print(query)

print("\nKey")
print(key)

print("\nValue")
print(value)

# ============================================================
# ATTENTION SCORE
# ============================================================

# Score =
#
# Query × Keyᵀ

score = torch.matmul(
    query,
    key.T
)

print("\nAttention Score")

print(score)

# ============================================================
# MULTIPLE TOKENS
# ============================================================

queries = torch.tensor([
    [1.0, 0.0],
    [0.0, 1.0]
])

keys = torch.tensor([
    [1.0, 0.0],
    [0.0, 1.0]
])

scores = torch.matmul(
    queries,
    keys.T
)

print("\nMultiple Token Scores")

print(scores)

# ============================================================
# SOFTMAX
# ============================================================

# Converts scores into probabilities.

attention_weights = F.softmax(
    scores,
    dim=-1
)

print("\nAttention Weights")

print(attention_weights)

# ============================================================
# VALUES
# ============================================================

values = torch.tensor([
    [10.0, 20.0],
    [30.0, 40.0]
])

print("\nValues")

print(values)

# ============================================================
# ATTENTION OUTPUT
# ============================================================

output = torch.matmul(
    attention_weights,
    values
)

print("\nAttention Output")

print(output)

# ============================================================
# SELF ATTENTION
# ============================================================

# Self Attention:
#
# Query
# Key
# Value
#
# all come from the same input.

tokens = torch.tensor([
    [1.0, 0.0],
    [0.0, 1.0],
    [1.0, 1.0]
])

Q = tokens

K = tokens

V = tokens

scores = torch.matmul(
    Q,
    K.T
)

weights = F.softmax(
    scores,
    dim=-1
)

output = torch.matmul(
    weights,
    V
)

print("\nSelf Attention Output")

print(output)

# ============================================================
# WHY SOFTMAX?
# ============================================================

# Softmax converts:
#
# [2, 4, 1]
#
# into:
#
# [0.11, 0.84, 0.05]
#
# allowing the model to focus more
# on important tokens.

sample_scores = torch.tensor([
    2.0,
    4.0,
    1.0
])

print("\nSoftmax Example")

print(
    F.softmax(
        sample_scores,
        dim=0
    )
)

# ============================================================
# SCALED DOT PRODUCT ATTENTION
# ============================================================

# Formula:
#
# Attention(Q,K,V)
#
# = Softmax(
#     QKᵀ / √d
#   )V
#
# This is the core of Transformers.

Q = torch.rand(
    3,
    4
)

K = torch.rand(
    3,
    4
)

V = torch.rand(
    3,
    4
)

d = K.shape[-1]

scores = torch.matmul(
    Q,
    K.T
)

scaled_scores = scores / (d ** 0.5)

weights = F.softmax(
    scaled_scores,
    dim=-1
)

output = torch.matmul(
    weights,
    V
)

print("\nScaled Attention Output")

print(output)

# ============================================================
# ATTENTION MATRIX
# ============================================================

print("\nAttention Matrix")

print(weights)

# ============================================================
# PRACTICAL EXAMPLE 1
# SENTENCE TOKENS
# ============================================================

sentence = torch.rand(
    5,
    8
)

scores = torch.matmul(
    sentence,
    sentence.T
)

weights = F.softmax(
    scores,
    dim=-1
)

output = torch.matmul(
    weights,
    sentence
)

print("\nSentence Attention")

print(output.shape)

# ============================================================
# PRACTICAL EXAMPLE 2
# WORD EMBEDDINGS
# ============================================================

embeddings = torch.rand(
    10,
    16
)

scores = torch.matmul(
    embeddings,
    embeddings.T
)

weights = F.softmax(
    scores,
    dim=-1
)

output = torch.matmul(
    weights,
    embeddings
)

print("\nEmbedding Attention")

print(output.shape)

# ============================================================
# PRACTICAL EXAMPLE 3
# MINI GPT STYLE INPUT
# ============================================================

tokens = torch.rand(
    20,
    32
)

scores = torch.matmul(
    tokens,
    tokens.T
)

weights = F.softmax(
    scores,
    dim=-1
)

output = torch.matmul(
    weights,
    tokens
)

print("\nMini GPT Example")

print(output.shape)

# ============================================================
# MULTI HEAD ATTENTION (CONCEPT)
# ============================================================

# Instead of one attention:
#
# Head 1
# Head 2
# Head 3
# Head 4
#
# Each head learns different patterns.
#
# Example:
#
# Head 1 → Grammar
# Head 2 → Relationships
# Head 3 → Context
# Head 4 → Meaning

# ============================================================
# WHY ATTENTION CHANGED AI
# ============================================================

# Attention enables:
#
# Long Context
# Parallel Processing
# Better Language Understanding
# Large Scale Training

# ============================================================
# COMMON TERMS
# ============================================================

# Query
# Key
# Value
# Attention Score
# Softmax
# Self Attention
# Multi Head Attention

# ============================================================
# ATTENTION FLOW
# ============================================================

# Input Tokens
#
# ↓
#
# Generate Q K V
#
# ↓
#
# Q × Kᵀ
#
# ↓
#
# Softmax
#
# ↓
#
# Attention Weights
#
# ↓
#
# Multiply V
#
# ↓
#
# Final Output

# ============================================================
# SUMMARY
# ============================================================

print("""
ATTENTION SUMMARY

Core Components:

Query (Q)
Key (K)
Value (V)

Attention Formula:

Softmax(QKᵀ)V

Scaled Attention:

Softmax(QKᵀ / √d)V

Important Concepts:

✔ Query
✔ Key
✔ Value
✔ Attention Scores
✔ Softmax
✔ Self Attention
✔ Multi Head Attention

Applications:

✔ GPT
✔ Gemini
✔ Claude
✔ Llama
✔ Transformers

Benefits:

✔ Long Context Understanding
✔ Better Language Modeling
✔ Parallel Processing
✔ Foundation of Modern AI
""")
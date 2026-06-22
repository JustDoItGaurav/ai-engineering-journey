# ============================================================
# TRANSFORMERS
# ============================================================

# Transformers are the foundation of modern AI.
#
# Used in:
#
# GPT
# ChatGPT
# Claude
# Gemini
# Llama
# DeepSeek
#
# Introduced In:
#
# "Attention Is All You Need" (2017)
#
# Why Transformers?
#
# ✔ Understand Long Context
# ✔ Parallel Processing
# ✔ Better Language Understanding
# ✔ Scalable Training
#
# Core Idea:
#
# Attention + Neural Networks

import torch
import torch.nn as nn

# ============================================================
# TRANSFORMER ARCHITECTURE
# ============================================================

# Input
#
# ↓
#
# Embedding
#
# ↓
#
# Positional Encoding
#
# ↓
#
# Multi Head Attention
#
# ↓
#
# Feed Forward Network
#
# ↓
#
# Output

# ============================================================
# TOKENS
# ============================================================

# Text is converted into tokens.
#
# Example:
#
# "I Love AI"
#
# →
#
# [101, 502, 888]

tokens = torch.tensor([
    [101, 502, 888]
])

print("Tokens")

print(tokens)

# ============================================================
# EMBEDDINGS
# ============================================================

# Embeddings convert tokens
# into vectors.

embedding = nn.Embedding(
    num_embeddings=1000,
    embedding_dim=16
)

embedded_tokens = embedding(tokens)

print("\nEmbeddings Shape")

print(embedded_tokens.shape)

# Shape:
#
# (Batch, Sequence Length, Embedding Size)

# ============================================================
# UNDERSTANDING EMBEDDINGS
# ============================================================

# Example:
#
# "King"
#
# →
#
# [0.2, -0.4, 0.9 ...]

print("\nSingle Token Embedding")

print(embedded_tokens[0][0])

# ============================================================
# POSITIONAL ENCODING
# ============================================================

# Attention does not know word order.
#
# Example:
#
# "Dog bites man"
#
# "Man bites dog"
#
# Same tokens, different meaning.
#
# Positional Encoding adds position information.

sequence_length = 5

embedding_size = 8

position_encoding = torch.rand(
    sequence_length,
    embedding_size
)

print("\nPositional Encoding")

print(position_encoding.shape)

# ============================================================
# ADD POSITIONAL ENCODING
# ============================================================

sample_embeddings = torch.rand(
    sequence_length,
    embedding_size
)

combined = sample_embeddings + position_encoding

print("\nEmbeddings + Position")

print(combined.shape)

# ============================================================
# MULTI HEAD ATTENTION
# ============================================================

# Instead of one attention mechanism,
# transformers use multiple heads.
#
# Benefits:
#
# Grammar
# Meaning
# Relationships
# Context

attention = nn.MultiheadAttention(
    embed_dim=16,
    num_heads=4,
    batch_first=True
)

output, weights = attention(
    embedded_tokens,
    embedded_tokens,
    embedded_tokens
)

print("\nAttention Output Shape")

print(output.shape)

print("\nAttention Weights Shape")

print(weights.shape)

# ============================================================
# FEED FORWARD NETWORK
# ============================================================

# After attention,
# each token passes through
# a small neural network.

feed_forward = nn.Sequential(

    nn.Linear(
        16,
        64
    ),

    nn.ReLU(),

    nn.Linear(
        64,
        16
    )

)

ff_output = feed_forward(output)

print("\nFeed Forward Output")

print(ff_output.shape)

# ============================================================
# TRANSFORMER BLOCK
# ============================================================

class TransformerBlock(nn.Module):

    def __init__(self):

        super().__init__()

        self.attention = nn.MultiheadAttention(
            embed_dim=16,
            num_heads=4,
            batch_first=True
        )

        self.feed_forward = nn.Sequential(

            nn.Linear(16, 64),

            nn.ReLU(),

            nn.Linear(64, 16)

        )

    def forward(self, x):

        attention_output, _ = self.attention(
            x,
            x,
            x
        )

        output = self.feed_forward(
            attention_output
        )

        return output

# ============================================================
# USING TRANSFORMER BLOCK
# ============================================================

block = TransformerBlock()

output = block(
    embedded_tokens
)

print("\nTransformer Block Output")

print(output.shape)

# ============================================================
# STACKING TRANSFORMER BLOCKS
# ============================================================

# Real models use many blocks.
#
# GPT-2 → 12+
# GPT-3 → 96+
# Llama → Multiple Layers

stack = nn.Sequential(

    TransformerBlock(),

    TransformerBlock(),

    TransformerBlock()

)

output = stack(
    embedded_tokens
)

print("\nStacked Transformer Output")

print(output.shape)

# ============================================================
# TRANSFORMER ENCODER
# ============================================================

encoder_layer = nn.TransformerEncoderLayer(

    d_model=16,

    nhead=4,

    batch_first=True

)

encoder = nn.TransformerEncoder(

    encoder_layer,

    num_layers=2

)

encoder_output = encoder(
    embedded_tokens
)

print("\nEncoder Output")

print(encoder_output.shape)

# ============================================================
# TRANSFORMER DECODER
# ============================================================

# Decoder predicts next token.
#
# Used in:
#
# GPT
# ChatGPT
# Claude
# Gemini

# ============================================================
# PRACTICAL EXAMPLE 1
# SENTENCE EMBEDDINGS
# ============================================================

sentence = torch.randint(
    0,
    1000,
    (1, 10)
)

embedded = embedding(
    sentence
)

output = block(
    embedded
)

print("\nSentence Output")

print(output.shape)

# ============================================================
# PRACTICAL EXAMPLE 2
# MINI CHATBOT INPUT
# ============================================================

chat_tokens = torch.randint(
    0,
    1000,
    (1, 20)
)

chat_embeddings = embedding(
    chat_tokens
)

output = block(
    chat_embeddings
)

print("\nChatbot Output")

print(output.shape)

# ============================================================
# PRACTICAL EXAMPLE 3
# DOCUMENT TOKENS
# ============================================================

document = torch.randint(
    0,
    1000,
    (1, 50)
)

document_embeddings = embedding(
    document
)

output = block(
    document_embeddings
)

print("\nDocument Output")

print(output.shape)

# ============================================================
# ENCODER VS DECODER
# ============================================================

# Encoder:
#
# Understand Input
#
# Examples:
#
# BERT
#
# Decoder:
#
# Generate Output
#
# Examples:
#
# GPT
# Llama
# Claude

# ============================================================
# COMMON TRANSFORMER COMPONENTS
# ============================================================

# Embedding
# Positional Encoding
# Multi Head Attention
# Feed Forward Network
# Transformer Block
# Encoder
# Decoder

# ============================================================
# TRANSFORMER FLOW
# ============================================================

# Text
#
# ↓
#
# Tokenization
#
# ↓
#
# Embedding
#
# ↓
#
# Positional Encoding
#
# ↓
#
# Multi Head Attention
#
# ↓
#
# Feed Forward Network
#
# ↓
#
# Transformer Block
#
# ↓
#
# Prediction

# ============================================================
# SUMMARY
# ============================================================

print("""
TRANSFORMERS SUMMARY

Main Components:

✔ Embeddings
✔ Positional Encoding
✔ Multi Head Attention
✔ Feed Forward Network
✔ Transformer Block

Popular Classes:

nn.Embedding()

nn.MultiheadAttention()

nn.TransformerEncoder()

Important Concepts:

✔ Tokens
✔ Embeddings
✔ Attention
✔ Encoder
✔ Decoder

Applications:

✔ ChatGPT
✔ Claude
✔ Gemini
✔ Llama
✔ Translation
✔ Text Generation

Benefits:

✔ Long Context Understanding
✔ Parallel Processing
✔ Scalable Training
✔ Foundation of Modern AI
""")
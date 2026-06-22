# ============================================================
# EMBEDDINGS IN AI AND MACHINE LEARNING
# ============================================================

# Embeddings convert text, images, or other data
# into numerical vectors.
#
# Computers cannot understand text directly.
#
# Embeddings transform text into numbers
# while preserving meaning.
#
# Examples:
#
# "Dog"  -> [0.23, 0.81, 0.45, ...]
# "Cat"  -> [0.21, 0.79, 0.42, ...]
#
# Similar meanings produce similar vectors.
#
# Uses:
#
# ✔ Semantic Search
# ✔ Recommendation Systems
# ✔ Chatbots
# ✔ RAG Applications
# ✔ Text Similarity
# ✔ Clustering

# Install:
#
# pip install openai numpy scikit-learn

# ============================================================
# WHAT IS AN EMBEDDING?
# ============================================================

text = "Machine Learning"

print("Text:", text)

print("""
Embedding converts text into
a vector of numbers.
""")

# ============================================================
# SIMPLE VECTOR EXAMPLE
# ============================================================

embedding = [
    0.21,
    0.45,
    0.88,
    0.12
]

print("\nSample Embedding")

print(embedding)

# ============================================================
# USING OPENAI EMBEDDINGS
# ============================================================

from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY"
)

response = client.embeddings.create(
    model="text-embedding-3-small",
    input="Machine Learning"
)

embedding = response.data[0].embedding

print("\nEmbedding Length")

print(len(embedding))

# ============================================================
# VIEW FIRST 10 VALUES
# ============================================================

print("\nFirst 10 Values")

print(embedding[:10])

# ============================================================
# GENERATING MULTIPLE EMBEDDINGS
# ============================================================

texts = [
    "Machine Learning",
    "Artificial Intelligence",
    "Deep Learning"
]

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=texts
)

print("\nNumber of Embeddings")

print(len(response.data))

# ============================================================
# COSINE SIMILARITY
# ============================================================

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

v1 = np.array([[1, 2, 3]])

v2 = np.array([[1, 2, 4]])

similarity = cosine_similarity(
    v1,
    v2
)

print("\nCosine Similarity")

print(similarity)

# ============================================================
# TEXT SIMILARITY EXAMPLE
# ============================================================

text1 = "Machine Learning"

text2 = "Artificial Intelligence"

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=[text1, text2]
)

emb1 = response.data[0].embedding

emb2 = response.data[1].embedding

similarity = cosine_similarity(
    [emb1],
    [emb2]
)

print("\nText Similarity")

print(similarity)

# ============================================================
# SEMANTIC SEARCH EXAMPLE
# ============================================================

documents = [
    "Python is a programming language",
    "Machine Learning uses data",
    "Football is a sport"
]

query = "Artificial Intelligence"

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=documents + [query]
)

vectors = [
    item.embedding
    for item in response.data
]

query_vector = vectors[-1]

document_vectors = vectors[:-1]

scores = cosine_similarity(
    [query_vector],
    document_vectors
)

best_match = np.argmax(scores)

print("\nBest Match")

print(documents[best_match])

# ============================================================
# SIMPLE DOCUMENT RETRIEVAL
# ============================================================

documents = [
    "Python Tutorial",
    "Machine Learning Guide",
    "Data Science Notes"
]

query = "Learn AI"

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=documents + [query]
)

vectors = [
    item.embedding
    for item in response.data
]

query_vector = vectors[-1]

document_vectors = vectors[:-1]

scores = cosine_similarity(
    [query_vector],
    document_vectors
)

best_index = np.argmax(scores)

print("\nRetrieved Document")

print(documents[best_index])

# ============================================================
# PRACTICAL EXAMPLE 1
# FAQ SEARCH
# ============================================================

faq = [
    "How to reset password?",
    "How to change email?",
    "How to update profile?"
]

question = "I forgot my password"

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=faq + [question]
)

vectors = [
    item.embedding
    for item in response.data
]

question_vector = vectors[-1]

faq_vectors = vectors[:-1]

scores = cosine_similarity(
    [question_vector],
    faq_vectors
)

answer_index = np.argmax(scores)

print("\nBest FAQ Match")

print(faq[answer_index])

# ============================================================
# PRACTICAL EXAMPLE 2
# RECOMMENDATION SYSTEM
# ============================================================

products = [
    "Gaming Laptop",
    "Wireless Mouse",
    "Mechanical Keyboard"
]

search = "Computer for gaming"

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=products + [search]
)

vectors = [
    item.embedding
    for item in response.data
]

search_vector = vectors[-1]

product_vectors = vectors[:-1]

scores = cosine_similarity(
    [search_vector],
    product_vectors
)

recommended = np.argmax(scores)

print("\nRecommended Product")

print(products[recommended])

# ============================================================
# PRACTICAL EXAMPLE 3
# RAG DOCUMENT SEARCH
# ============================================================

knowledge_base = [
    "Python supports OOP.",
    "Machine Learning uses training data.",
    "SQL manages databases."
]

query = "How do models learn?"

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=knowledge_base + [query]
)

vectors = [
    item.embedding
    for item in response.data
]

query_vector = vectors[-1]

kb_vectors = vectors[:-1]

scores = cosine_similarity(
    [query_vector],
    kb_vectors
)

best_document = np.argmax(scores)

print("\nRetrieved Knowledge")

print(knowledge_base[best_document])

# ============================================================
# VECTOR DATABASE CONCEPT
# ============================================================

print("""
Vector Database Stores:

Text
Embedding
Metadata

Examples:

Pinecone
Weaviate
Qdrant
ChromaDB
FAISS
""")

# ============================================================
# IMPORTANT TERMS
# ============================================================

# Embedding
# Vector
# Similarity Search
# Cosine Similarity
# Semantic Search
# Vector Database
# RAG

# ============================================================
# ADVANTAGES
# ============================================================

# ✔ Understands Meaning
# ✔ Fast Search
# ✔ Semantic Matching
# ✔ Better Recommendations
# ✔ Essential For RAG

# ============================================================
# LIMITATIONS
# ============================================================

# ✘ Storage Cost
# ✘ Requires Vector Database
# ✘ Similarity Is Approximate
# ✘ Large Datasets Need Optimization

# ============================================================
# SUMMARY
# ============================================================

print("""
EMBEDDINGS SUMMARY

What Are Embeddings?

Numerical vector representations
of text, images, or data.

Create Embedding

client.embeddings.create()

Popular Model

text-embedding-3-small

Uses

✔ Semantic Search
✔ Recommendations
✔ Chatbots
✔ RAG
✔ Clustering

Similarity Measure

cosine_similarity()

Important Concepts

Embedding
Vector
Similarity Search
Vector Database
RAG

Benefits

✔ Captures Meaning
✔ Fast Retrieval
✔ Better Search
✔ AI-Powered Applications
""")
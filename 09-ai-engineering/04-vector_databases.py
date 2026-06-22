# ============================================================
# VECTOR DATABASES IN AI
# ============================================================

# A Vector Database stores embeddings
# and allows fast similarity search.
#
# Why Vector Databases?
#
# Traditional Databases:
#
# Search Exact Values
#
# Example:
# "Machine Learning"
#
# Vector Databases:
#
# Search Meaning
#
# Example:
# "AI"
# "Artificial Intelligence"
# "Machine Learning"
#
# All can be found because their
# embeddings are similar.
#
# Uses:
#
# ✔ RAG Applications
# ✔ Semantic Search
# ✔ Chatbots
# ✔ Recommendation Systems
# ✔ Document Retrieval
# ✔ AI Assistants

# Install:
#
# pip install openai numpy scikit-learn

# ============================================================
# WHAT IS A VECTOR?
# ============================================================

vector = [
    0.12,
    0.45,
    0.67,
    0.89
]

print("Sample Vector")

print(vector)

# ============================================================
# SIMPLE EMBEDDING STORAGE
# ============================================================

documents = [
    "Python Tutorial",
    "Machine Learning Guide",
    "SQL Notes"
]

print("\nDocuments")

for doc in documents:
    print(doc)

# ============================================================
# GENERATING EMBEDDINGS
# ============================================================

from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY"
)

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=documents
)

vectors = [
    item.embedding
    for item in response.data
]

print("\nNumber Of Vectors")

print(len(vectors))

# ============================================================
# STORING EMBEDDINGS
# ============================================================

vector_store = {}

for doc, vector in zip(
    documents,
    vectors
):
    vector_store[doc] = vector

print("\nVectors Stored")

print(len(vector_store))

# ============================================================
# SIMILARITY SEARCH
# ============================================================

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

query = "Learn Artificial Intelligence"

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=query
)

query_vector = response.data[0].embedding

scores = []

for document, vector in vector_store.items():

    score = cosine_similarity(
        [query_vector],
        [vector]
    )[0][0]

    scores.append(
        (document, score)
    )

scores.sort(
    key=lambda x: x[1],
    reverse=True
)

print("\nTop Match")

print(scores[0])

# ============================================================
# TOP K SEARCH
# ============================================================

top_k = 2

print("\nTop Results")

for result in scores[:top_k]:

    print(result)

# ============================================================
# METADATA STORAGE
# ============================================================

database = [
    {
        "id": 1,
        "text": "Python Tutorial",
        "category": "Programming"
    },
    {
        "id": 2,
        "text": "Machine Learning Guide",
        "category": "AI"
    }
]

print("\nMetadata Example")

print(database)

# ============================================================
# FILTERING WITH METADATA
# ============================================================

filtered = [
    item
    for item in database
    if item["category"] == "AI"
]

print("\nFiltered Results")

print(filtered)

# ============================================================
# PRACTICAL EXAMPLE 1
# FAQ SEARCH SYSTEM
# ============================================================

faq = [
    "How to reset password?",
    "How to update profile?",
    "How to change email?"
]

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=faq
)

faq_vectors = [
    item.embedding
    for item in response.data
]

query = "I forgot my password"

query_vector = client.embeddings.create(
    model="text-embedding-3-small",
    input=query
).data[0].embedding

scores = []

for question, vector in zip(
    faq,
    faq_vectors
):

    score = cosine_similarity(
        [query_vector],
        [vector]
    )[0][0]

    scores.append(
        (question, score)
    )

scores.sort(
    key=lambda x: x[1],
    reverse=True
)

print("\nBest FAQ Match")

print(scores[0])

# ============================================================
# PRACTICAL EXAMPLE 2
# DOCUMENT SEARCH
# ============================================================

documents = [
    "Python supports OOP.",
    "Machine Learning uses data.",
    "SQL manages databases."
]

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=documents
)

doc_vectors = [
    item.embedding
    for item in response.data
]

query = "How do AI models learn?"

query_vector = client.embeddings.create(
    model="text-embedding-3-small",
    input=query
).data[0].embedding

scores = []

for document, vector in zip(
    documents,
    doc_vectors
):

    score = cosine_similarity(
        [query_vector],
        [vector]
    )[0][0]

    scores.append(
        (document, score)
    )

scores.sort(
    key=lambda x: x[1],
    reverse=True
)

print("\nMost Relevant Document")

print(scores[0])

# ============================================================
# PRACTICAL EXAMPLE 3
# PRODUCT RECOMMENDATION
# ============================================================

products = [
    "Gaming Laptop",
    "Wireless Mouse",
    "Mechanical Keyboard"
]

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=products
)

product_vectors = [
    item.embedding
    for item in response.data
]

query = "Computer for gaming"

query_vector = client.embeddings.create(
    model="text-embedding-3-small",
    input=query
).data[0].embedding

scores = []

for product, vector in zip(
    products,
    product_vectors
):

    score = cosine_similarity(
        [query_vector],
        [vector]
    )[0][0]

    scores.append(
        (product, score)
    )

scores.sort(
    key=lambda x: x[1],
    reverse=True
)

print("\nRecommended Product")

print(scores[0])

# ============================================================
# VECTOR DATABASE WORKFLOW
# ============================================================

print("""
1. Create Embeddings

2. Store Vectors

3. Store Metadata

4. User Query

5. Create Query Embedding

6. Similarity Search

7. Return Best Results
""")

# ============================================================
# POPULAR VECTOR DATABASES
# ============================================================

vector_databases = [
    "Pinecone",
    "ChromaDB",
    "FAISS",
    "Qdrant",
    "Weaviate",
    "Milvus"
]

print("\nPopular Vector Databases")

for db in vector_databases:
    print(db)

# ============================================================
# WHY VECTOR DATABASES?
# ============================================================

# ✔ Fast Similarity Search
# ✔ Scalable
# ✔ Metadata Filtering
# ✔ RAG Support
# ✔ Billions of Vectors

# ============================================================
# IMPORTANT TERMS
# ============================================================

# Embedding
# Vector
# Similarity Search
# Metadata
# ANN Search
# Semantic Search
# RAG

# ============================================================
# ADVANTAGES
# ============================================================

# ✔ Semantic Understanding
# ✔ Fast Retrieval
# ✔ Better Search
# ✔ Essential For AI Apps

# ============================================================
# LIMITATIONS
# ============================================================

# ✘ Extra Infrastructure
# ✘ Storage Cost
# ✘ Embedding Generation Cost
# ✘ Approximate Results

# ============================================================
# SUMMARY
# ============================================================

print("""
VECTOR DATABASE SUMMARY

What Is A Vector Database?

A database optimized for storing
and searching embeddings.

Workflow

Create Embeddings
Store Vectors
Similarity Search
Retrieve Results

Common Operations

Insert
Search
Update
Delete

Popular Databases

Pinecone
ChromaDB
FAISS
Qdrant
Weaviate
Milvus

Uses

✔ RAG
✔ Semantic Search
✔ Chatbots
✔ Recommendations

Benefits

✔ Fast
✔ Scalable
✔ AI Friendly
✔ Meaning-Based Search
""")
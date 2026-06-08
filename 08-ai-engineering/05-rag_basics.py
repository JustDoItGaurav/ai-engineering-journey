# ============================================================
# RAG (RETRIEVAL AUGMENTED GENERATION)
# ============================================================

# RAG = Retrieval + Generation
#
# Retrieval:
# Find relevant information
#
# Generation:
# Use that information to generate answers
#
# Why RAG?
#
# LLM Alone:
# ✘ Limited Knowledge Cutoff
# ✘ Can Hallucinate
# ✘ Doesn't Know Your Documents
#
# RAG:
# ✔ Uses External Knowledge
# ✔ More Accurate Answers
# ✔ Less Hallucination
# ✔ Can Use Company Data
#
# Uses:
#
# ✔ AI Chatbots
# ✔ Company Knowledge Base
# ✔ PDF Question Answering
# ✔ Customer Support
# ✔ Search Systems

# Install:
#
# pip install openai scikit-learn numpy

# ============================================================
# WHAT IS RAG?
# ============================================================

print("""
RAG Workflow

Documents
    ↓
Embeddings
    ↓
Vector Database
    ↓
Similarity Search
    ↓
Relevant Chunks
    ↓
LLM
    ↓
Final Answer
""")

# ============================================================
# STEP 1
# CREATE KNOWLEDGE BASE
# ============================================================

documents = [
    "Python is a programming language.",
    "Machine Learning learns from data.",
    "SQL is used for databases.",
    "Deep Learning uses neural networks."
]

print("Knowledge Base")

for doc in documents:
    print("-", doc)

# ============================================================
# STEP 2
# GENERATE EMBEDDINGS
# ============================================================

from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY"
)

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=documents
)

document_vectors = [
    item.embedding
    for item in response.data
]

print("\nEmbeddings Created")

print("Total:", len(document_vectors))

# ============================================================
# STEP 3
# USER QUERY
# ============================================================

query = "How do AI models learn?"

print("\nUser Query")

print(query)

# ============================================================
# STEP 4
# CREATE QUERY EMBEDDING
# ============================================================

query_response = client.embeddings.create(
    model="text-embedding-3-small",
    input=query
)

query_vector = (
    query_response
    .data[0]
    .embedding
)

# ============================================================
# STEP 5
# SIMILARITY SEARCH
# ============================================================

from sklearn.metrics.pairwise import cosine_similarity

scores = cosine_similarity(
    [query_vector],
    document_vectors
)

print("\nSimilarity Scores")

print(scores)

# ============================================================
# STEP 6
# RETRIEVE BEST DOCUMENT
# ============================================================

import numpy as np

best_index = np.argmax(scores)

retrieved_document = documents[
    best_index
]

print("\nRetrieved Document")

print(retrieved_document)

# ============================================================
# STEP 7
# BUILD CONTEXT
# ============================================================

context = retrieved_document

print("\nContext")

print(context)

# ============================================================
# STEP 8
# SEND TO LLM
# ============================================================

prompt = f"""
Answer the question using
the provided context.

Context:
{context}

Question:
{query}
"""

response = client.responses.create(
    model="gpt-5",
    input=prompt
)

print("\nFinal Answer")

print(response.output_text)

# ============================================================
# RETRIEVING TOP K RESULTS
# ============================================================

top_k = 2

indices = np.argsort(
    scores[0]
)[-top_k:]

print("\nTop K Documents")

for index in indices:

    print(documents[index])

# ============================================================
# MULTI-DOCUMENT CONTEXT
# ============================================================

context = "\n".join(
    [
        documents[i]
        for i in indices
    ]
)

print("\nCombined Context")

print(context)

# ============================================================
# IMPROVED RAG PROMPT
# ============================================================

prompt = f"""
You are an AI assistant.

Use ONLY the provided context.

Context:
{context}

Question:
{query}

If answer is not found,
say:
"I don't know."
"""

print(prompt)

# ============================================================
# PRACTICAL EXAMPLE 1
# FAQ BOT
# ============================================================

faq = [
    "Reset password from settings page.",
    "Update email from profile page.",
    "Change password under security."
]

question = (
    "I forgot my password"
)

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

best_match = np.argmax(scores)

print("\nFAQ Result")

print(faq[best_match])

# ============================================================
# PRACTICAL EXAMPLE 2
# PDF CHATBOT CONCEPT
# ============================================================

pdf_chunks = [
    "Chapter 1 explains Python.",
    "Chapter 2 explains SQL.",
    "Chapter 3 explains ML."
]

query = "Tell me about ML"

print("""
PDF Chunks Stored

User Question

Retrieve Relevant Chunk

Send To LLM

Generate Answer
""")

# ============================================================
# PRACTICAL EXAMPLE 3
# COMPANY KNOWLEDGE BOT
# ============================================================

company_docs = [
    "Employees get 20 leave days.",
    "Office timing is 9 AM to 6 PM.",
    "Work from home is allowed twice a week."
]

query = (
    "How many leave days do I get?"
)

print("""
Search Company Documents

Retrieve Relevant Policy

Generate Response
""")

# ============================================================
# IMPORTANT RAG COMPONENTS
# ============================================================

# Knowledge Base
# Embeddings
# Vector Database
# Similarity Search
# Retriever
# Context Builder
# LLM

# ============================================================
# POPULAR VECTOR DATABASES
# ============================================================

vector_dbs = [
    "Pinecone",
    "Qdrant",
    "ChromaDB",
    "FAISS",
    "Milvus"
]

print("\nPopular Vector Databases")

for db in vector_dbs:
    print(db)

# ============================================================
# ADVANTAGES
# ============================================================

# ✔ Uses External Data
# ✔ Reduces Hallucinations
# ✔ Real-Time Knowledge
# ✔ Better Accuracy
# ✔ Company-Specific Answers

# ============================================================
# LIMITATIONS
# ============================================================

# ✘ Retrieval Can Fail
# ✘ Requires Embeddings
# ✘ Requires Vector Database
# ✘ More Complex Than Simple LLM

# ============================================================
# SUMMARY
# ============================================================

print("""
RAG SUMMARY

RAG =
Retrieval Augmented Generation

Workflow

Documents
→ Embeddings
→ Vector Database
→ Similarity Search
→ Context
→ LLM
→ Answer

Core Components

Knowledge Base
Embeddings
Retriever
Vector Database
LLM

Popular Use Cases

✔ Chatbots
✔ PDF QA
✔ Customer Support
✔ Enterprise Search

Benefits

✔ Accurate
✔ Up-to-Date
✔ Less Hallucination
✔ Scalable
""")
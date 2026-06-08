# ============================================================
# LANGCHAIN BASICS
# ============================================================

# LangChain is a framework for building
# LLM-powered applications.
#
# It helps connect:
#
# ✔ LLMs
# ✔ Prompts
# ✔ Memory
# ✔ Tools
# ✔ Agents
# ✔ Vector Databases
# ✔ RAG Pipelines
#
# Common Uses:
#
# ✔ Chatbots
# ✔ AI Assistants
# ✔ RAG Applications
# ✔ Document QA
# ✔ Agents

# Install:
#
# pip install langchain
# pip install langchain-openai

# ============================================================
# IMPORTS
# ============================================================

from langchain_openai import ChatOpenAI

# ============================================================
# CREATE LLM
# ============================================================

llm = ChatOpenAI(
    model="gpt-5"
)

print("LLM Created")

# ============================================================
# BASIC INVOCATION
# ============================================================

response = llm.invoke(
    "What is Machine Learning?"
)

print(response.content)

# ============================================================
# USING SYSTEM INSTRUCTIONS
# ============================================================

response = llm.invoke(
    [
        (
            "system",
            "You are a Python teacher."
        ),
        (
            "human",
            "Explain loops."
        )
    ]
)

print(response.content)

# ============================================================
# PROMPT TEMPLATE
# ============================================================

from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["topic"],
    template="""
    Explain {topic}
    for beginners.
    """
)

formatted_prompt = prompt.format(
    topic="Machine Learning"
)

print(formatted_prompt)

# ============================================================
# USING PROMPT WITH LLM
# ============================================================

response = llm.invoke(
    formatted_prompt
)

print(response.content)

# ============================================================
# CHAIN BASICS
# ============================================================

# Chain:
#
# Prompt -> LLM -> Output

topic = "Data Science"

prompt_text = (
    f"Explain {topic}"
)

response = llm.invoke(
    prompt_text
)

print(response.content)

# ============================================================
# USING PIPE OPERATOR
# ============================================================

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic}"
)

chain = prompt | llm

response = chain.invoke(
    {
        "topic": "Neural Networks"
    }
)

print(response.content)

# ============================================================
# OUTPUT PARSER
# ============================================================

from langchain_core.output_parsers import (
    StrOutputParser
)

parser = StrOutputParser()

chain = (
    prompt
    | llm
    | parser
)

result = chain.invoke(
    {
        "topic": "Deep Learning"
    }
)

print(result)

# ============================================================
# CHAT PROMPT TEMPLATE
# ============================================================

from langchain.prompts import (
    ChatPromptTemplate
)

chat_prompt = (
    ChatPromptTemplate
    .from_messages(
        [
            (
                "system",
                "You are a tutor."
            ),
            (
                "human",
                "{question}"
            )
        ]
    )
)

chain = (
    chat_prompt
    | llm
    | parser
)

response = chain.invoke(
    {
        "question":
        "What is AI?"
    }
)

print(response)

# ============================================================
# MEMORY CONCEPT
# ============================================================

print("""
Memory Stores:

Previous Messages
Conversation Context
User Information

Useful For:

Chatbots
AI Assistants
""")

# ============================================================
# DOCUMENT LOADING CONCEPT
# ============================================================

documents = [
    "Python is a programming language.",
    "Machine Learning uses data."
]

print("\nDocuments Loaded")

for doc in documents:
    print(doc)

# ============================================================
# TEXT SPLITTING CONCEPT
# ============================================================

print("""
Large Documents
       ↓
Split Into Chunks
       ↓
Embeddings
       ↓
Vector Database
""")

# ============================================================
# EMBEDDINGS
# ============================================================

from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

print("\nEmbedding Model Created")

# ============================================================
# VECTOR STORE CONCEPT
# ============================================================

print("""
Vector Store

Stores Embeddings

Examples:

FAISS
ChromaDB
Pinecone
Qdrant
""")

# ============================================================
# SIMPLE RAG WORKFLOW
# ============================================================

print("""
User Question
      ↓
Retriever
      ↓
Relevant Chunks
      ↓
LLM
      ↓
Answer
""")

# ============================================================
# RETRIEVER CONCEPT
# ============================================================

print("""
Retriever Searches

Most Relevant Documents

Using Similarity Search
""")

# ============================================================
# PRACTICAL EXAMPLE 1
# STUDY ASSISTANT
# ============================================================

prompt = PromptTemplate(
    input_variables=["topic"],
    template="""
    Explain {topic}
    with examples.
    """
)

chain = (
    prompt
    | llm
    | parser
)

result = chain.invoke(
    {
        "topic":
        "Linear Regression"
    }
)

print(result)

# ============================================================
# PRACTICAL EXAMPLE 2
# EMAIL GENERATOR
# ============================================================

prompt = PromptTemplate(
    input_variables=["purpose"],
    template="""
    Write an email for:

    {purpose}
    """
)

chain = (
    prompt
    | llm
    | parser
)

result = chain.invoke(
    {
        "purpose":
        "Leave Application"
    }
)

print(result)

# ============================================================
# PRACTICAL EXAMPLE 3
# BLOG GENERATOR
# ============================================================

prompt = PromptTemplate(
    input_variables=["topic"],
    template="""
    Write a blog about:

    {topic}
    """
)

chain = (
    prompt
    | llm
    | parser
)

result = chain.invoke(
    {
        "topic":
        "Artificial Intelligence"
    }
)

print(result)

# ============================================================
# IMPORTANT LANGCHAIN COMPONENTS
# ============================================================

# LLM
# Prompt
# Chain
# Output Parser
# Memory
# Retriever
# Embeddings
# Vector Store
# Agent

# ============================================================
# ADVANTAGES
# ============================================================

# ✔ Easy LLM Integration
# ✔ Reusable Components
# ✔ RAG Support
# ✔ Agent Support
# ✔ Production Ready

# ============================================================
# LIMITATIONS
# ============================================================

# ✘ Learning Curve
# ✘ Frequent Updates
# ✘ Extra Abstraction Layer

# ============================================================
# SUMMARY
# ============================================================

print("""
LANGCHAIN SUMMARY

What Is LangChain?

Framework for building
LLM-powered applications.

Core Components

LLM
Prompt
Chain
Memory
Retriever
Embeddings
Agent

Basic Flow

Prompt
   ↓
LLM
   ↓
Output

Popular Uses

✔ Chatbots
✔ RAG
✔ AI Assistants
✔ Document QA
✔ Agents

Benefits

✔ Modular
✔ Scalable
✔ Flexible
✔ AI Application Development
""")
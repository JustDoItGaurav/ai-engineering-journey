# ============================================================
# OPENAI API IN PYTHON
# ============================================================

# OpenAI API allows you to use AI models for:
#
# ✔ Chatbots
# ✔ Content Generation
# ✔ Code Generation
# ✔ Data Analysis
# ✔ AI Assistants
# ✔ Summarization
# ✔ Translation
#
# Install:
#
# pip install openai

# ============================================================
# IMPORT OPENAI
# ============================================================

from openai import OpenAI

# ============================================================
# CREATE CLIENT
# ============================================================

client = OpenAI(
    api_key="YOUR_API_KEY"
)

# ============================================================
# BASIC CHAT COMPLETION
# ============================================================

response = client.responses.create(
    model="gpt-5",
    input="What is Machine Learning?"
)

print(response.output_text)

# ============================================================
# STORING API KEY USING ENVIRONMENT VARIABLE
# ============================================================

# Windows:
#
# set OPENAI_API_KEY=your_key
#
# Linux/Mac:
#
# export OPENAI_API_KEY=your_key

import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# ============================================================
# ASKING MULTIPLE QUESTIONS
# ============================================================

questions = [
    "What is AI?",
    "What is Deep Learning?",
    "What is NLP?"
]

for question in questions:

    response = client.responses.create(
        model="gpt-5",
        input=question
    )

    print("\nQuestion:", question)
    print(response.output_text)

# ============================================================
# SYSTEM INSTRUCTIONS
# ============================================================

response = client.responses.create(
    model="gpt-5",
    instructions="You are a Python tutor.",
    input="Explain loops."
)

print(response.output_text)

# ============================================================
# CHATBOT EXAMPLE
# ============================================================

conversation = []

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    conversation.append({
        "role": "user",
        "content": user_input
    })

    response = client.responses.create(
        model="gpt-5",
        input=conversation
    )

    reply = response.output_text

    print("Bot:", reply)

    conversation.append({
        "role": "assistant",
        "content": reply
    })

# ============================================================
# SUMMARIZATION EXAMPLE
# ============================================================

text = """
Machine Learning is a branch of AI
that enables computers to learn
from data without explicit programming.
"""

response = client.responses.create(
    model="gpt-5",
    input=f"Summarize:\n{text}"
)

print(response.output_text)

# ============================================================
# TRANSLATION EXAMPLE
# ============================================================

response = client.responses.create(
    model="gpt-5",
    input="Translate 'Good Morning' into Hindi."
)

print(response.output_text)

# ============================================================
# CODE GENERATION
# ============================================================

response = client.responses.create(
    model="gpt-5",
    input="Write a Python function for factorial."
)

print(response.output_text)

# ============================================================
# JSON OUTPUT EXAMPLE
# ============================================================

response = client.responses.create(
    model="gpt-5",
    input="""
    Return a student record as JSON:
    Name: Rahul
    Age: 21
    Course: Data Science
    """
)

print(response.output_text)

# ============================================================
# PRACTICAL EXAMPLE 1
# AI STUDY ASSISTANT
# ============================================================

question = "Explain Linear Regression."

response = client.responses.create(
    model="gpt-5",
    instructions="You are a Data Science teacher.",
    input=question
)

print(response.output_text)

# ============================================================
# PRACTICAL EXAMPLE 2
# EMAIL WRITER
# ============================================================

prompt = """
Write a professional leave application email.
"""

response = client.responses.create(
    model="gpt-5",
    input=prompt
)

print(response.output_text)

# ============================================================
# PRACTICAL EXAMPLE 3
# BLOG GENERATOR
# ============================================================

topic = "Benefits of Artificial Intelligence"

response = client.responses.create(
    model="gpt-5",
    input=f"Write a blog about {topic}"
)

print(response.output_text)

# ============================================================
# ERROR HANDLING
# ============================================================

try:

    response = client.responses.create(
        model="gpt-5",
        input="Hello"
    )

    print(response.output_text)

except Exception as e:

    print("Error:", e)

# ============================================================
# IMPORTANT PARAMETERS
# ============================================================

# model
# input
# instructions

# ============================================================
# BEST PRACTICES
# ============================================================

# ✔ Store API Keys Securely
# ✔ Use Environment Variables
# ✔ Handle Errors
# ✔ Keep Prompts Clear
# ✔ Reuse Client Object

# ============================================================
# SUMMARY
# ============================================================

print("""
OPENAI API SUMMARY

Install:

pip install openai

Import:

from openai import OpenAI

Create Client:

client = OpenAI()

Generate Response:

client.responses.create()

Common Uses

✔ Chatbots
✔ AI Assistants
✔ Summarization
✔ Translation
✔ Code Generation
✔ Content Writing

Important Parameters

model
input
instructions

Best Practices

✔ Secure API Keys
✔ Error Handling
✔ Clear Prompts
✔ Reusable Client

Benefits

✔ Easy Integration
✔ Powerful AI Models
✔ Flexible Applications
✔ Production Ready
""")
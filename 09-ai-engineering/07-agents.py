# ============================================================
# AGENTS IN AI AND LANGCHAIN
# ============================================================

# Agents are AI systems that can:
#
# ✔ Think
# ✔ Decide
# ✔ Choose Tools
# ✔ Take Actions
# ✔ Solve Multi-Step Tasks
#
# Normal LLM:
#
# Question -> Answer
#
# Agent:
#
# Question
#    ↓
# Reason
#    ↓
# Select Tool
#    ↓
# Execute Tool
#    ↓
# Generate Answer
#
# Uses:
#
# ✔ AI Assistants
# ✔ Research Agents
# ✔ Customer Support
# ✔ Data Analysis
# ✔ Automation

# Install:
#
# pip install langchain
# pip install langchain-openai

# ============================================================
# WHAT IS AN AGENT?
# ============================================================

print("""
Agent Workflow

User Question
      ↓
Reasoning
      ↓
Choose Tool
      ↓
Use Tool
      ↓
Get Result
      ↓
Final Answer
""")

# ============================================================
# IMPORTS
# ============================================================

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-5"
)

# ============================================================
# SIMPLE TOOL
# ============================================================

def calculator(text):

    return eval(text)

print(
    calculator("10 + 5")
)

# ============================================================
# TOOL CONCEPT
# ============================================================

print("""
A Tool Is A Function

Examples:

Calculator
Search Engine
Database Query
Weather API
Email Sender
""")

# ============================================================
# DEFINING A TOOL
# ============================================================

from langchain.tools import tool

@tool
def multiply(a: int, b: int):
    """
    Multiply two numbers
    """

    return a * b

print(
    multiply.invoke(
        {
            "a": 10,
            "b": 20
        }
    )
)

# ============================================================
# MULTIPLE TOOLS
# ============================================================

@tool
def add(a: int, b: int):
    """
    Add numbers
    """

    return a + b


@tool
def subtract(a: int, b: int):
    """
    Subtract numbers
    """

    return a - b

print(
    add.invoke(
        {
            "a": 5,
            "b": 3
        }
    )
)

# ============================================================
# BIND TOOLS TO LLM
# ============================================================

tools = [
    add,
    subtract,
    multiply
]

llm_with_tools = llm.bind_tools(
    tools
)

print("""
Tools Connected To LLM
""")

# ============================================================
# TOOL CALLING
# ============================================================

response = llm_with_tools.invoke(
    "What is 15 multiplied by 8?"
)

print(response)

# ============================================================
# AGENT DECISION MAKING
# ============================================================

print("""
User:
What is 15 * 8?

Agent:
Needs Calculator

Tool:
Multiply

Result:
120

Final Answer:
120
""")

# ============================================================
# AGENT LOOP CONCEPT
# ============================================================

print("""
Think
  ↓
Act
  ↓
Observe
  ↓
Think Again
  ↓
Answer
""")

# ============================================================
# PRACTICAL EXAMPLE 1
# MATH AGENT
# ============================================================

question = """
What is
(10 * 5) + 20 ?
"""

response = llm_with_tools.invoke(
    question
)

print(response)

# ============================================================
# PRACTICAL EXAMPLE 2
# CUSTOMER SUPPORT AGENT
# ============================================================

@tool
def get_policy():
    """
    Return company leave policy
    """

    return (
        "Employees receive "
        "20 leave days annually."
    )

print(
    get_policy.invoke({})
)

# ============================================================
# PRACTICAL EXAMPLE 3
# PRODUCT AGENT
# ============================================================

@tool
def get_product_price():
    """
    Return laptop price
    """

    return "$1200"

print(
    get_product_price.invoke({})
)

# ============================================================
# MEMORY CONCEPT
# ============================================================

print("""
Agent Memory

Stores:

Conversation
Previous Actions
User Context
""")

# ============================================================
# SEARCH TOOL CONCEPT
# ============================================================

print("""
Agent + Search

Question
   ↓
Search Tool
   ↓
Results
   ↓
Final Answer
""")

# ============================================================
# DATABASE TOOL CONCEPT
# ============================================================

print("""
Agent + Database

Question
   ↓
Database Query
   ↓
Results
   ↓
Answer
""")

# ============================================================
# RAG AGENT CONCEPT
# ============================================================

print("""
Question
    ↓
Retriever
    ↓
Relevant Documents
    ↓
LLM
    ↓
Answer
""")

# ============================================================
# TYPES OF AGENTS
# ============================================================

agents = [
    "Tool Calling Agent",
    "ReAct Agent",
    "RAG Agent",
    "Research Agent",
    "Multi-Agent System"
]

print("\nAgent Types")

for item in agents:

    print(item)

# ============================================================
# ADVANTAGES
# ============================================================

# ✔ Can Use Tools
# ✔ Can Automate Tasks
# ✔ Can Perform Multi-Step Reasoning
# ✔ More Powerful Than Basic Chat

# ============================================================
# LIMITATIONS
# ============================================================

# ✘ More Complex
# ✘ Higher Cost
# ✘ More Latency
# ✘ Tool Errors Affect Results

# ============================================================
# IMPORTANT TERMS
# ============================================================

# Agent
# Tool
# Tool Calling
# Action
# Observation
# Memory
# Reasoning

# ============================================================
# SUMMARY
# ============================================================

print("""
AGENTS SUMMARY

What Is An Agent?

An AI system that can
reason, choose tools,
and perform actions.

Workflow

Question
→ Reason
→ Tool
→ Action
→ Answer

Core Components

LLM
Tools
Memory
Reasoning

Popular Tools

Calculator
Search
Database
API
Retriever

Agent Types

Tool Calling Agent
ReAct Agent
RAG Agent
Research Agent

Uses

✔ AI Assistants
✔ Automation
✔ Research
✔ Customer Support

Benefits

✔ Smart Decisions
✔ Tool Usage
✔ Multi-Step Tasks
✔ Powerful AI Systems
""")
# ============================================================
# PROMPT ENGINEERING IN GENERATIVE AI
# ============================================================

# Prompt Engineering is the process of
# designing effective prompts to get
# better results from AI models.
#
# A Prompt = Instruction given to AI
#
# Examples:
#
# ✔ Ask Questions
# ✔ Generate Content
# ✔ Write Code
# ✔ Summarize Text
# ✔ Translate Languages
#
# Better Prompt → Better Output

# ============================================================
# WHAT IS A PROMPT?
# ============================================================

prompt = "Explain Machine Learning."

print(prompt)

# ============================================================
# BASIC PROMPT
# ============================================================

# Simple instruction

prompt = "What is Artificial Intelligence?"

print(prompt)

# ============================================================
# CLEAR AND SPECIFIC PROMPT
# ============================================================

# Bad Prompt

bad_prompt = "Tell me about Python."

# Good Prompt

good_prompt = """
Explain Python programming language
for beginners in 5 points with examples.
"""

print(good_prompt)

# ============================================================
# ROLE-BASED PROMPTING
# ============================================================

# Assign a role to AI

prompt = """
You are a Data Science teacher.

Explain Linear Regression
in simple language.
"""

print(prompt)

# ============================================================
# TASK-BASED PROMPTING
# ============================================================

prompt = """
Write a professional email
requesting leave for 2 days.
"""

print(prompt)

# ============================================================
# FORMAT-BASED PROMPTING
# ============================================================

prompt = """
Explain Machine Learning.

Output Format:

1. Definition
2. Types
3. Applications
4. Benefits
"""

print(prompt)

# ============================================================
# STEP-BY-STEP PROMPTING
# ============================================================

prompt = """
Explain how to build a machine
learning model step by step.
"""

print(prompt)

# ============================================================
# FEW-SHOT PROMPTING
# ============================================================

# Giving examples before asking

prompt = """
Example:

Input: Apple
Output: Fruit

Input: Carrot
Output: Vegetable

Input: Mango
Output:
"""

print(prompt)

# ============================================================
# ZERO-SHOT PROMPTING
# ============================================================

# No examples provided

prompt = """
Classify:

Mango
"""

print(prompt)

# ============================================================
# CHAIN OF THOUGHT STYLE PROMPT
# ============================================================

prompt = """
Solve the problem step by step.

A shop sold 10 pens at ₹20 each.

What is the total revenue?
"""

print(prompt)

# ============================================================
# SUMMARIZATION PROMPT
# ============================================================

text = """
Machine Learning is a branch of AI
that allows systems to learn from data.
"""

prompt = f"""
Summarize the following text:

{text}
"""

print(prompt)

# ============================================================
# TRANSLATION PROMPT
# ============================================================

prompt = """
Translate the following into Hindi:

Good Morning
"""

print(prompt)

# ============================================================
# CODE GENERATION PROMPT
# ============================================================

prompt = """
Write a Python function
to calculate factorial.
"""

print(prompt)

# ============================================================
# CODE EXPLANATION PROMPT
# ============================================================

prompt = """
Explain the following Python code
line by line.
"""

print(prompt)

# ============================================================
# JSON OUTPUT PROMPT
# ============================================================

prompt = """
Return the following information
as JSON.

Name: Rahul
Age: 21
Course: Data Science
"""

print(prompt)

# ============================================================
# TABLE OUTPUT PROMPT
# ============================================================

prompt = """
Compare Python and Java.

Return output in table format.
"""

print(prompt)

# ============================================================
# PRACTICAL EXAMPLE 1
# STUDY ASSISTANT
# ============================================================

prompt = """
You are a Machine Learning tutor.

Explain Decision Trees with:
- Definition
- Example
- Advantages
- Disadvantages
"""

print(prompt)

# ============================================================
# PRACTICAL EXAMPLE 2
# CONTENT WRITING
# ============================================================

prompt = """
Write a 500-word blog on
Artificial Intelligence.

Tone:
Professional

Audience:
Beginners
"""

print(prompt)

# ============================================================
# PRACTICAL EXAMPLE 3
# RESUME IMPROVEMENT
# ============================================================

prompt = """
Improve the following resume summary
to make it more professional.
"""

print(prompt)

# ============================================================
# PROMPT TEMPLATE
# ============================================================

topic = "Machine Learning"

prompt = f"""
Role:
You are an expert teacher.

Task:
Explain {topic}

Requirements:
- Simple language
- Real-world examples
- 5 key points

Output Format:
Bullet Points
"""

print(prompt)

# ============================================================
# EFFECTIVE PROMPTING TIPS
# ============================================================

# ✔ Be Specific
# ✔ Give Context
# ✔ Define Output Format
# ✔ Assign a Role
# ✔ Provide Examples
# ✔ Mention Audience
# ✔ Mention Tone

# ============================================================
# COMMON MISTAKES
# ============================================================

# ✘ Vague Instructions
# ✘ Missing Context
# ✘ Too Much Ambiguity
# ✘ No Output Format
# ✘ Overly Complex Requests

# ============================================================
# ADVANCED TECHNIQUES
# ============================================================

# Zero-Shot Prompting
# One-Shot Prompting
# Few-Shot Prompting
# Role Prompting
# Chain of Thought
# Structured Prompting

# ============================================================
# SUMMARY
# ============================================================

print("""
PROMPT ENGINEERING SUMMARY

What is Prompt Engineering?

Designing effective prompts
to get better AI outputs.

Prompt Types

✔ Zero-Shot
✔ One-Shot
✔ Few-Shot
✔ Role-Based
✔ Task-Based
✔ Chain of Thought

Best Practices

✔ Be Clear
✔ Be Specific
✔ Give Context
✔ Define Format
✔ Provide Examples

Prompt Structure

Role
Task
Context
Requirements
Output Format

Uses

✔ Content Writing
✔ Coding
✔ AI Assistants
✔ Learning
✔ Business Automation

Benefits

✔ Better Responses
✔ Higher Accuracy
✔ Consistent Output
✔ Faster Workflow
""")
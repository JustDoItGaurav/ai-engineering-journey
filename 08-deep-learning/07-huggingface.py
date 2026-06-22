# ============================================================
# HUGGING FACE IN DEEP LEARNING & AI
# ============================================================

# Hugging Face is the most popular platform
# for working with AI and Large Language Models.
#
# Used For:
#
# 1. Text Generation
# 2. Sentiment Analysis
# 3. Translation
# 4. Question Answering
# 5. Embeddings
# 6. Image Classification
# 7. Speech Recognition
#
# Why Hugging Face?
#
# ✔ Thousands of Pretrained Models
# ✔ Easy To Use
# ✔ Industry Standard
# ✔ Open Source
# ✔ Supports Transformers
#
# Install:
#
# pip install transformers
# pip install torch

# ============================================================
# IMPORTING LIBRARIES
# ============================================================

from transformers import pipeline

# ============================================================
# WHAT IS A PIPELINE?
# ============================================================

# Pipeline provides a simple interface
# to use pretrained models.
#
# Example:
#
# Text
# ↓
# Model
# ↓
# Output

# ============================================================
# SENTIMENT ANALYSIS
# ============================================================

sentiment = pipeline(
    "sentiment-analysis"
)

result = sentiment(
    "I love learning AI and Deep Learning"
)

print("Sentiment Analysis")

print(result)

# ============================================================
# TEXT GENERATION
# ============================================================

generator = pipeline(
    "text-generation",
    model="gpt2"
)

result = generator(
    "Artificial Intelligence is",
    max_length=30
)

print("\nText Generation")

print(result)

# ============================================================
# QUESTION ANSWERING
# ============================================================

qa = pipeline(
    "question-answering"
)

result = qa(
    question="What is AI?",
    context="""
    Artificial Intelligence is the simulation
    of human intelligence by machines.
    """
)

print("\nQuestion Answering")

print(result)

# ============================================================
# TRANSLATION
# ============================================================

translator = pipeline(
    "translation_en_to_fr"
)

result = translator(
    "I love machine learning"
)

print("\nTranslation")

print(result)

# ============================================================
# SUMMARIZATION
# ============================================================

summarizer = pipeline(
    "summarization"
)

text = """
Artificial Intelligence is transforming
industries across the world. Companies use
AI for automation, analytics, customer support,
healthcare, and research.
"""

summary = summarizer(
    text,
    max_length=30,
    min_length=10
)

print("\nSummary")

print(summary)

# ============================================================
# TOKENIZER
# ============================================================

# Tokenizers convert text
# into tokens.

from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    "bert-base-uncased"
)

tokens = tokenizer(
    "I love AI"
)

print("\nTokenization")

print(tokens)

# ============================================================
# TOKEN IDS
# ============================================================

print("\nInput IDs")

print(tokens["input_ids"])

# ============================================================
# DECODING TOKENS
# ============================================================

decoded = tokenizer.decode(
    tokens["input_ids"]
)

print("\nDecoded Text")

print(decoded)

# ============================================================
# LOADING A MODEL
# ============================================================

from transformers import AutoModel

model = AutoModel.from_pretrained(
    "bert-base-uncased"
)

print("\nModel Loaded")

print(type(model))

# ============================================================
# EMBEDDINGS
# ============================================================

inputs = tokenizer(
    "Artificial Intelligence",
    return_tensors="pt"
)

outputs = model(**inputs)

print("\nEmbedding Shape")

print(outputs.last_hidden_state.shape)

# ============================================================
# USING DISTILBERT
# ============================================================

# Smaller and faster version of BERT.

small_model = AutoModel.from_pretrained(
    "distilbert-base-uncased"
)

print("\nDistilBERT Loaded")

print(type(small_model))

# ============================================================
# FEATURE EXTRACTION
# ============================================================

feature_extractor = pipeline(
    "feature-extraction"
)

features = feature_extractor(
    "Deep Learning is amazing"
)

print("\nFeature Extraction")

print(type(features))

# ============================================================
# TEXT CLASSIFICATION
# ============================================================

classifier = pipeline(
    "text-classification"
)

result = classifier(
    "This course is excellent"
)

print("\nText Classification")

print(result)

# ============================================================
# PRACTICAL EXAMPLE 1
# CUSTOMER REVIEW ANALYSIS
# ============================================================

review = """
The product quality is amazing and delivery
was very fast.
"""

result = sentiment(review)

print("\nCustomer Review Analysis")

print(result)

# ============================================================
# PRACTICAL EXAMPLE 2
# ARTICLE SUMMARIZER
# ============================================================

article = """
Machine Learning and Artificial Intelligence
are transforming businesses worldwide.
Organizations use AI to improve efficiency,
reduce costs, and enhance customer experiences.
"""

summary = summarizer(
    article,
    max_length=25,
    min_length=10
)

print("\nArticle Summary")

print(summary)

# ============================================================
# PRACTICAL EXAMPLE 3
# CHATBOT RESPONSE GENERATION
# ============================================================

response = generator(
    "Hello, how are you today?",
    max_length=50
)

print("\nChatbot Response")

print(response)

# ============================================================
# SAVING TOKENIZER
# ============================================================

# tokenizer.save_pretrained(
#     "my_tokenizer"
# )

# ============================================================
# SAVING MODEL
# ============================================================

# model.save_pretrained(
#     "my_model"
# )

# ============================================================
# LOADING SAVED MODEL
# ============================================================

# model = AutoModel.from_pretrained(
#     "my_model"
# )

# ============================================================
# POPULAR HUGGING FACE CLASSES
# ============================================================

# pipeline()
# AutoTokenizer
# AutoModel
# AutoModelForCausalLM
# AutoModelForSequenceClassification

# ============================================================
# POPULAR TASKS
# ============================================================

# Sentiment Analysis
# Text Generation
# Translation
# Summarization
# Question Answering
# Embeddings

# ============================================================
# POPULAR MODELS
# ============================================================

# BERT
# DistilBERT
# GPT-2
# Llama
# Gemma
# Phi
# Mistral

# ============================================================
# HUGGING FACE FLOW
# ============================================================

# Text
#
# ↓
#
# Tokenizer
#
# ↓
#
# Model
#
# ↓
#
# Prediction
#
# ↓
#
# Output

# ============================================================
# SUMMARY
# ============================================================

print("""
HUGGING FACE SUMMARY

Install:

pip install transformers

Main Components:

pipeline()

AutoTokenizer

AutoModel

Popular Tasks:

✔ Text Generation
✔ Sentiment Analysis
✔ Translation
✔ Summarization
✔ Question Answering
✔ Embeddings

Popular Models:

✔ BERT
✔ GPT-2
✔ Llama
✔ Gemma
✔ Phi
✔ Mistral

Applications:

✔ Chatbots
✔ RAG Systems
✔ AI Assistants
✔ Search Systems
✔ NLP Applications

Benefits:

✔ Pretrained Models
✔ Easy To Use
✔ Industry Standard
✔ Production Ready
✔ Huge Community
""")
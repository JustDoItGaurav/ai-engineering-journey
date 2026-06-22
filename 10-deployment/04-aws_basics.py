# ============================================================
# AWS BASICS FOR AI ENGINEERS
# ============================================================

# AWS = Amazon Web Services
#
# AWS is the most popular cloud platform.
#
# Companies use AWS to:
#
# ✔ Deploy Applications
# ✔ Store Data
# ✔ Host APIs
# ✔ Run AI Systems
# ✔ Scale Infrastructure
#
# Why Learn AWS?
#
# ✔ Industry Standard
# ✔ Cloud Deployment
# ✔ AI Hosting
# ✔ High Availability
# ✔ Global Infrastructure
#
# Website:
#
# https://aws.amazon.com

# ============================================================
# AWS SERVICES WE WILL LEARN
# ============================================================

# EC2
# S3
# Lambda

# ============================================================
# WHAT IS EC2?
# ============================================================

# EC2 =
#
# Elastic Compute Cloud
#
# Virtual Machine In AWS
#
# Used To:
#
# Run Applications
# Host Websites
# Deploy APIs
# Host AI Projects

# ============================================================
# EC2 EXAMPLE
# ============================================================

# Local Machine
#
# app.py
#
# ↓
#
# Upload To EC2
#
# ↓
#
# Run FastAPI App
#
# ↓
#
# Public URL

# ============================================================
# CREATE EC2 INSTANCE
# ============================================================

# AWS Console
#
# ↓
#
# EC2
#
# ↓
#
# Launch Instance
#
# ↓
#
# Select Ubuntu
#
# ↓
#
# Create Key Pair
#
# ↓
#
# Launch

# ============================================================
# CONNECT TO EC2
# ============================================================

# Example:

# ssh -i key.pem ubuntu@IP_ADDRESS

# ============================================================
# UPDATE EC2
# ============================================================

# sudo apt update

# ============================================================
# INSTALL PYTHON
# ============================================================

# python3 --version

# ============================================================
# INSTALL GIT
# ============================================================

# sudo apt install git

# ============================================================
# CLONE PROJECT
# ============================================================

# git clone repository_url

# ============================================================
# RUN FASTAPI APP
# ============================================================

# uvicorn app:app
# --host 0.0.0.0
# --port 8000

# ============================================================
# SECURITY GROUPS
# ============================================================

# Security Groups act like a firewall.
#
# Example:
#
# Allow:
#
# SSH   → Port 22
# HTTP  → Port 80
# HTTPS → Port 443
# FastAPI → Port 8000

# ============================================================
# WHAT IS S3?
# ============================================================

# S3 =
#
# Simple Storage Service
#
# Used To Store:
#
# Images
# Videos
# PDFs
# Models
# Datasets

# ============================================================
# S3 EXAMPLE
# ============================================================

# Upload:
#
# model.pkl
#
# Store:
#
# S3 Bucket
#
# Access Anywhere

# ============================================================
# WHAT IS A BUCKET?
# ============================================================

# Bucket =
#
# Folder In AWS

# Example:
#
# ai-models
# datasets
# chatbot-files

# ============================================================
# CREATE S3 BUCKET
# ============================================================

# AWS Console
#
# ↓
#
# S3
#
# ↓
#
# Create Bucket

# ============================================================
# INSTALL BOTO3
# ============================================================

# pip install boto3

# ============================================================
# IMPORT BOTO3
# ============================================================

import boto3

# ============================================================
# CONNECT TO S3
# ============================================================

# s3 = boto3.client("s3")

# ============================================================
# UPLOAD FILE
# ============================================================

# s3.upload_file(
#     "data.csv",
#     "my-bucket",
#     "data.csv"
# )

# ============================================================
# DOWNLOAD FILE
# ============================================================

# s3.download_file(
#     "my-bucket",
#     "data.csv",
#     "downloaded.csv"
# )

# ============================================================
# LIST FILES
# ============================================================

# response = s3.list_objects_v2(
#     Bucket="my-bucket"
# )

# ============================================================
# WHAT IS AWS LAMBDA?
# ============================================================

# Lambda =
#
# Serverless Computing
#
# Run Code Without Managing Servers

# ============================================================
# LAMBDA EXAMPLE
# ============================================================

# User Uploads File
#
# ↓
#
# Lambda Executes
#
# ↓
#
# Process File
#
# ↓
#
# Save To S3

# ============================================================
# SIMPLE LAMBDA FUNCTION
# ============================================================

def lambda_handler(event, context):

    return {
        "statusCode": 200,
        "message": "Hello Lambda"
    }

# ============================================================
# WHEN TO USE LAMBDA?
# ============================================================

# Small Tasks
# Automation
# File Processing
# API Triggers
# Notifications

# ============================================================
# AI PROJECT DEPLOYMENT
# ============================================================

# User
#
# ↓
#
# FastAPI
#
# ↓
#
# EC2
#
# ↓
#
# AI Model
#
# ↓
#
# Response

# ============================================================
# RAG SYSTEM DEPLOYMENT
# ============================================================

# Documents
#
# ↓
#
# S3 Bucket
#
# ↓
#
# Vector Database
#
# ↓
#
# FastAPI
#
# ↓
#
# EC2

# ============================================================
# CHATBOT DEPLOYMENT
# ============================================================

# Frontend
#
# ↓
#
# FastAPI
#
# ↓
#
# EC2
#
# ↓
#
# OpenAI API

# ============================================================
# PRACTICAL EXAMPLE 1
# HOST FASTAPI APP
# ============================================================

# Create EC2
#
# Install Python
#
# Clone Project
#
# Run:
#
# uvicorn app:app
# --host 0.0.0.0

# ============================================================
# PRACTICAL EXAMPLE 2
# STORE DATASET
# ============================================================

# Upload:
#
# dataset.csv
#
# To:
#
# S3 Bucket

# ============================================================
# PRACTICAL EXAMPLE 3
# STORE AI MODEL
# ============================================================

# Upload:
#
# model.pkl
#
# To:
#
# S3 Bucket
#
# Download During Deployment

# ============================================================
# COMMON AWS SERVICES
# ============================================================

# EC2
# S3
# Lambda

# ============================================================
# COMMON TOOLS
# ============================================================

# boto3
# AWS Console
# AWS CLI

# ============================================================
# AWS WORKFLOW
# ============================================================

# Code
#
# ↓
#
# GitHub
#
# ↓
#
# EC2
#
# ↓
#
# Run Application
#
# ↓
#
# Store Files In S3

# ============================================================
# SUMMARY
# ============================================================

print("""
AWS BASICS SUMMARY

Main Services:

EC2
S3
Lambda

EC2:

✔ Virtual Machine
✔ Host APIs
✔ Deploy AI Apps

S3:

✔ Store Files
✔ Store Models
✔ Store Datasets

Lambda:

✔ Serverless Functions
✔ Event Driven
✔ Automation

Python Library:

boto3

Applications:

✔ AI Deployment
✔ FastAPI Hosting
✔ RAG Systems
✔ Chatbots
✔ ML Applications

Benefits:

✔ Scalable
✔ Reliable
✔ Global Infrastructure
✔ Industry Standard
✔ Cloud Ready
""")
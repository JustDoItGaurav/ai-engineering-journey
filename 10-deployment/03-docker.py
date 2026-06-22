# ============================================================
# DOCKER
# ============================================================

# Docker is a platform used to package applications
# into containers.
#
# Container:
#
# A lightweight environment that contains:
#
# ✔ Code
# ✔ Libraries
# ✔ Dependencies
# ✔ Runtime
#
# Why Docker?
#
# ✔ Works On Any Machine
# ✔ Easy Deployment
# ✔ Consistent Environment
# ✔ Industry Standard
# ✔ Essential For AI Deployment

# ============================================================
# INSTALL DOCKER
# ============================================================

# Download:
#
# https://www.docker.com/

# Verify Installation:
#
# docker --version

# ============================================================
# CHECK DOCKER VERSION
# ============================================================

# Command:
#
# docker --version

# Example:
#
# Docker version 27.x.x

# ============================================================
# WHAT IS A CONTAINER?
# ============================================================

# Example:
#
# FastAPI App
#
# Dependencies:
#
# fastapi
# uvicorn
# openai
# pandas
#
# Docker packages everything together.

# ============================================================
# WHAT IS AN IMAGE?
# ============================================================

# Image:
#
# Blueprint For Containers
#
# Container:
#
# Running Instance Of Image

# ============================================================
# HELLO WORLD CONTAINER
# ============================================================

# Command:
#
# docker run hello-world

# ============================================================
# LIST IMAGES
# ============================================================

# Command:
#
# docker images

# ============================================================
# LIST CONTAINERS
# ============================================================

# Running Containers
#
# docker ps

# All Containers
#
# docker ps -a

# ============================================================
# PULL IMAGE
# ============================================================

# Download Image From Docker Hub
#
# docker pull python:3.11

# ============================================================
# RUN PYTHON CONTAINER
# ============================================================

# docker run -it python:3.11

# ============================================================
# CREATE SIMPLE PYTHON APP
# ============================================================

# app.py

print("Hello Docker")

# ============================================================
# DOCKERFILE
# ============================================================

# Dockerfile tells Docker how
# to build an image.

# File Name:
#
# Dockerfile

"""
FROM python:3.11

COPY app.py .

CMD ["python", "app.py"]
"""

# ============================================================
# DOCKERFILE EXPLANATION
# ============================================================

# FROM
#
# Base Image
#
# COPY
#
# Copy Files
#
# CMD
#
# Run Command

# ============================================================
# BUILD IMAGE
# ============================================================

# docker build -t myapp .

# ============================================================
# VIEW IMAGES
# ============================================================

# docker images

# ============================================================
# RUN IMAGE
# ============================================================

# docker run myapp

# ============================================================
# PORT MAPPING
# ============================================================

# Host Port : Container Port
#
# Example:
#
# docker run -p 8000:8000 myapp

# ============================================================
# FASTAPI PROJECT
# ============================================================

# Structure:
#
# project/
#
# ├── app.py
# ├── requirements.txt
# └── Dockerfile

# ============================================================
# REQUIREMENTS FILE
# ============================================================

# requirements.txt

"""
fastapi
uvicorn
"""

# ============================================================
# FASTAPI APP
# ============================================================

# app.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():

    return {
        "message": "Hello Docker"
    }

# ============================================================
# FASTAPI DOCKERFILE
# ============================================================

"""
FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [
"uvicorn",
"app:app",
"--host",
"0.0.0.0",
"--port",
"8000"
]
"""

# ============================================================
# BUILD FASTAPI IMAGE
# ============================================================

# docker build -t fastapi-app .

# ============================================================
# RUN FASTAPI CONTAINER
# ============================================================

# docker run -p 8000:8000 fastapi-app

# Open:
#
# http://localhost:8000

# ============================================================
# ENVIRONMENT VARIABLES
# ============================================================

# Example:
#
# OPENAI_API_KEY

# Run Container:
#
# docker run
# -e OPENAI_API_KEY=abc123
# myapp

# ============================================================
# USING .ENV FILE
# ============================================================

# .env

"""
OPENAI_API_KEY=abc123
"""

# ============================================================
# VOLUMES
# ============================================================

# Volumes allow persistent storage.
#
# Example:
#
# docker run
# -v mydata:/data
# myapp

# ============================================================
# STOP CONTAINER
# ============================================================

# docker stop container_id

# ============================================================
# REMOVE CONTAINER
# ============================================================

# docker rm container_id

# ============================================================
# REMOVE IMAGE
# ============================================================

# docker rmi image_name

# ============================================================
# PRACTICAL EXAMPLE 1
# FASTAPI DEPLOYMENT
# ============================================================

# Build

# docker build -t ai-api .

# Run

# docker run -p 8000:8000 ai-api

# ============================================================
# PRACTICAL EXAMPLE 2
# AI CHATBOT CONTAINER
# ============================================================

# Project:
#
# chatbot/
#
# ├── app.py
# ├── requirements.txt
# └── Dockerfile

# Build

# docker build -t chatbot .

# Run

# docker run -p 8000:8000 chatbot

# ============================================================
# PRACTICAL EXAMPLE 3
# RAG APPLICATION
# ============================================================

# Files:
#
# app.py
# vector_db/
# requirements.txt
# Dockerfile

# Build

# docker build -t rag-app .

# Run

# docker run -p 8000:8000 rag-app

# ============================================================
# COMMON COMMANDS
# ============================================================

# docker --version
# docker images
# docker ps
# docker ps -a
# docker pull
# docker build
# docker run
# docker stop
# docker rm
# docker rmi

# ============================================================
# DOCKER WORKFLOW
# ============================================================

# App
#
# ↓
#
# Dockerfile
#
# ↓
#
# Build Image
#
# ↓
#
# Run Container
#
# ↓
#
# Deploy

# ============================================================
# SUMMARY
# ============================================================

print("""
DOCKER SUMMARY

Check Version:

docker --version

Build Image:

docker build -t myapp .

Run Container:

docker run myapp

Port Mapping:

docker run -p 8000:8000 myapp

Important Components:

✔ Image
✔ Container
✔ Dockerfile
✔ Volumes
✔ Environment Variables

Common Commands:

docker build
docker run
docker ps
docker stop
docker rm

Applications:

✔ FastAPI Deployment
✔ AI APIs
✔ Chatbots
✔ RAG Systems
✔ Production Deployment

Benefits:

✔ Portable
✔ Consistent Environment
✔ Easy Deployment
✔ Industry Standard
✔ Cloud Ready
""")
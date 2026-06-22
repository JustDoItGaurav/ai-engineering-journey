# ============================================================
# FASTAPI
# ============================================================

# FastAPI is a modern Python framework
# used to build APIs quickly.
#
# API = Application Programming Interface
#
# APIs allow applications to communicate.
#
# Example:
#
# User
# ↓
# Request
# ↓
# FastAPI
# ↓
# Response
#
# Why FastAPI?
#
# ✔ Fast
# ✔ Easy To Learn
# ✔ Automatic Documentation
# ✔ Used In AI Applications
# ✔ Industry Standard
#
# Install:
#
# pip install fastapi
# pip install uvicorn

# ============================================================
# IMPORTING FASTAPI
# ============================================================

from fastapi import FastAPI

# ============================================================
# CREATE APPLICATION
# ============================================================

app = FastAPI()

# ============================================================
# FIRST API
# ============================================================

@app.get("/")
def home():

    return {
        "message": "Hello FastAPI"
    }

# ============================================================
# RUN APPLICATION
# ============================================================

# Command:
#
# uvicorn filename:app --reload
#
# Example:
#
# uvicorn main:app --reload

# ============================================================
# OPEN API
# ============================================================

# Browser:
#
# http://127.0.0.1:8000

# ============================================================
# AUTOMATIC DOCUMENTATION
# ============================================================

# Swagger UI
#
# http://127.0.0.1:8000/docs

# ============================================================
# RETURNING JSON
# ============================================================

@app.get("/student")
def student():

    return {
        "name": "Rahul",
        "age": 21,
        "course": "AI"
    }

# ============================================================
# PATH PARAMETERS
# ============================================================

@app.get("/student/{student_id}")
def get_student(student_id: int):

    return {
        "student_id": student_id
    }

# Example:
#
# /student/101

# ============================================================
# MULTIPLE PATH PARAMETERS
# ============================================================

@app.get("/student/{student_id}/course/{course}")
def details(
    student_id: int,
    course: str
):

    return {
        "id": student_id,
        "course": course
    }

# ============================================================
# QUERY PARAMETERS
# ============================================================

@app.get("/search")
def search(
    keyword: str
):

    return {
        "keyword": keyword
    }

# Example:
#
# /search?keyword=AI

# ============================================================
# MULTIPLE QUERY PARAMETERS
# ============================================================

@app.get("/products")
def products(
    category: str,
    limit: int = 10
):

    return {
        "category": category,
        "limit": limit
    }

# Example:
#
# /products?category=laptop&limit=5

# ============================================================
# POST REQUEST
# ============================================================

# POST is used to send data.

@app.post("/create")
def create():

    return {
        "message": "Created Successfully"
    }

# ============================================================
# REQUEST BODY
# ============================================================

from pydantic import BaseModel

class Student(BaseModel):

    name: str

    age: int

# ============================================================
# RECEIVE JSON DATA
# ============================================================

@app.post("/student")
def create_student(
    student: Student
):

    return {
        "name": student.name,
        "age": student.age
    }

# Example JSON:
#
# {
#     "name":"John",
#     "age":22
# }

# ============================================================
# PUT REQUEST
# ============================================================

@app.put("/student/{student_id}")
def update_student(
    student_id: int
):

    return {
        "message": f"Student {student_id} Updated"
    }

# ============================================================
# DELETE REQUEST
# ============================================================

@app.delete("/student/{student_id}")
def delete_student(
    student_id: int
):

    return {
        "message": f"Student {student_id} Deleted"
    }

# ============================================================
# RESPONSE MODEL
# ============================================================

class UserResponse(BaseModel):

    name: str

    age: int

@app.get(
    "/user",
    response_model=UserResponse
)
def user():

    return {
        "name": "Alex",
        "age": 25
    }

# ============================================================
# STATUS CODES
# ============================================================

from fastapi import status

@app.get("/status")
def check():

    return {
        "status_code":
        status.HTTP_200_OK
    }

# ============================================================
# PRACTICAL EXAMPLE 1
# STUDENT API
# ============================================================

students = [
    {
        "id": 1,
        "name": "John"
    },
    {
        "id": 2,
        "name": "Alice"
    }
]

@app.get("/students")
def get_students():

    return students

# ============================================================
# PRACTICAL EXAMPLE 2
# HOUSE PRICE PREDICTION API
# ============================================================

@app.post("/predict-price")
def predict_price(
    area: int
):

    predicted_price = area * 50

    return {
        "area": area,
        "predicted_price": predicted_price
    }

# ============================================================
# PRACTICAL EXAMPLE 3
# AI CHATBOT API
# ============================================================

class Prompt(BaseModel):

    message: str

@app.post("/chat")
def chatbot(
    prompt: Prompt
):

    return {
        "user": prompt.message,
        "assistant": "Hello, I am an AI assistant."
    }

# ============================================================
# COMMON HTTP METHODS
# ============================================================

# GET
# POST
# PUT
# DELETE

# ============================================================
# COMMON FASTAPI COMPONENTS
# ============================================================

# FastAPI()
# BaseModel
# Path Parameters
# Query Parameters
# Request Body
# Response Model

# ============================================================
# FASTAPI WORKFLOW
# ============================================================

# User
#
# ↓
#
# API Request
#
# ↓
#
# FastAPI Route
#
# ↓
#
# Python Function
#
# ↓
#
# JSON Response

# ============================================================
# SUMMARY
# ============================================================

print("""
FASTAPI SUMMARY

Install:

pip install fastapi
pip install uvicorn

Run:

uvicorn main:app --reload

Documentation:

/docs

HTTP Methods:

GET
POST
PUT
DELETE

Important Components:

✔ FastAPI()
✔ BaseModel
✔ Request Body
✔ Query Parameters
✔ Path Parameters
✔ Response Model

Applications:

✔ AI APIs
✔ ML Model Deployment
✔ Chatbots
✔ Web Applications

Benefits:

✔ Fast
✔ Easy To Learn
✔ Automatic Docs
✔ Production Ready
✔ Industry Standard
""")
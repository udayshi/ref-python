# FastAPI CRUD Application with SQLAlchemy and Pydantic

This project is a basic implementation of a CRUD application using FastAPI, SQLAlchemy, and Pydantic, structured into multiple files for better modularity and maintainability. The application provides APIs for managing items, demonstrating best practices for modern Python web development.

## Features
- Create, read, update, and delete (CRUD) operations for items.
- Utilizes SQLAlchemy for database interactions.
- Pydantic for data validation and serialization.
- Modular file structure for scalability.
- SQLite as the default database (can be replaced with other databases).


## Setup

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --port 8080  --reload
http://127.0.0.1:8080
http://127.0.0.1:8080/docs
```

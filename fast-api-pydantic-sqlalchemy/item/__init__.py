from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from db import engine, Base, get_db

# Initialize database
Base.metadata.create_all(bind=engine)
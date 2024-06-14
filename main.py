# main.py

from fastapi import FastAPI
from database.base import Base
from database.engine import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)
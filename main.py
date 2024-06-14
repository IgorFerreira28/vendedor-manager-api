# main.py

from fastapi import FastAPI
from database.base import Base
from database.engine import engine
from api.routes import router as vendedor_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(vendedor_router)
# main.py

from fastapi import FastAPI
from api.routes.routes_sellers import router as vendedor_router
from api.routes.routes_sales import router as vendas_router

app = FastAPI()

app.include_router(vendedor_router)
app.include_router(vendas_router)
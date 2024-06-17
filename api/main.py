# main.py

from fastapi import FastAPI
from api.routes.routes_sellers import router as vendedor_router
from api.routes.routes_sales import router as vendas_router
from api.routes.routes_payment import router as pagamento_router
from api.routes.routes_sales_uf import router as vendas_uf_router

app = FastAPI()

app.include_router(vendedor_router)
app.include_router(vendas_router)
app.include_router(pagamento_router)
app.include_router(vendas_uf_router)
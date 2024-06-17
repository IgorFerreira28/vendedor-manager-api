#routes/routes_sales.py

from fastapi import APIRouter, UploadFile
from api.controllers.controller_sales import insert_sales_to_database, insert_to_sales

router = APIRouter()

@router.post("/upload_sales_csv")
async def upload_csv(file: UploadFile):
    
    insert_sales_to_database(file)
    
    return {"message": "Vendas inseridas com sucesso!"}

@router.post("/add/sale")
async def add_sale(cpf: int, data: str, valor: int, nome: str, cliente: str, custo: int, canal: str):
    insert_to_sales(cpf, data, valor, nome, cliente, custo, canal)
    return {"message": "Venda inserida com sucesso!"}
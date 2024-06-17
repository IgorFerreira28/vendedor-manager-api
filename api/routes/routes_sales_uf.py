#routes/routes_sales_uf.py

from fastapi import APIRouter, HTTPException
from api.controllers.controller_sales_uf import create_table, get_sales_uf, new_calculate_media



router = APIRouter()

@router.get("/create_table_sales_uf")
async def create_table_sales_uf():
    create_table()
    return {"message": "Tabela criada com sucesso!"}

@router.get("/get/table_sales_uf")
async def get_table_sales_uf():
    comissions = get_sales_uf()
    if not comissions:
        raise HTTPException(status_code=404, detail="Nenhum vendedor encontrado")
    return comissions

@router.put("/put/table_sales_uf")
async def update_table_sales_uf():
    new_calculate_media()
    return {"message": "Médias Atualizadas com sucesso!"}
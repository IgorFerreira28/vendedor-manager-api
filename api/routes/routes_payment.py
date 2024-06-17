#routes/routes_payment.py
from fastapi import APIRouter, HTTPException
from api.controllers.controller_payment import create_table, get_comission, new_calculate_comission

router = APIRouter()

@router.get("/create_table_payment")
async def create_table_route():
    create_table()
    return {"message": "Tabela criada com sucesso!"}

@router.get("/get/commission")
async def get_payments():
    comissions = get_comission()
    if not comissions:
        raise HTTPException(status_code=404, detail="Nenhum vendedor encontrado")
    return comissions

@router.put("/put/commission")
async def update_payment():
    new_calculate_comission()
    return {"message": "Comissões Atualizadas com sucesso!"}


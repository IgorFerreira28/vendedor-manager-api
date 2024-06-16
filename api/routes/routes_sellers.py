#api/routes/routes_sellers.py

from fastapi import APIRouter, HTTPException
from database.vendedores import Vendedor
from api.controllers.controller_sellers import get_sellers, get_seller, add_seller, update_seller, delete_seller

router = APIRouter()


@router.post("/add/seller")
async def add_vendedor(cpf: int, nome: str, email: str, nascimento: str, uf: str):
    add_seller(cpf, nome, email, nascimento, uf)
    print(nome, email, nascimento, uf, cpf)
    return {"message": "Vendedor adicionado com sucesso!"}

@router.get("/get/sellers")
async def get_vendedores():
    vendedores = get_sellers()
    if not vendedores:
        raise HTTPException(status_code=404, detail="Nenhum vendedor encontrado")
    return vendedores

@router.get("/get/seller/{cpf}")
async def get_vendedor(cpf: int):
    vendedor = get_seller(cpf)
    if not vendedor:
        raise HTTPException(status_code=404, detail="Vendedor não encontrado")
    return vendedor

@router.put("/update/seller/{cpf}")
async def update_vendedor(cpf: int, nome: str, email: str, nascimento: str, uf: str):
    vendedor = get_seller(cpf)
    if not vendedor:
        raise HTTPException(status_code=404, detail="Vendedor não encontrado")
    
    update_seller(cpf, nome, email, nascimento, uf)
    return {"message": "Vendedor atualizado com sucesso!", "vendedor": nome}

@router.delete("/delete/seller/{cpf}")
async def delete_vendedor(cpf: int):
    vendedor = get_seller(cpf)
    if not vendedor:
        raise HTTPException(status_code=404, detail="Vendedor não encontrado")
    else:
        delete_seller(cpf)
        return {"message": "Vendedor deletado com sucesso!", "vendedor": cpf}
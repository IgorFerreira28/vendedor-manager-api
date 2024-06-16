#api/routes/routes_sellers.py

from fastapi import APIRouter, Depends, HTTPException, status, UploadFile
from database.session import get_db
from database.vendedores import Vendedor
from api.controllers.controller_sellers import get_sellers, get_seller, add_seller, update_seller, delete_seller

router = APIRouter()


@router.post("/add/seller")
async def add_vendedor(cpf: int, nome: str, email: str, nascimento: str, uf: str, db = Depends(get_db)):
    add_seller(cpf, nome, email, nascimento, uf, db)
    return {"message": "Vendedor adicionado com sucesso!"}

@router.get("/get/sellers")
async def get_vendedores(db = Depends(get_db)):
    vendedores = get_sellers(db)
    if not vendedores:
        raise HTTPException(status_code=404, detail="Nenhum vendedor encontrado")
    return vendedores

@router.get("get/seller/{cpf}")
async def get_vendedor(cpf: int, db = Depends(get_db)):
    vendedor = get_seller(cpf, db)
    if not vendedor:
        raise HTTPException(status_code=404, detail="Vendedor não encontrado")
    return vendedor

@router.put("update/seller/{cpf}")
async def update_vendedor(cpf: int, nome: str, email: str, nascimento: str, uf: str, db = Depends(get_db)):
    vendedor = update_seller(cpf, db)
    if not vendedor:
        raise HTTPException(status_code=404, detail="Vendedor não encontrado")
    
    update_seller(cpf, nome, email, nascimento, uf, db)
    return {"message": "Vendedor atualizado com sucesso!", "vendedor": nome}

@router.delete("delete/seller/{cpf}")
async def delete_vendedor(cpf: int, db = Depends(get_db)):
    vendedor = delete_seller(cpf, db)
    if not vendedor:
        raise HTTPException(status_code=404, detail="Vendedor não encontrado")
    
    db.delete(vendedor)
    db.commit()
    return {"message": "Vendedor deletado com sucesso!", "vendedor": vendedor.nome}
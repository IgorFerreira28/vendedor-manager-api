# api/routes/vendedor.py

from fastapi import APIRouter, Depends, HTTPException, status, UploadFile
from database.session import get_db
from database.vendedores import Vendedor
from api.controllers.controller_sellers import get_sellers

router = APIRouter()


@router.get("/get/vendedores")
async def get_vendedores(db = Depends(get_db)):
    vendedores = get_sellers(db)
    return vendedores

@router.get("get/vendedor/{cpf}")
async def get_vendedor(cpf: int, db = Depends(get_db)):
    vendedor = db.query(Vendedor).filter(Vendedor.cpf == cpf).first()
    if not vendedor:
        raise HTTPException(status_code=404, detail="Vendedor não encontrado")
    return vendedor


@router.delete("delete/vendedor/{cpf}")
async def delete_vendedor(cpf: int, db = Depends(get_db)):
    vendedor = db.query(Vendedor).filter(Vendedor.cpf == cpf).first()
    if not vendedor:
        raise HTTPException(status_code=404, detail="Vendedor não encontrado")
    
    db.delete(vendedor)
    db.commit()
    return {"message": "Vendedor deletado com sucesso!", "vendedor": vendedor.nome}
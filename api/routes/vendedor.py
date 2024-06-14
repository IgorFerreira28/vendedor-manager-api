# api/routes/vendedor.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.session import get_db
from api.models.vendedores import Vendedor
from pydantic import BaseModel, EmailStr, constr


router = APIRouter()

class Vendedor(BaseModel):
    cpf: constr(max_length=11, min_length=11) # type: ignore
    nome: constr(max_length=100) # type: ignore
    email: EmailStr
    nascimento: constr(max_length=10, min_length=10) # type: ignore
    uf: constr(max_length=2) # type: ignore

@router.post("create/vendedor")
async def create_vendedor(vendedor: Vendedor, db: Session = Depends(get_db)):
    if db.query(Vendedor).filter(Vendedor.cpf == vendedor.cpf).first():
        raise HTTPException(status_code=400, detail="CPF já cadastrado")
    
    if db.query(Vendedor).filter(Vendedor.email == vendedor.email).first():
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    
    #cria novo vendedor
    new_vendedor = Vendedor(cpf=vendedor.cpf, nome=vendedor.nome, email=vendedor.email, nascimento=vendedor.nascimento, uf=vendedor.uf)

    db.add(new_vendedor)
    db.commit()
    db.refresh(new_vendedor)
    return {"message": "Vendedor cadastrado com sucesso!", "vendedor": new_vendedor.nome}

@router.get("get/vendedores")
async def get_vendedores(db: Session = Depends(get_db)):
    vendedores = db.query(Vendedor).all()
    return vendedores

@router.get("get/vendedor/{cpf}")
async def get_vendedor(cpf: int, db: Session = Depends(get_db)):
    vendedor = db.query(Vendedor).filter(Vendedor.cpf == cpf).first()
    if not vendedor:
        raise HTTPException(status_code=404, detail="Vendedor não encontrado")
    return vendedor

@router.put("update/vendedor/{cpf}")
async def update_vendedor(cpf: int, vendedor: Vendedor, db: Session = Depends(get_db)):
    vendedor = db.query(Vendedor).filter(Vendedor.cpf == cpf).first()
    if not vendedor:
        raise HTTPException(status_code=404, detail="Vendedor não encontrado")
    
    vendedor.nome = vendedor.nome
    vendedor.email = vendedor.email
    vendedor.nascimento = vendedor.nascimento
    vendedor.uf = vendedor.uf

    db.commit()
    db.refresh(vendedor)
    return {"message": "Vendedor atualizado com sucesso!", "vendedor": vendedor.nome}

@router.delete("delete/vendedor/{cpf}")
async def delete_vendedor(cpf: int, db: Session = Depends(get_db)):
    vendedor = db.query(Vendedor).filter(Vendedor.cpf == cpf).first()
    if not vendedor:
        raise HTTPException(status_code=404, detail="Vendedor não encontrado")
    
    db.delete(vendedor)
    db.commit()
    return {"message": "Vendedor deletado com sucesso!", "vendedor": vendedor.nome}
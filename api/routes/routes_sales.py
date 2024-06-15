from fastapi import APIRouter, Depends, HTTPException, status, UploadFile
from api.controllers.controller_sales import insert_sales_to_database
from database.session import get_db
from sqlite3 import Cursor

router = APIRouter()

@router.post("/upload_csv")
async def upload_csv(file: UploadFile, db: Cursor = Depends(get_db)):
    
    insert_sales_to_database(db, file)
    
    return {"message": "Vendas inseridas com sucesso!"}
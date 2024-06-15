from fastapi import UploadFile, HTTPException, status
from sqlite3 import Cursor
import sqlite3
import pandas as pd

def insert_sales_to_database(db: Cursor, file: UploadFile):
    cnx = sqlite3.connect("database/data.sqlite")

    if not file or not file.filename.endswith(".csv"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Dados inválidos")
    
    data = pd.read_csv(file.file)

    data.to_sql("sales", cnx, if_exists="append", index=False)

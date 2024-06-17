# api/controllers/controller_sellers.py
from fastapi import UploadFile, HTTPException, status
from database.session import get_db
import pandas as pd
        

def insert_file_sellers(file: UploadFile, db = get_db()):
    # Verifica se o arquivo é válido
    if not file or not file.filename.endswith(".csv"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Dados inválidos")

    try:
        # Lê o arquivo CSV
        data = pd.read_csv(file.file)

        create_table_query = """
        CREATE TABLE IF NOT EXISTS sellers (
            "nascimento" DATA,
            "nome" TEXT,
            "email" TEXT,
            "cpf" INTEGER PRIMARY KEY,
            "uf" TEXT
        );
        """
        db.execute(create_table_query)
        db.commit()

        data.to_sql("sellers", db, if_exists="append", index=False)


    except pd.errors.EmptyDataError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Arquivo CSV está vazio")
    except pd.errors.ParserError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Erro ao analisar o arquivo CSV")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    finally:
        # Certifica-se de que a conexão ao banco de dados seja fechada
        if db:
            db.close()


def get_sellers(db = get_db()):

    cursor = db.cursor()

    try:
        cursor.execute("SELECT * FROM sellers")
        return cursor.fetchall()
    finally:
        cursor.close()

def get_seller(cpf, db = get_db()):
    cursor = db.cursor()
    
    cursor.execute(f"SELECT * FROM sellers WHERE cpf = ?", (cpf,))

    return cursor.fetchall()


def add_seller(cpf, nome, email, nascimento, uf, db = get_db()):

    if not cpf or not nome or not email or not nascimento or not uf:
        return "Dados inválidos"
    
    try:
        db.execute(
            f"INSERT INTO sellers (cpf, nome, email, nascimento, uf) VALUES (?, ?, ?, ?, ?)", (cpf, nome, email, nascimento, uf)
        )

        db.commit()
    except:
        return False
    

def update_seller(cpf, nome, email, nascimento, uf, db = get_db()):
    try:
        db.execute(
            f"UPDATE sellers SET nome = ?, email = ?, nascimento = ?, uf = ? WHERE cpf = ?", (nome, email, nascimento, uf, cpf))
        
        db.commit()
    except:
        return False

def delete_seller(cpf, db = get_db()):
    try:
        db.execute(f"DELETE FROM sellers WHERE cpf = ?", (cpf,))

        db.commit()
    except:
        return "Não foi possível deletar o vendedor"
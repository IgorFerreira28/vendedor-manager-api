#api/controllers/controller_sales.py

from fastapi import UploadFile, HTTPException, status
import pandas as pd
from database.session import get_db

def insert_sales_to_database(file: UploadFile, db = get_db()):
    # Verifica se o arquivo é válido
    if not file or not file.filename.endswith(".csv"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Dados inválidos")

    try:
        # Lê o arquivo CSV
        data = pd.read_csv(file.file, thousands='.', decimal=',')

        # Cria a tabela 'sales' com uma coluna 'id' como chave primária, se não existir
        create_table_query = """
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cpf INTEGER,
            "data_da_venda" TEXT,
            "nome_do_vendedor" TEXT,
            "valor_da_venda" INTEGER,
            "tipo_de_cliente" TEXT,
            "canal_de_venda" TEXT,
            "custo_da_venda" INTEGER,
            FOREIGN KEY (cpf) REFERENCES sellers(cpf)
        );
        """
        db.execute(create_table_query)
        db.commit()

        # Insere os dados do CSV na tabela 'sales'
        data.to_sql("sales", db, if_exists="append", index=False)

        
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

def insert_to_sales(cpf, data, valor, nome, cliente, custo, canal, db = get_db()):
    try:
        db.execute("INSERT INTO sales (cpf, data_da_venda, nome_do_vendedor, valor_da_venda, tipo_de_cliente, canal_de_venda, custo_da_venda) VALUES (?, ?, ?, ?, ?, ?, ?)", (cpf, data, nome, valor, cliente, canal, custo))
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    finally:
        if db:
            db.close()
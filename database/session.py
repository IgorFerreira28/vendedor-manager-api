# database/session.py

import sqlite3
import os


def get_db():
    local_path = os.path.dirname(os.path.abspath(__file__))

    print("/Users/Igor Ferreira/Documents/GitHub/vendedor-maneger-api/database/data.sqlite")
    conn = sqlite3.connect(
        "/Users/Igor Ferreira/Documents/GitHub/vendedor-maneger-api/database/data.sqlite"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS sellers (
            cpf INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            nascimento TEXT NOT NULL,
            uf TEXT NOT NULL
        )
        """
    )
    

    return cursor
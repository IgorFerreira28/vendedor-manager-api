# api/controllers/controller_sellers.py

from database.session import get_db
        

def get_sellers(db = get_db()):

    cursor = db.cursor()

    cursor.execute(f"SELECT * FROM sellers")

    return cursor.fetchall()

def get_seller(cpf, db = get_db()):
    cursor = db.cursor()
    
    cursor.execute(f"SELECT * FROM sellers WHERE cpf = ?", (cpf))

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
        db.execute(f"DELETE FROM sellers WHERE cpf = ?", (cpf))

        db.commit()
    except:
        return False
# api/controllers/controller_sellers.py

from database.session import get_db
        

def get_sellers(db):

    db.execute(f"SELECT * FROM sellers")

    return db.fetchall()

def get_seller(cpf, db):
    db.execute(f"SELECT * FROM sellers WHERE cpf = ?", (cpf))

    return db.fetchall()


def add_seller(cpf, nome, email, nascimento, uf, db):

    if not cpf or not nome or not email or not nascimento or not uf:
        return "Dados inválidos"
    
    try:
        db.execute(
            f"INSERT INTO sellers (cpf, nome, email, nascimento, uf) VALUES (?, ?, ?, ?, ?)", (cpf, nome, email, nascimento, uf)
        )

        db.commit()
    except:
        return False
    

def update_seller(cpf, nome, email, nascimento, uf, db):
    try:
        db.execute(
            f"UPDATE sellers SET nome = ?, email = ?, nascimento = ?, uf = ? WHERE cpf = ?", (nome, email, nascimento, uf, cpf))
        
        db.commit()
    except:
        return False

def delete_seller(cpf, db):
    try:
        db.execute(f"DELETE FROM sellers WHERE cpf = ?", (cpf))

        db.commit()
    except:
        return False
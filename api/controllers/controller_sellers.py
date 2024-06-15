from database.session import get_db
        

def get_sellers(db):

    db.execute(f"SELECT * FROM sellers")

    return db.fetchall()


def add_seller(cpf, nome, email, nascimento, uf):
    cursor = get_db()

    if not cpf or not nome or not email or not nascimento or not uf:
        return "Dados inválidos"
    cursor.execute(
        f"INSERT INTO sellers (cpf, nome, email, nascimento, uf) VALUES (?, ?, ?, ?, ?)", (cpf, nome, email, nascimento, uf)
    )

    cursor.commit()

def update_seller(cpf, nome, email, nascimento, uf):
    cursor = get_db()

    cursor.execute(
        f"UPDATE sellers SET nome = '{nome}', email = '{email}', nascimento = '{nascimento}', uf = '{uf}' WHERE cpf = '{cpf}'")
    
    cursor.commit()

def delete_seller(cpf):
    cursor = get_db()

    cursor.execute(f"DELETE FROM sellers WHERE cpf = '{cpf}'")

    cursor.commit()
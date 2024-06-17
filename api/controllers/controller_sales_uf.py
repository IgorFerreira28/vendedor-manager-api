#api/controllers/controller_sales_uf.py

from database.session import get_db


def create_table(db = get_db()):
    slq_query = """CREATE TABLE IF NOT EXISTS status_uf AS
        SELECT 
            sellers.uf AS estado, 
            SUM(sales.valor_da_venda) AS volume_de_vendas,
            COUNT(DISTINCT sellers.cpf) AS quantidade_de_vendedores,
            (SUM(sales.valor_da_venda) / COUNT(DISTINCT sellers.cpf)) AS media_de_vendas
        FROM 
            sales
        LEFT JOIN 
            sellers ON sellers.cpf = sales.cpf 
        GROUP BY 
            sellers.uf;"""
    
    db.execute(slq_query)
    db.commit()

def get_sales_uf(db = get_db()):
    try:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM status_uf")
        return cursor.fetchall()
    finally:
        cursor.close()

def new_calculate_media(db = get_db()):
    db.execute('DROP TABLE IF EXISTS nova_tabela_media')
    
    db.execute('''
        CREATE TABLE nova_tabela_media AS
        SELECT 
            sellers.uf AS estado, 
            SUM(sales.valor_da_venda) AS volume_de_vendas,
            COUNT(DISTINCT sellers.cpf) AS quantidade_de_vendedores,
            (SUM(sales.valor_da_venda) / COUNT(DISTINCT sellers.cpf)) AS media_de_vendas
        FROM 
            sales
        LEFT JOIN 
            sellers ON sellers.cpf = sales.cpf 
        GROUP BY 
            sellers.uf;''')
    db.commit()
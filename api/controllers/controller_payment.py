#api/controllers/controller_payment.py

from database.session import get_db

def create_table(db = get_db()):
    slq_query = """CREATE TABLE IF NOT EXISTS payments AS
    SELECT 
        sellers.nome AS nome_vendedor, 
        SUM(
            CASE 
                WHEN sales.canal_de_venda = 'Online' 
                    THEN (
                        CASE 
                            WHEN sales.valor_da_venda * 0.10 * 0.80 > 1000 
                                THEN sales.valor_da_venda * 0.90 
                                ELSE sales.valor_da_venda * 0.10 * 0.80 
                        END
                    )
                ELSE (
                    CASE 
                        WHEN sales.valor_da_venda > 1000 
                            THEN sales.valor_da_venda * 0.10 * 0.80 
                            ELSE sales.valor_da_venda * 0.10 
                    END
                ) 
            END
        ) AS total_vendas 
    FROM 
        sales 
    LEFT JOIN 
        sellers ON sellers.cpf = sales.cpf 
    GROUP BY 
        sellers.nome 
    ORDER BY 
        sellers.nome;
    """

    db.execute(slq_query)
    db.commit()

def get_comission(db = get_db()):

    try:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM payments")
        return cursor.fetchall()
    finally:
        cursor.close()

def new_calculate_comission(db = get_db()):
    db.execute('DROP TABLE IF EXISTS nova_tabela_comissao')

        # Criar a nova tabela com os dados atualizados
    db.execute('''
            CREATE TABLE nova_tabela_comissao AS
            SELECT 
                sales."Data da Venda", 
                sellers.nome AS nome_vendedor, 
                SUM(
                    CASE 
                        WHEN sales."Canal da Venda" = 'Online' 
                            THEN (
                                CASE 
                                    WHEN sales."Valor da Venda" * 0.10 * 0.80 > 1000 
                                        THEN sales."Valor da Venda" * 0.90 
                                        ELSE sales."Valor da Venda" * 0.10 * 0.80 
                                END
                            )
                        ELSE (
                            CASE 
                                WHEN sales."Valor da Venda" > 1000 
                                    THEN sales."Valor da Venda" * 0.10 * 0.80 
                                    ELSE sales."Valor da Venda" * 0.10 
                            END
                        ) 
                    END
                ) AS total_vendas 
            FROM 
                sales 
            LEFT JOIN 
                sellers ON sellers.cpf = sales.cpf 
            GROUP BY 
                sales."Data da Venda", sellers.nome 
            ORDER BY 
                sellers.nome;
        ''')

        # Confirmar as alterações no banco de dados
    db.commit()
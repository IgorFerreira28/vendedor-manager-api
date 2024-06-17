# vendedor-maneger-api
Este projeto implementa uma API utilizando FastAPI para gerenciar informações de vendedores, calcular comissões de vendas e apresentar análises por canal e estado. A solução foi desenvolvida em Python e utiliza SQLite como banco de dados para persistência dos dados.

Estrutura do Projeto
O projeto está estruturado da seguinte maneira:

main.py: Arquivo principal onde a aplicação FastAPI é configurada e as rotas são incluídas.

database/: Contém o arquivo session.py para gerenciar a conexão com o banco de dados SQLite (data.sqlite), o banco de dados está persistindo localmente.

api/
    routes/: Contém os arquivos de rotas para diferentes partes da API (routes_sellers.py, routes_sales.py, routes_payment.py, routes_sales_uf.py).

    controllers/: Implementações dos métodos para manipulação de dados nos bancos de dados (controller_sellers.py, controller_sales.py, controller_payment.py, controller_sales_uf.py).

Configuração
Instalação das Dependências

Certifique-se de ter Python 3.7+ instalado. Em seguida, instale as dependências utilizando o pip:

pip install fastapi
pip install uvicorn 
pip install pandas

Executando a Aplicação

Para iniciar o servidor de desenvolvimento, execute o seguinte comando na raiz do projeto:

py -m uvicorn api.main:app --reload

após a execução do comando, cole em seu navegador de preferência o seguinte caminho:  http://127.0.0.1:8000/docs

Uso da API:

A API oferece endpoints para gerenciar vendedores, vendas, comissões e médias de vendas por estado. Abaixo estão os principais endpoints disponíveis:

Vendedores:

POST /add/csv_sellers: Adiciona vendedores a partir de um arquivo CSV.
POST /add/seller: Adiciona um vendedor manualmente.
GET /get/sellers: Retorna todos os vendedores.
GET /get/seller/{cpf}: Retorna um vendedor específico por CPF.
PUT /update/seller/{cpf}: Atualiza os dados de um vendedor.
DELETE /delete/seller/{cpf}: Deleta um vendedor por CPF.

Vendas:

POST /upload_sales_csv: Adiciona vendas a partir de um arquivo CSV.
POST /add/sale: Adiciona uma venda manualmente.

Comissões:

GET /get/commission: Retorna as comissões de cada vendedor.
PUT /put/commission: Recalcula as comissões com base nos dados atuais de vendas.

Média de Vendas por Estado:

GET /get/table_sales_uf: Retorna a média de vendas por estado.
GET /create_table_sales_uf: Cria a tabela de média de vendas por estado.
PUT /put/table_sales_uf: Atualiza as médias de vendas por estado.

Casos de Uso Implementados
Gerenciamento de Vendedores:

Implementado todas as funções CRUD (Create, Read, Update, Delete) para gerenciar vendedores, incluindo nome, CPF, data de nascimento, e-mail e estado (UF).

Leitura de Planilha de Vendedores:

Implementada função para ler uma planilha de dados de vendedores (CSV) para adicionar ou atualizar em lote no banco de dados.

Cálculo de Comissões de Vendas:

Implementada função para ler uma planilha de vendas e calcular as comissões que devem ser pagas para cada vendedor, conforme as regras especificadas.

Análises de Vendas por Canal e Estado:

Apresentado o volume de vendas (R$) e média por profissional para cada canal e por cada estado.
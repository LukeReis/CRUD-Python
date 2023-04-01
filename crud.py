import mysql.connector


# CREDENCIAIS DE ACESSO PARA INICAR A CONEXAO COM O BANCO DE DADOS
conexao = mysql.connector.connect(
    host='seu_host',
    user='usuario_do_seu_banco',
    password='senha_do_seu_banco',
    database='nome_do_seu_banco',
)

cursor = conexao.cursor()

# INPUTS PARA USUARIO
criar = input('Deseja acrescentar um novo produto? (s/SIM - n/NAO): ')
atualizar = input('Deseja atualizar um produto existente? (s/SIM - n/NAO): ')

if atualizar == 's':
    up_valor = input('Deseja atualizar o valor? (s/SIM - n/NAO): ')
    up_nome = input('Deseja atualizar o nome? (s/SIM - n/NAO): ')

apagar = input('Deseja apagar um produto do cadastro? (s/SIM - n/NAO): ')


# CRUD
# CADASTRAR NO BANCO
def create():
    produto = input('Qual o nome do produto a ser adicionado: ')
    preco = int(input('Qual o valor do produto: '))
    # ATENÇÃO AS ""
    comando = f'INSERT INTO produtos (nome_produto, valor_produto) VALUES ("{produto}", {preco})'
    cursor.execute(comando)
    conexao.commit()  # editar o banco de dados

# LER O BANCO
def read():
    comando = 'SELECT * FROM produtos'
    cursor.execute(comando)
    resultado = cursor.fetchall()  # ler o banco de dados
    print(resultado)

# ATUALIZAR VALOR DE PRODUTO CADASTRADO NO ABNCO
def update_valor():
    valor_atual = int(input('Informe o preço atual do produto: '))
    novo_valor = int(input('Informe o novo preço: '))
    comando = f'UPDATE produtos SET valor_produto = {novo_valor} WHERE valor_produto = "{valor_atual}"'
    cursor.execute(comando)
    conexao.commit()

# ATUALIZAR NOME DE PRODUTO CADASTRADO NO BANCO
def update_nome():
    nome_atual = input('Informe o nome atual do produto; ')
    novo_nome = input('Informe o novo nome do produto: ')
    comando = f'UPDATE produtos SET nome_produto = {novo_nome} WHERE nome_produto = "{nome_atual}"'
    cursor.execute(comando)
    conexao.commit()

# DELETAR UM PRODUTO CADASTRADO NO BANCO
def delete():
    nome_produto = input('Informe o nome do produto a ser deletado: ')
    comando = f'DELETE FROM produtos WHERE nome_produto = "{nome_produto}"'
    cursor.execute(comando)
    conexao.commit()


# CONDICIONAIS PARA CHAMAR AS FUNÇOES
if criar == 's':
     create()

if atualizar == 's' and up_valor == 's':
     update_valor()

if atualizar == 's' and up_nome == 's':
     update_nome()

if apagar == 's':
     delete()

# LER BANCO
read()

# FECHAR CONEXAO COM O BANCO
cursor.close()
conexao.close()

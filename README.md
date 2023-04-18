# CRUD-Python

Este é um código em Python que realiza operações de CRUD (Create, Read, Update e Delete) em um banco de dados MySQL. Ele utiliza a biblioteca PySimpleGUI para criar interfaces gráficas.

# Pré-requisitos
Antes de utilizar este script, certifique-se de ter o MySQL instalado em sua máquina e ter as credenciais de acesso ao banco de dados (host, usuário, senha e nome do banco de dados).

Crie uma tabela no seu banco de dados MySQL com o seguinte comando:


CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_produto VARCHAR(255),
    valor_produto INT
);


Para utilizar este script, basta ter o Python instalado em sua máquina. Também é necessário instalar o pacote mysql-connector-python, que pode ser instalado através do comando no seu terminal: "pip install mysql-connector-python"

# Utilização
Clone este repositório ou baixe o arquivo crud.py.
Instale as dependências necessárias, executando o comando pip install PySimpleGUI mysql-connector-python.
Configure as credenciais de acesso ao banco de dados. Para isso, edite as seguintes linhas no início do arquivo crud.py:
##
```
conexao = mysql.connector.connect(
    host='seu_host',
    user='usuario_do_seu_banco',
    password='senha_do_seu_banco',
    database='nome_do_seu_banco',
)
```
##
Substitua os valores entre as aspas pelos dados de acesso ao seu banco de dados.

Execute o arquivo crud.py e utilize as funcionalidades disponíveis:
Adicionar Produto: permite cadastrar um novo produto no banco de dados, informando o nome e o preço.
Atualizar Produto: permite atualizar o nome ou o preço de um produto já cadastrado no banco de dados, informando o ID do produto.
Deletar Produto: permite excluir um produto cadastrado no banco de dados, informando o ID do produto.
Ler Banco de Dados: exibe todos os produtos cadastrados no banco de dados.



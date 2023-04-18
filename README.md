# CRUD-Python

Este é um script em Python que permite gerenciar um banco de dados de produtos. Este programa permite ao usuário realizar as operações básicas de CRUD (criação, leitura, atualização e exclusão) em um banco de dados MySQL

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
Ao executar o script, será solicitado ao usuário que informe se deseja adicionar um novo produto, atualizar um produto existente ou excluir um produto do banco de dados. Dependendo da opção escolhida, o usuário será solicitado a informar as informações necessárias (nome, preço, novo nome, novo preço, etc.).

No arquivo Python, insira as suas credenciais de acesso ao banco de dados MySQL nas variáveis host, user, password e database.


Após as operações serem realizadas, o script exibirá todos os produtos cadastrados no banco de dados.

# Observações
O programa foi criado para fins educacionais e pode ser adaptado para atender a necessidades específicas.
Este programa não contempla questões de segurança como, por exemplo, validação de entrada de dados e prevenção de ataques SQL injection.

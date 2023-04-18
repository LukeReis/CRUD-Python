import mysql.connector
import PySimpleGUI as sg

# CREDENCIAIS DE ACESSO PARA INICAR A CONEXAO COM O BANCO DE DADOS
conexao = mysql.connector.connect(
    host='seu_host',
    user='usuario_do_seu_banco',
    password='senha_do_seu_banco',
    database='nome_do_seu_banco',
)

cursor = conexao.cursor()


sg.theme('Reddit')

def janela_inicial():
    layout = [
        [sg.Text('CRUD Python')],
        [sg.Button('Adicionar Produto'), sg.Button('Atualizar Produto'), sg.Button('Deletar Produto'), sg.Button('Ler Banco de Dados')]
    ]
    return sg.Window('CRUD', layout, finalize=True)

def janela_add_prod():
    layout = [
        [sg.Text('Informe o produto'), sg.Input(key='addProduto')],
        [sg.Text('Informe o preco'), sg.Input(key='addPreco')],
        [sg.Text('', key='aviso')],
        [sg.Button('ADICIONAR'), sg.Button('VOLTAR')]
    ]
    return sg.Window('CRUD Adicionar Produto', layout, finalize=True)

def janela_define_atualizar():
    layout = [
        [sg.Text('O que deseja atualizar no produto?')],
        [sg.Button('VALOR'), sg.Button('NOME'), sg.Button('VOLTAR')]
    ]
    return sg.Window('CRUD Adicionar Produto', layout, finalize=True)

def janela_atualiza_valor():
    layout = [
        [sg.Text('Informe o ID do produto'), sg.Input(key='idVenda')],
        [sg.Text('Informe o novo preço do produto'), sg.Input(key='novoPrecoProd')],
        [sg.Text('',key='aviso')],
        [sg.Button('ATUALIZAR VALOR'), sg.Button('VOLTAR')]
    ]
    return sg.Window('CRUD Atualiza Valor', layout, finalize=True)

def janela_atualiza_nome():
    layout = [
        [sg.Text('Informe o ID do produto'), sg.Input(key='idProd')],
        [sg.Text('Informe o novo nome do produto'), sg.Input(key='novoNomeProd')],
        [sg.Text('',key='aviso')],
        [sg.Button('ATUALIZAR NOME'), sg.Button('VOLTAR')]
    ]
    return sg.Window('CRUD Atualiza Nome', layout, finalize=True)

def janela_deletar():
    layout = [
        [sg.Text('Informe o ID do produto para deletar'), sg.Input(key='deleteProd')],
        [sg.Text('',key='aviso')],
        [sg.Button('DELETAR'), sg.Button('VOLTAR')]
    ]
    return sg.Window('CRUD Deletar', layout, finalize=True)

def leitura_banco():
    layout = [
        [sg.Text('',key='aviso')],
        [sg.Button('LER'), sg.Button('VOLTAR')]
    ]
    return sg.Window('Tela Leitura', layout, finalize=True)

# criar as janelas inciais
janela1, janela2, janela3 = janela_inicial(), None, None


while True:
    window, eventos, valores = sg.read_all_windows()

    def create():
        # produto = input('Qual o nome do produto a ser adicionado: ')
        # preco = int(input('Qual o valor do produto: '))
        produto = valores['addProduto']
        preco = valores['addPreco']
        comando = f'INSERT INTO produtos (nome_produto, valor_produto) VALUES ("{produto}", {preco})' # ATENÇÃO AS ""
        cursor.execute(comando)
        conexao.commit()  # editar o banco de dados

    # LER O BANCO
    def read():
        comando = 'SELECT * FROM produtos'
        cursor.execute(comando)
        resultado = cursor.fetchall()  # ler o banco de dados
        return resultado

# ATUALIZAR VALOR DE PRODUTO CADASTRADO NO ABNCO
    def update_valor():
        IdVendas = valores['idVenda']
        novo_valor = valores['novoPrecoProd']
        comando = f'UPDATE produtos SET valor_produto = {novo_valor} WHERE idVendas = "{IdVendas}"'
        cursor.execute(comando)
        conexao.commit()

# ATUALIZAR NOME DE PRODUTO CADASTRADO NO BANCO
    def update_nome():
        IdVendas = valores['idProd']
        novo_nome = valores['novoNomeProd']
        comando = f'UPDATE produtos SET nome_produto = {novo_nome} WHERE idVendas = "{IdVendas}"'
        cursor.execute(comando)
        conexao.commit()

# DELETAR UM PRODUTO CADASTRADO NO BANCO
    def delete():
        IdVendas = valores['deleteProd']
        comando = f'DELETE FROM produtos WHERE idVendas = "{IdVendas}"'
        cursor.execute(comando)
        conexao.commit()

    # quando a janela for fechada
    if window == janela1 and eventos == sg.WIN_CLOSED:
        break

    # ADICIONAR PRODUTO
    if window == janela1 and eventos == 'Adicionar Produto':
        janela1.hide()
        janela2 = janela_add_prod()
    if window == janela2 and eventos == 'ADICIONAR':
        create()
        janela2['aviso'].Update('Produto Cadastrado!!')

    # ATUALIZAR PRODUTO
    elif window == janela1 and eventos == 'Atualizar Produto':
        janela1.hide()
        janela2 = janela_define_atualizar()
    if window == janela2 and eventos == 'VOLTAR':
        janela2.hide()
        janela1.un_hide()
    if window == janela2 and eventos == 'VALOR':
        janela2.hide()
        janela3 = janela_atualiza_valor()
    if window == janela3 and eventos == 'VOLTAR':
        janela3.hide()
        janela2.un_hide()
    if window == janela3 and eventos == 'ATUALIZAR VALOR':
        update_valor()
        janela3['aviso'].Update('Valor Atualizado!!')
    if window == janela2 and eventos == 'NOME':
        janela1.hide()
        janela3 = janela_atualiza_nome()
    if window == janela3 and eventos == 'ATUALIZAR NOME':
        update_nome()
        janela3['aviso'].UPdate('Nome Atualizado!!')
            
    # DELETAR PRODUTO
    elif window == janela1 and eventos == 'Deletar Produto':
        janela1.hide()
        janela2 = janela_deletar()
    if window == janela2 and eventos == 'DELETAR':
        delete()
        janela2['aviso'].Update('Produto Deletado!!')
        
    # LEITURA DO BANCO
    if window == janela1 and eventos == 'Ler Banco de Dados':
        janela1.hide()
        janela2 = leitura_banco()
    if window == janela2 and eventos == 'VOLTAR':
        janela2.hide()
        janela1.un_hide()
    if window ==  janela2 and eventos == 'LER':
        dados = read()
        janela2['aviso'].Update(f'Dados do banco: {dados}')

# FECHAR CONEXAO COM O BANCO
cursor.close()
conexao.close()
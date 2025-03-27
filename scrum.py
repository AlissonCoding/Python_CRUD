import json

class Produto:
    def __init__(self, codigo, nome, preco, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f'{self.codigo} | {self.nome} | R${self.preco:.2f} | {self.quantidade}'

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "preco": self.preco,
            "quantidade": self.quantidade
        }

produtos = {}

ARQUIVO_JSON = "dadosprodutos.json"

def salvar_produtos():
    with open(ARQUIVO_JSON, "a", encoding="utf-8") as arquivo:
        json.dump({codigo: prod.to_dict() for codigo, prod in produtos.items()}, arquivo, ensure_ascii=False, indent=4)

def carregar_produtos():
    global produtos
    try:
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            produtos = {codigo: Produto(**prod) for codigo, prod in dados.items()}
    except FileNotFoundError:
        produtos = {}

def cadastrar_produto():
    codigo = input('Código do produto: ')
    if codigo in produtos:
        print('Produto já cadastrado!')
        return
    
    nome = input('Nome do produto: ')

    for produto in produtos.values():
        if produto.nome.lower() == nome.lower():
            print('Já existe um produto cadastrado com esse nome!')
            return
    
    preco = float(input('Preço do produto: '))
    quantidade = int(input('Quantos produtos: '))
    
    produtos[codigo] = Produto(codigo, nome, preco, quantidade)

    salvar_produtos()
    
    print('Produto cadastrado com sucesso!')

def alterar_produto():
    codigo = input('Código do produto: ')
    if codigo not in produtos:
        print('Produto não encontrado!')
        return
    
    produto = produtos[codigo]
    
    produto.nome = input('Nome do produto: ')
    produto.preco = float(input('Preço do produto: '))
    produto.quantidade = int(input('Quantos produtos: '))

    salvar_produtos()
    print('Produto alterado com sucesso!')

def remover_produto():
    if produtos == {}:
        print('Não existem produtos cadastrados, não é possível fazer remoção')

    codigo = input('Código do produto: ')
    if codigo in produtos:
        del produtos[codigo]

        salvar_produtos()

        print('O produto foi removido com sucesso!')
    else:
        print('Produto não encontrado!')
    
def listar_produto():
    if not produtos:
        print('Nenhum produto cadastrado!')
        return
    print('Código | Nome | Preço | Quantidade')
    
    total_produtos = 0
    
    for produto in produtos.values():
        print(produto)
        total_produtos += produto.quantidade

    print(f"Total de itens: {total_produtos}")

def menu_principal():
    while True: 
        print('1. Cadastrar produto')
        print('2. Alterar produto')
        print('3. Remover produto')
        print('4. Listar produto')
        print('5. Sair')

        acao = input('O que você gostaria de fazer: ')

        if acao == '1':
            cadastrar_produto()
        elif acao == '2':
            alterar_produto()
        elif acao == '3':
            remover_produto()
        elif acao == '4':
            listar_produto()
        elif acao == '5':
            print('Fechando o aplicativo...')
            break
        else:
            print('Essa opção não existe!')

menu_principal()

print('Teste')
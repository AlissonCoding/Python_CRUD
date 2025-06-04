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

PRODUTOS_RECOMENDADOS = [
    {"codigo": "TEC001", "produto": "Monitor Ultrawide 34 360hz", "preco": "R$ 2900"},
    {"codigo": "TEC002", "produto": "Teclado Mecânico RGB", "preco": "R$ 270"},
    {"codigo": "TEC003", "produto": "Mouse Gamer Sem Fio", "preco": "R$ 440"},
    {"codigo": "TEC004", "produto": "Headset Gamer 7.1", "preco": "R$ 400"},
    {"codigo": "TEC005", "produto": "SSD NVMe 1TB", "preco": "R$ 320"},
    {"codigo": "TEC006", "produto": "Placa de Vídeo RTX 4090", "preco": "R$ 23000"},
    {"codigo": "TEC007", "produto": "Notebook Gamer AMD Radeon 9", "preco": "R$ 9500"},
    {"codigo": "TEC008", "produto": "Apple Watch", "preco": "R$ 5900"},
    {"codigo": "TEC009", "produto": "Cadeira Gamer Ergonômica", "preco": "R$ 900"},
    {"codigo": "TEC010", "produto": "Roteador Wi-Fi 6E", "preco": "R$ 500"}
]

ARQUIVO_JSON = "dadosprodutos.json"

def salvar_produtos():
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as arquivo:
        json.dump({codigo: prod.to_dict() for codigo, prod in produtos.items()}, arquivo, ensure_ascii=False, indent=4)

def carregar_produtos():
    global produtos
    try:
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            produtos_carregados_nesta_sessao = {}
            
            for codigo, item_valor in dados.items():
                produtos_carregados_nesta_sessao[codigo] = Produto(**item_valor)
            
            produtos = produtos_carregados_nesta_sessao 

    except FileNotFoundError:
        produtos = {}
    except json.JSONDecodeError:
        print(f"Aviso: Erro ao decodificar o arquivo JSON ({ARQUIVO_JSON}). Pode estar corrompido ou vazio. Iniciando com lista de produtos vazia.")
        produtos = {}
    except (AttributeError, TypeError) as e:
        print(f"Aviso: Estrutura de dados inesperada no arquivo JSON ({e}). Iniciando com lista de produtos vazia.")
        produtos = {}
    except Exception as e:
        print(f"Erro inesperado ao carregar produtos: {e}. Iniciando com lista de produtos vazia.")
        produtos = {}

def recomendar_produtos():
    if not produtos:
        print("Existem essas opções no estoque, o que você deseja?")
        print("-" * 70) 
        print("Código   | Produto                        | Preço")
        print("-" * 70)
        
        for r in PRODUTOS_RECOMENDADOS:
            print(f"{r['codigo']:<8} | {r['produto']:<30} | {r['preco']:<8}")
        
        print("-" * 70)
        print("\nPara cadastrar um desses ou qualquer outro produto, escolha a opção 'Cadastrar produto' no menu.")
    else:
        print("Já temos produtos cadastrados! Dê uma olhada na lista usando a opção 'Listar produto'.")

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
    if produtos == {}:
        print("Não existem produtos cadastrados. Portanto não há o que alterar.")
        return
    
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
        print('1. Recomendar produto')
        print('2. Cadastrar produto')
        print('3. Alterar produto')
        print('4. Remover produto')
        print('5. Listar produto')
        print('6. Sair')

        acao = input('O que você gostaria de fazer: ')
        if acao == '1':
            recomendar_produtos()
        elif acao == '2':
            cadastrar_produto()
        elif acao == '3':
            alterar_produto()
        elif acao == '4':
            remover_produto()
        elif acao == '5':
            listar_produto()
        elif acao == '6':
            print('Fechando o aplicativo...')
            break
        else:
            print('Essa opção não existe!')

if __name__ == "__main__":
    carregar_produtos()
    menu_principal()


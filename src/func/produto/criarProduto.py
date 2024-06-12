from src.model.produto import Produto

def criarProduto():
    nome = str(input("Digite o nome do produto: "))
    descricao = str(input("Digite a descrição do produto: "))
    preco = str(input("Digite o preço do produto: "))
    estoque = str(input("Digite a quantidade em estoque do produto: "))
    produto = Produto(nome, descricao, preco, estoque)
    return produto
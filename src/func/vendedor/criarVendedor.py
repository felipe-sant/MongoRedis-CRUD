from src.model.vendedor import Vendedor

def criarVendedor(id):
    nome = str(input("Digite o nome do vendedor: "))
    rg = str(input("Digite o RG do vendedor: "))
    produtos = []
    vendedor = Vendedor(id, nome, rg)
    return vendedor
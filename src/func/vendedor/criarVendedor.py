from src.model.vendedor import Vendedor
from src.menu.crudProdutos import crudProdutos

def criarVendedor(id):
    nome = str(input("Digite o nome do vendedor: "))
    rg = str(input("Digite o RG do vendedor: "))
    vendedor = Vendedor(id, nome, rg)
    return vendedor
from src.func.criarChave import criarChave
from src.func.verificarChaveExistente import verificarChaveExistente
from src.func.vendedor.criarVendedor import criarVendedor
from src.func.vendedor.sincronizacao.adicionarVendedorAoRedis import adicionarVendedorAoRedis
from src.menu.menuVendedorProduto import menuVendedorProduto

def cadastrarVendedor():
    id = criarChave("vendedor")
    if verificarChaveExistente("vendedor", id):
        print("\nErro: chave já existente")
        input()
        return
    vendedor = criarVendedor(id)
    opcao = str(input("Deseja adicionar alguns produtos? (s/n) "))
    if opcao == "s":
        menuVendedorProduto(vendedor)
    adicionarVendedorAoRedis(vendedor)
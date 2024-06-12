from src.func.vendedor.sincronizacao.pegarTodosVendedoresDoRedis import pegarTodosVendedoresDoRedis
from src.func.vendedor.sincronizacao.adicionarVendedorAoMongo import adicionarVendedorAoMongo
from src.func.vendedor.sincronizacao.deletarTodosVendedoresRedis import deletarTodosVendedoresRedis
from src.func.vendedor.sincronizacao.pegarTodosVendedoresDoMongo import pegarTodosVendedoresDoMongo
from src.func.vendedor.produtos.atualizarProdutos import atualizarProdutos

def moverVendedoresParaMongo():
    vendedorRedis = pegarTodosVendedoresDoRedis()
    for vendedor in vendedorRedis:
        try:
            adicionarVendedorAoMongo(vendedor)
            print(f"Vendedor {vendedor.nome} adicionado com sucesso")
        except:
            print(f"Erro ao adicionar vendedor {vendedor.nome}")
    vendedorMongo = pegarTodosVendedoresDoMongo()
    for vendedor in vendedorMongo:
        try:
            atualizarProdutos(vendedor)
        except Exception as e:
            print(f"Erro ao atualizar produtos do vendedor {vendedor.nome}")
            print(e)
            input()
            
    deletarTodosVendedoresRedis()
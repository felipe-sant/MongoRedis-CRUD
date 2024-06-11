from src.func.vendedor.sincronizacao.pegarTodosVendedoresDoRedis import pegarTodosVendedoresDoRedis
from src.func.vendedor.sincronizacao.adicionarVendedorAoMongo import adicionarVendedorAoMongo
from src.func.vendedor.sincronizacao.deletarTodosVendedoresRedis import deletarTodosVendedoresRedis

def moverVendedoresParaMongo():
    vendedorRedis = pegarTodosVendedoresDoRedis()
    for vendedor in vendedorRedis:
        try:
            adicionarVendedorAoMongo(vendedor)
            print(f"Vendedor {vendedor.nome} adicionado com sucesso")
        except:
            print(f"Erro ao adicionar vendedor {vendedor.nome}")
    deletarTodosVendedoresRedis()
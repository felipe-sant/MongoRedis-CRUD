from src.func.buscarDados import BuscarDados
from src.utils.jsonParaVendedor import jsonParaVendedor

def pegarTodosVendedoresDoRedis():
    dados = BuscarDados("vendedor")
    listaDeVendedores = []
    for vendedor in dados:
        listaDeVendedores.append(jsonParaVendedor(vendedor))
    return listaDeVendedores
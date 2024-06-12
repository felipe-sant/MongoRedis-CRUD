from src.data.mongo.func.buscar import buscarMongo
from src.utils.jsonParaVendedor import jsonParaVendedor

def pegarTodosVendedoresDoMongo():
    try:
        dados = buscarMongo("vendedor")
        listaDeVendedores = []
        for vendedor in dados:
            listaDeVendedores.append(jsonParaVendedor(vendedor))
    except:
        listaDeVendedores = None
    return listaDeVendedores
from src.data.mongo.func.buscar import buscarMongo
from src.utils.jsonParaCompra import jsonParaCompra

def buscarTodasComprasDoMongo():
    dados = buscarMongo("compra")
    listaDeCompras = []
    for compra in dados:
        listaDeCompras.append(jsonParaCompra(compra))
    return listaDeCompras
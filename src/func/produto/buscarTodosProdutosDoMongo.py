from src.data.mongo.func.buscar import buscarMongo
from src.utils.jsonParaProduto import JsonParaProduto

def buscarTodosProdutosDoMongo():
    try:
        dados = buscarMongo("produto")
        listaDeProdutos = []
        for produto in dados:
            listaDeProdutos.append(JsonParaProduto(produto))
    except:
        listaDeProdutos = None
    return listaDeProdutos
            
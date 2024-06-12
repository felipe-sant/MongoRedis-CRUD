from src.data.mongo.func.buscar import buscarMongo

def verificarIdExistente(colecao, id):
    dado = buscarMongo(colecao, {"_id": id})
    if dado is None:
        return False
    return True
    
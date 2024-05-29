from src.data.mongo.func.buscar import buscarMongo
from bson.objectid import ObjectId

def verificarIdExistente(colecao, id):
    dado = buscarMongo(colecao, {"_id": ObjectId(id)})
    if dado is None:
        return False
    return True
    
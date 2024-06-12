from src.func.verificarIdExistente import verificarIdExistente
from src.data.mongo.func.deletar import deletarMongo
from bson.objectid import ObjectId

def deletarCompra():
    id = input("Digite o id da compra: ")
    try:
        objectId = ObjectId(id)
    except:
        print("\nId inválido")
        input()
        return
    if not verificarIdExistente("compra", objectId):
        print("\nCompra não encontrada")
        input()
        return
    
    deletarMongo("compra", {"_id": objectId})
    print("\nCompra deletada com sucesso!")
    input()
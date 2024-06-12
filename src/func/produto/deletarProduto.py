from bson.objectid import ObjectId
from src.func.verificarIdExistente import verificarIdExistente
from src.data.mongo.func.deletar import deletarMongo

def deletarProduto():
    id = input("Digite o id do produto: ")
    try:
        objectId = ObjectId(id)
    except:
        print("\nId inválido")
        input()
        return
    if not verificarIdExistente("produto", objectId):
        print("\nProduto não encontrado")
        input()
        return
        
    deletarMongo("produto", {"_id": objectId})
    print("\nProduto deletado com sucesso!")
    input()
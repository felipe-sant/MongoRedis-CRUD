from bson.objectid import ObjectId
from src.func.verificarIdExistente import verificarIdExistente
from src.data.mongo.func.buscar import buscarMongo

def setarUsuario(compra):
    id = str(input("Digite o id do usuário: "))
    try:
        objectId = ObjectId(id)
    except:
        print("Id inválido")
        input()
        return None
    if verificarIdExistente("usuario", objectId):
        usuario = buscarMongo("usuario", {"_id": objectId})[0]
        if usuario is None:
            print("Usuário não encontrado")
            input()
            return None
        else:
            compra.setUsuario(usuario)
            return "Usuário setado com sucesso"
    else:
        print("Usuário não encontrado")
        input()
        return None
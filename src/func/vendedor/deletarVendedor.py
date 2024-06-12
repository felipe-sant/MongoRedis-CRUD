from src.func.criarChave import criarChave
from src.func.verificarChaveExistente import verificarChaveExistente
from src.data.redis.func.delete import delete
from bson.objectid import ObjectId
from src.func.verificarIdExistente import verificarIdExistente
from src.data.mongo.func.deletar import deletarMongo

def deletarVendedor():
    id = input("Digite o id do vendedor: ")
    try:
        chave = criarChave("vendedor", id)
        if (verificarChaveExistente("vendedor", chave)):
            delete(chave)
            print("\nVendedor deletado com sucesso!")
            input()
            return
        else:
            raise
    except:
        try:
            id = ObjectId(id)
            if (verificarIdExistente("vendedor", id)):
                deletarMongo("vendedor", {"_id": id})
                print("\nVendedor deletado com sucesso!")
                input()
                return
            else:
                raise
        except:
            pass
    print("\nVendedor não encontrado")
    input()
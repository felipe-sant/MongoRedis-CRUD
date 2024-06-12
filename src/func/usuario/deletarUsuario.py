from src.func.verificarChaveExistente import verificarChaveExistente
from src.data.redis.func.delete import delete
from src.func.criarChave import criarChave
from bson.objectid import ObjectId
from src.func.verificarIdExistente import verificarIdExistente
from src.data.mongo.func.deletar import deletarMongo

def deletarUsuario():
    id = input("Digite o id do usuário: ")
    try:
        chave = criarChave("usuario", id)
        if (verificarChaveExistente("usuario", chave)):
            delete(chave)
            print("\nUsuário deletado com sucesso!")
            input()
            return
        else:
            raise
    except:
        try:
            id = ObjectId(id)
            if (verificarIdExistente("usuario", id)):
                deletarMongo("usuario", {"_id": id})
                print("\nUsuário deletado com sucesso!")
                input()
                return
            else:
                raise
        except:
            pass
    print("\nUsuário não encontrado")
    input()

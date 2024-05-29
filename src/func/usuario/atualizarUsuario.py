from src.func.criarChave import criarChave
from src.func.verificarChaveExistente import verificarChaveExistente
from bson.objectid import ObjectId
from src.func.verificarIdExistente import verificarIdExistente
from src.func.usuario.criarUsuario import criarUsuario
from src.func.usuario.atualizarUsuarioNoRedis import atualizarUsuarioNoRedis
from src.data.redis.func.get import get
from src.utils.jsonParaUsuario import jsonParaUsuario

def atualizarUsuario():
    id = input("Digite o id do usuário: ")
    try:
        chave = criarChave("usuario", id)
        if (verificarChaveExistente("usuario", chave)):
            usuario = jsonParaUsuario(get(chave))
            usuarioNovo = criarUsuario(chave)
            atualizarUsuarioNoRedis(chave, usuario, usuarioNovo)
            print("\nUsuário atualizado com sucesso!")
            input()
            return
        else:
            raise
    except:
        try:
            id = ObjectId(id)
            if (verificarIdExistente("usuario", id)):
                print("usuario existente no mongo")
                input()
                return
            else:
                raise
        except:
            pass
    print("\nUsuário não encontrado")
    input()
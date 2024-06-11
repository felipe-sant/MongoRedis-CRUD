
from src.func.usuario.sincronizacao.moverUsuariosParaMongo import moverUsuariosParaMongo
from src.func.criarChave import criarChave
from bson.objectid import ObjectId
from src.func.verificarChaveExistente import verificarChaveExistente
from src.func.verificarIdExistente import verificarIdExistente
from src.func.usuario.sincronizacao.pegarTodosUsuariosDoMongo import pegarTodosUsuariosDoMongo
from src.func.usuario.sincronizacao.pegarTodosUsuariosDoRedis import pegarTodosUsuariosDoRedis

def listarUsuario():
    id = input("Digite o id do usuário (deixe em branco para listar todos): ")
    if (id == ""):
        moverUsuariosParaMongo()
        listaDeUsuarios = pegarTodosUsuariosDoMongo()
        print()
        for i in range(len(listaDeUsuarios)):
            print(f"- ({i+1}/{len(listaDeUsuarios)}) -")
            listaDeUsuarios[i].mostrar()
            input()
        return
    else:
        try:
            chave = criarChave("usuario", id)
            if (verificarChaveExistente("usuario", chave)):
                listaDeUsuarios = pegarTodosUsuariosDoRedis()
                for usuario in listaDeUsuarios:
                    if usuario.id == chave:
                        usuario.mostrar()
                        input()
                return
            else:
                raise
        except:
            try:
                id = ObjectId(id)
                print()
                if (verificarIdExistente("usuario", id)):
                    listaDeUsuarios = pegarTodosUsuariosDoMongo()
                    for usuario in listaDeUsuarios:
                        if usuario.id == id:
                            usuario.mostrar()
                            input()
                    return
                else:
                    raise
            except:
                pass
        print("Usuário não encontrado!")
        input()
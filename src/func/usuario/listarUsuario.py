from src.func.usuario.pegarTodosUsuariosDoMongo import pegarTodosUsuariosDoMongo
from src.func.usuario.sincronizacao.moverUsuariosParaMongo import moverUsuariosParaMongo
from src.func.criarChave import criarChave
from src.func.usuario.pegarTodosUsuariosDoRedis import pegarTodosUsuariosDoRedis
from bson.objectid import ObjectId

def listarUsuario():
    id = input("Digite o id do usuário (deixe em branco para listar todos): ")
    print()  
    if (id == ""):
        moverUsuariosParaMongo()
        listaDeUsuarios = pegarTodosUsuariosDoMongo()
        for i in range(len(listaDeUsuarios)):
            print(f"- ({i+1}/{len(listaDeUsuarios)}) -")
            listaDeUsuarios[i].mostrar()
            input()
        return
    else:
        try:
            listaDeUsuarios = pegarTodosUsuariosDoRedis()
            for usuario in listaDeUsuarios:
                if usuario.id == criarChave("usuario", id):
                    usuario.mostrar()
                    input()
                    return
        except:
            try:
                listaDeUsuarios = pegarTodosUsuariosDoMongo()
                for usuario in listaDeUsuarios:
                    if usuario.id == ObjectId(id):
                        usuario.mostrar()
                        input()
                        return
            except:
                pass
        print("Usuário não encontrado!")
        input()
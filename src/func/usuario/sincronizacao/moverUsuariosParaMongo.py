from src.func.usuario.sincronizacao.pegarTodosUsuariosDoRedis import pegarTodosUsuariosDoRedis
from src.func.usuario.sincronizacao.adicionarUsuarioAoMongo import adicionarUsuarioAoMongo
from src.func.usuario.sincronizacao.deletarTodosUsuariosRedis import deletarTodosUsuariosRedis

def moverUsuariosParaMongo():
    usuariosRedis = pegarTodosUsuariosDoRedis()
    for usuario in usuariosRedis:
        try:
            adicionarUsuarioAoMongo(usuario)
            print(f"Usuário {usuario.nome} adicionado com sucesso")
        except:
            print(f"Erro ao adicionar usuário {usuario.nome}")
    deletarTodosUsuariosRedis()
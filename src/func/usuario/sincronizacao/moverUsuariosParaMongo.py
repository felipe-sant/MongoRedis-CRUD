from src.func.usuario.pegarTodosUsuariosDoRedis import pegarTodosUsuariosDoRedis
from src.func.usuario.adicionarUsuarioAoMongo import adicionarUsuarioAoMongo
from src.func.usuario.deletarTodosUsuariosRedis import deletarTodosUsuariosRedis

def moverUsuariosParaMongo():
    usuariosRedis = pegarTodosUsuariosDoRedis()
    for usuario in usuariosRedis:
        adicionarUsuarioAoMongo(usuario)
    deletarTodosUsuariosRedis()
from src.model.usuario import Usuario
from src.func.criarChave import criarChave
from src.func.verificarChaveExistente import verificarChaveExistente
from src.func.usuario.adicionarUsuarioAoRedis import adicionarUsuarioAoRedis
from src.func.usuario.adicionarUsuarioAoMongo import adicionarUsuarioAoMongo
from src.func.usuario.criarUsuario import criarUsuario

def cadastrarUsuario():
    id = criarChave("usuario")
    if verificarChaveExistente("usuario", id):
        print("\nErro: chave já existente")
        input()
        return
    usuario = criarUsuario(id)
    adicionarUsuarioAoRedis(usuario)
from src.func.criarChave import criarChave
from src.func.verificarChaveExistente import verificarChaveExistente
from src.func.usuario.criarUsuario import criarUsuario
from src.func.usuario.sincronizacao.adicionarUsuarioAoRedis import adicionarUsuarioAoRedis

def cadastrarUsuario():
    id = criarChave("usuario")
    if verificarChaveExistente("usuario", id):
        print("\nErro: chave já existente")
        input()
        return
    usuario = criarUsuario(id)
    adicionarUsuarioAoRedis(usuario)
from src.model.usuario import Usuario
from src.func.criarChave import criarChave
from src.func.verificarChaveExistente import verificarChaveExistente
from src.func.usuario.adicionarUsuarioAoRedis import adicionarUsuarioAoRedis
from src.func.usuario.adicionarUsuarioAoMongo import adicionarUsuarioAoMongo

def cadastrarUsuario():
    id = criarChave("usuario")
    if verificarChaveExistente("usuario", id):
        print("\nErro: chave já existente")
        input()
        return
    nome = str(input("Digite o nome do usuário: "))
    endereco = str(input("Digite o endereço do usuário: "))
    rg = str(input("Digite o RG do usuário: "))
    
    usuario = Usuario(id, nome, endereco, rg)
    adicionarUsuarioAoRedis(usuario)
from src.model.usuario import Usuario
from src.data.mongo.func.atualizar import atualizar

def criarUsuario(usuario = None):
    if (usuario == None):
        nome = str(input("Digite o nome do usuário: "))
        endereco = str(input("Digite o endereço do usuário: "))
        rg = str(input("Digite o RG do usuário: "))
        usuario = Usuario(nome, endereco, rg)
    else:
        usuarioNovo = criarUsuario()
        usuario.atualizar(usuarioNovo)
    return usuario
from src.model.usuario import Usuario

def criarUsuario(id):
    nome = str(input("Digite o nome do usuário: "))
    endereco = str(input("Digite o endereço do usuário: "))
    rg = str(input("Digite o RG do usuário: "))
    usuario = Usuario(id, nome, endereco, rg)
    return usuario
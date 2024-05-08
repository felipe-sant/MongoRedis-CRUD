from src.model.usuario import Usuario

def criarUsuario():
    nome = str(input("Digite o nome do usuário: "))
    endereco = str(input("Digite o endereço do usuário: "))
    rg = str(input("Digite o RG do usuário: "))
    usuario = Usuario(nome, endereco, rg)
    return usuario
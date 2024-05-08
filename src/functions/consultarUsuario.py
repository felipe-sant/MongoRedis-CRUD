from src.functions.criar.criarChave import criarChave
from src.functions.buscarDados import BuscarDados
from src.functions.listar.listarUsuarios import listarUsuarios

def consultarUsuario():
    chave = str(input("Digite a chave do usuario (deixe vazio para listar todos): "))
    print()
    if chave == "":
        usuarios = BuscarDados("usuario")
        listarUsuarios(usuarios)
    else:
        chave = criarChave("usuario", chave)
        print(f"buscando usuario com a chave: {chave}")
from src.func.buscarDados import BuscarDados
from src.func.usuario.listarUsuarios import listarUsuarios
from src.func.criarChave import criarChave

def consultarUsuario():
    chave = str(input("Digite a chave do usuário (deixe vazio para listar todos): "))
    try:
        print()
        if chave == "":
            usuarios = BuscarDados("usuario")
            listarUsuarios(usuarios)
        else:
            chave = criarChave("usuario", chave)
            print(f"buscando usuario com a chave: {chave}") # FAZER A FUNCAO DE BUSCAR COM UMA CHAVE ESPECIFICA
    except Exception as e:
        print(f"\nErro ao buscar usuário: {e}")
        input()
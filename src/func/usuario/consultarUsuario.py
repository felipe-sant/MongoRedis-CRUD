from src.func.buscarDados import BuscarDados
from src.func.usuario.listarUsuarios import listarUsuarios

def consultarUsuario():
    nome = str(input("Digite o nome do usuário (deixe vazio para listar todos): "))
    try:
        print()
        if nome == "":
            usuarios = BuscarDados("usuario")
            if usuarios == []:
                print("Nenhum usuário encontrado")
                input()
                return
            listarUsuarios(usuarios)
        else:
            usuarios = BuscarDados("usuario")
            usuarios = [usuario for usuario in usuarios if usuario["nome"] == nome]
            if usuarios == []:
                print("Usuário não encontrado")
                input()
                return
            listarUsuarios(usuarios)
    except Exception as e:
        print(f"\nErro ao buscar usuário: {e}")
        input()
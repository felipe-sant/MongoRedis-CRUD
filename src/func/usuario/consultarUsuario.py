from src.func.buscarDados import BuscarDados
from src.func.usuario.listarUsuarios import listarUsuarios
from src.func.criarChave import criarChave
from src.data.redis.func.get import get
from src.func.verificarChaveExistente import verificarChaveExistente

def consultarUsuario():
    nome = str(input("Digite o nome do usuário (deixe vazio para listar todos): "))
    try:
        print()
        if nome == "":
            usuarios = BuscarDados("usuario")
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
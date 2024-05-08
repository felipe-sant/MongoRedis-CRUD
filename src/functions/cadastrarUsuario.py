from src.functions.criar.criarUsuario import criarUsuario
from src.functions.criar.criarChave import criarChave
from src.data.redis.func.set import set
from src.functions.usuarioParaJson import usuarioParaJson

def cadastrarUsuario():
    try:
        chave = criarChave("usuario")
        usuario = criarUsuario()
        set(chave, usuarioParaJson(usuario, chave))
        print("\nUsuário cadastrado com sucesso!")
        input()
    except Exception as e:
        print(f"\nErro ao cadastrar usuário: {e}")
    
from src.func.criarChave import criarChave
from src.data.redis.func.set import set
from src.utils.usuarioParaJson import usuarioParaJson
from src.func.usuario.criarUsuario import criarUsuario

def cadastrarUsuario():
    try:
        chave = criarChave("usuario")
        usuario = criarUsuario()
        set(chave, usuarioParaJson(usuario, chave))
        print("\nUsuário cadastrado com sucesso!")
        input()
    except Exception as e:
        print(f"\nErro ao cadastrar usuário: {e}")
    
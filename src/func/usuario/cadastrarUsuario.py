from src.func.criarChave import criarChave
from src.data.redis.func.set import set
from src.utils.usuarioParaJson import usuarioParaJson
from src.func.usuario.criarUsuario import criarUsuario
from src.func.verificarChaveExistente import verificarChaveExistente

def cadastrarUsuario():
    chave = criarChave("usuario")
    if (verificarChaveExistente("usuario", chave)):
        print("\nUsuário já cadastrado!")
        input()
        return
    usuario = criarUsuario()
    try:
        set(chave, usuarioParaJson(usuario, chave))
        print("\nUsuário cadastrado com sucesso!")
        input()
    except Exception as e:
        print(f"\nErro ao cadastrar usuário: {e}")
        input()
    
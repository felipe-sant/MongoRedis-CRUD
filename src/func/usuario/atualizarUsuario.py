from src.func.criarChave import criarChave
from src.func.verificarChaveExistente import verificarChaveExistente
from src.data.redis.func.get import get
from src.data.redis.func.set import set
from src.func.usuario.criarUsuario import criarUsuario
from src.utils.jsonParaUsuario import jsonParaUsuario
from src.utils.usuarioParaJson import usuarioParaJson

def atualizarUsuario():
    chaveParaAtualizar = criarChave("usuario")
    try:
        if (verificarChaveExistente("usuario", chaveParaAtualizar)):
            usuarioJson = get(chaveParaAtualizar)
            usuario = jsonParaUsuario(usuarioJson)
            novoUsuario = criarUsuario(usuario)
            novoUsuarioJson = usuarioParaJson(novoUsuario, chaveParaAtualizar)
            set(chaveParaAtualizar, novoUsuarioJson)
            print("\nUsuário atualizado com sucesso!")
            input()
        else:
            raise Exception("Chave não encontrada!")
    except Exception as e:
        print(f"\nErro ao atualizar usuário: {e}")
        input()
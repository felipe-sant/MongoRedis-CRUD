from src.model.usuario import Usuario
from src.utils.usuarioParaJson import usuarioParaJson
from src.data.redis.func.set import set

def atualizarUsuarioNoRedis(id, usuario: Usuario, usuarioNovo: Usuario):
    usuario.atualizar(usuarioNovo)
    usuarioJson = usuarioParaJson(usuario)
    try:
        set(id, usuarioJson)
        return "Usuário atualizado com sucesso!"
    except Exception as e:
        return f"Erro: {e}"
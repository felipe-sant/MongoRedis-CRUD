from src.model.usuario import Usuario
from src.utils.usuarioParaJson import usuarioParaJson
from src.data.redis.func.set import set

def adicionarUsuarioAoRedis(usuario: Usuario):
    usuarioJson = usuarioParaJson(usuario)
    try:
        set(usuario.id, usuarioJson)
        return "Usuário cadastrado com sucesso!"
    except Exception as e:
        return f"Erro: {e}"
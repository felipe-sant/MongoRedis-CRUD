from src.model.usuario import Usuario
from src.utils.usuarioParaJson import usuarioParaJson
from src.data.mongo.func.atualizar import atualizarMongo

def atualizarUsuarioNoMongo(id, usuario: Usuario, usuarioNovo: Usuario):
    usuarioNovo.id = ""
    usuario.atualizar(usuarioNovo)
    usuarioJson = usuarioParaJson(usuario, False)
    try:
        atualizarMongo("usuario", usuarioJson, {"_id": id})
        return "Usuário atualizado com sucesso!"
    except Exception as e:
        return f"Erro: {e}"
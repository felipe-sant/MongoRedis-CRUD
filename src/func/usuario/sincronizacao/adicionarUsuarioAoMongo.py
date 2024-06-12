from src.data.mongo.func.criar import criarMongo
from src.utils.usuarioParaJson import usuarioParaJson
from src.model.usuario import Usuario

def adicionarUsuarioAoMongo(usuario: Usuario):
    usuarioJson = usuarioParaJson(usuario, False)
    criarMongo("usuario", usuarioJson)
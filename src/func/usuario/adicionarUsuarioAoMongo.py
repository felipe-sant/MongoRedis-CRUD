from src.data.mongo.func.criar import criarMongo
from src.utils.usuarioParaJson import usuarioParaJson
from src.model.usuario import Usuario

def adicionarUsuarioAoMongo(usuarioJson: Usuario):
    usuario = usuarioParaJson(usuarioJson, False)
    criarMongo("usuario", usuario)
from src.model.usuario import Usuario

def jsonParaUsuario(usuarioJson):
    usuario = Usuario(usuarioJson["nome"], usuarioJson["endereco"], usuarioJson["rg"])
    return usuario
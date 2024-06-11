from src.data.mongo.func.buscar import buscarMongo
from src.utils.jsonParaUsuario import jsonParaUsuario

def pegarTodosUsuariosDoMongo():
    try:
        dados = buscarMongo("usuario")
        listaDeUsuarios = []
        for usuario in dados:
            listaDeUsuarios.append(jsonParaUsuario(usuario))    
    except:
        listaDeUsuarios = None
    return listaDeUsuarios
    
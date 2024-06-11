from src.func.buscarDados import BuscarDados
from src.utils.jsonParaUsuario import jsonParaUsuario

def pegarTodosUsuariosDoRedis():
    dados = BuscarDados("usuario")
    listaDeUsuarios = []
    for usuario in dados:
        listaDeUsuarios.append(jsonParaUsuario(usuario))
    return listaDeUsuarios    
    
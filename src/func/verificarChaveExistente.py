from src.func.buscarDados import BuscarDados
from src.data.redis.func.keys import key

def verificarChaveExistente(colecao, chaveParaVerificar):
    listaDeChaves = key(colecao)
    for chave in listaDeChaves:
        if chave.decode("utf-8") == chaveParaVerificar:
            return True
    return False
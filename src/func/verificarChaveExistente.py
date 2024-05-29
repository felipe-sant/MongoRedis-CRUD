from src.func.buscarDados import BuscarDados
from src.data.redis.func.keys import key

def verificarChaveExistente(colecao, chave):
    chaves = key(colecao)
    if chave in chaves:
        return True
    return False
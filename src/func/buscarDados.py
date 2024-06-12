from src.data.redis.func.keys import key
from src.data.redis.func.get import get

def BuscarDados(tipo):
    chaves = key(tipo)
    listaDados = []
    for chave in chaves:
        dado = get(chave)
        listaDados.append(dado)
    return listaDados
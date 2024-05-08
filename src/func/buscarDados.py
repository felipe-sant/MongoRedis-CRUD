import json
from src.data.redis.func.keys import key
from src.data.redis.func.get import get

def BuscarDados(tipo):
    chaves = key(tipo)
    listaDados = []
    for chave in chaves:
        dado = get(chave)
        dado = json.loads(dado.encode("utf-8"))
        listaDados.append(dado)
    return listaDados
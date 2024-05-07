from src.data.mongo.connection import database

def Buscar(colecao, filtro=None):
    try:
        dados = database[colecao].find(filtro)
        return dados
    except Exception as e:
        return None

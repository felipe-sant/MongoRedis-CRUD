from src.data.mongo.connection import database

def criar(colecao, dados):
    if type(dados) == dict:
        database[colecao].insert_one(dados)
        return "Documento inserido com sucesso!"
    elif type(dados) == list:
        database[colecao].insert_many(dados)
        return f"{len(dados)} documentos inseridos com sucesso!"
    else:
        return "Erro ao inserir documento!"

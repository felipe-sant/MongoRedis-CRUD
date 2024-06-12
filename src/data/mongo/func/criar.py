from src.data.mongo.connection import database

def criarMongo(colecao, dados):
    try:
        database[colecao].insert_one(dados)
    except Exception as e:
        print(f"Erro ao inserir documento! \n{e}")
        input()

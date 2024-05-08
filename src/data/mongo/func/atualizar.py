from src.data.mongo.connection import database

def atualizar(colecao, novoDado, filtro):
    try:
        database[colecao].update_many(filtro, {"$set": novoDado})
        return "Documento atualizado com sucesso!"
    except Exception as e:
        return f"Erro ao atualizar documento: {e}"

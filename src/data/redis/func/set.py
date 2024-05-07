from src.data.redis.connection import connection

def Set(chave, valor):
    connection.set(chave, valor)

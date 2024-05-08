from src.data.redis.connection import connection

def set(chave, valor):
    connection.set(chave, valor)

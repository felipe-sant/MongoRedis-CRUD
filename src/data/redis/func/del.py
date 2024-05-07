from src.data.redis.connection import connection

def Del(chave):
    connection.delete(chave)

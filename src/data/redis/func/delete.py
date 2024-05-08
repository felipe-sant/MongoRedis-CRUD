from src.data.redis.connection import connection

def delete(chave):
    connection.delete(chave)

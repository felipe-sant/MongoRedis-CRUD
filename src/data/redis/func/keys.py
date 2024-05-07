from src.data.redis.connection import connection

def Key(chave):
    return connection.keys(chave)

from src.data.redis.connection import connection

def key(chave):
    return connection.keys(chave+"@*")

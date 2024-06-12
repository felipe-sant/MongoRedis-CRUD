from src.data.redis.connection import connection

def expire(chave, segundos):
    connection.expire(chave, segundos)
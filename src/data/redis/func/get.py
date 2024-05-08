from src.data.redis.connection import connection

def get(chave):
    return connection.get(chave).decode('utf-8') if connection.get(chave) else None

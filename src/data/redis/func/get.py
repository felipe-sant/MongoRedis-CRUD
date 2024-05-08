from src.data.redis.connection import connection
import json

def get(chave):
    return json.loads(connection.get(chave))

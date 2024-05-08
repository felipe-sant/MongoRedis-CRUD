from src.data.redis.connection import connection
import json

def get(chave):
    try:
        return json.loads(connection.get(chave))
    except Exception as e:
        return None

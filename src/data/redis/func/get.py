from src.data.redis.connection import connection
import json

def get(chave, isJson = True):
    try:
        if isJson:
            return json.loads(connection.get(chave))
        return connection.get(chave)
    except Exception as e:
        print(e)
        return None

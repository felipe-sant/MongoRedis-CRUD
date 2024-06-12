from src.data.redis.func.keys import key
from src.data.redis.func.delete import delete

def deletarTodosVendedoresRedis():
    chaves = key("vendedor")
    for chave in chaves:
        try:
            delete(chave)
        except:
            print(f"Ocorreu um erro ao deletar a chave {chave}")
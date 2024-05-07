from src.data.redis.func.set import Set
from src.data.redis.func.get import Get

chave = 'teste'
valor = 'valor'

Set(chave, valor)

print(Get("pedro"))
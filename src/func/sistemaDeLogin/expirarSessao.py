from src.func.criarChave import criarChave
from src.data.redis.func.delete import delete
from src.func.verificarChaveExistente import verificarChaveExistente

def expirarSessao():
    sessao_chave = criarChave("sessions", "redis")
    if verificarChaveExistente("sessions", sessao_chave):
        delete(sessao_chave)
        
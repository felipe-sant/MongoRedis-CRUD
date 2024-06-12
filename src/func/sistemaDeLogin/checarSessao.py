from src.func.criarChave import criarChave
from src.func.verificarChaveExistente import verificarChaveExistente

def checarSessao():
    sessao_chave = criarChave("sessions", "redis")
    if verificarChaveExistente("sessions", sessao_chave):
        return True
    return False
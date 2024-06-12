from src.func.criarChave import criarChave
from src.data.redis.func.expire import expire
from src.data.redis.func.set import set

def definirTempoExpiracao():
    segundos = int(input("Digite o tempo de expiração da sessão em segundos: "))
    sessao_chave = criarChave("sessions", "tempoDeExpiracao")
    set(sessao_chave, segundos)
    print("\nTempo de expiração definido com sucesso!")
    input()
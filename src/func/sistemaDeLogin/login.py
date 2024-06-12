import getpass
from src.data.redis.func.get import get
from src.func.criarChave import criarChave
from src.utils.criptografarSenha import criptografarSenha
from src.data.redis.func.set import set
import hashlib
from src.data.redis.func.expire import expire
from src.menu.menuPrincipal import menuPrincipal

def login():
    nomeDeUser = str(input("Nome de usuário: "))
    senha = str(getpass.getpass("Senha: "))
    chave = criarChave("system_users", nomeDeUser)
    senhaDoServidor = get(chave, False)
    if senhaDoServidor != None:
        senhaDoServidor = senhaDoServidor.decode("utf-8")
    if criptografarSenha(senha) == senhaDoServidor:
        sessao_chave = criarChave("sessions", "redis")
        sessao_id = hashlib.sha256((nomeDeUser+senha).encode()).hexdigest()
        set(sessao_chave, sessao_id)
        
        tempoDeExpiracao_chave = criarChave("sessions", "tempoDeExpiracao")
        tempoDeExpiracao = get(tempoDeExpiracao_chave, False)
        expire(sessao_chave, tempoDeExpiracao)
        
        print("\nLogado com sucesso!")
        input()
        
        menuPrincipal()
    else:
        print("\nNome de usuário ou senha incorretos!")
        input()
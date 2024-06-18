from src.utils.criptografarSenha import criptografarSenha
import getpass
from src.func.criarChave import criarChave
from src.data.redis.func.set import set
from src.func.verificarChaveExistente import verificarChaveExistente

def registrar():
    nomeDeUser = str(input("Nome de usuário: "))
    senha = str(getpass.getpass("Senha: "))
    confirmacaoDeSenha = str(getpass.getpass("Confirme sua senha: "))
    
    if senha != confirmacaoDeSenha:
        print("\nAs senhas não coincidem!")
        input()
        return
    
    chave = criarChave("system_users", nomeDeUser)
    senhaCriptografada = criptografarSenha(senha)
    
    if verificarChaveExistente("system_users", chave):
        print("\nUsuário já existe!")
        input()
        return
    
    try:
        set(chave, senhaCriptografada)
        print("\nUsuário registrado com sucesso")
        input()
    except:
        print("\nErro ao registrar usuário")
        input()
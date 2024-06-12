import hashlib

def criptografarSenha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()
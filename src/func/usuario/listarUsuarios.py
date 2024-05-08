from src.utils.jsonParaUsuario import jsonParaUsuario
from src.data.mongo.func.buscar import buscar

def listarUsuarios(usuarios):
    total = len(usuarios)
    contador = 0
    for elemento in usuarios:
        contador += 1
        usuario = jsonParaUsuario(elemento)
        print(f"- usuário ({contador}/{total}) -")
        if "chave" in elemento:
            chave = elemento["chave"].replace("usuario@", "")
            print(f"_chave: {chave}")
        usuario.mostrar()
        input()
from src.utils.jsonParaUsuario import jsonParaUsuario

def listarUsuarios(usuarios):
    contador = 0
    total = len(usuarios)
    for elemento in usuarios:
        contador += 1
        usuario = jsonParaUsuario(elemento)
        print(f"- usuário - ({contador}/{total}) -")
        try:
            chave = elemento["chave"].replace("usuario@", "")
            print(f"chave: {chave}")  
        except:   
            pass
        usuario.mostrar()
        input()
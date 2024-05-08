from src.utils.jsonParaUsuario import jsonParaUsuario

def listarUsuarios(usuarios):
    if usuarios == []:
        print("Não há usuários cadastrados")
        input()
        return
        
    contador = 0
    total = len(usuarios)
    for elemento in usuarios:
        contador += 1
        usuario = jsonParaUsuario(elemento)
        print(f"- usuário ({contador}/{total}) -")
        if "chave" in elemento:
            chave = elemento["chave"].replace("usuario@", "")
            print(f"chave: {chave}")
        usuario.mostrar()
        input()
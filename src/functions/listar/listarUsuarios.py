from src.model.usuario import Usuario

def listarUsuarios(usuarios):
    contador = 0
    total = len(usuarios)
    for elemento in usuarios:
        contador += 1
        usuario = Usuario(elemento["nome"], elemento["endereco"], elemento["rg"])
        print(f"- Usuario ({contador}/{total}) -")
        try:
            chave = elemento["chave"]
            print(f"chave: {chave}")  
        except:   
            pass
        usuario.mostrar()
        input()
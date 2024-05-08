from src.model.usuario import Usuario

def listarUsuarios(usuarios):
    contador = 0
    total = len(usuarios)
    for elemento in usuarios:
        contador += 1
        usuario = Usuario(elemento["nome"], elemento["endereco"], elemento["rg"])
        print(f"- Usuario ({contador}/{total}) -")
        usuario.mostrar()
        input()
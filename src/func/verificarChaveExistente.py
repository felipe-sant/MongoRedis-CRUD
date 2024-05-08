from src.func.buscarDados import BuscarDados

def verificarChaveExistente(colecao, chave):
    listaDados = BuscarDados(colecao)
    for dado in listaDados:
        try:
            if dado["chave"] == chave:
                return True
        except:
            pass
    return False
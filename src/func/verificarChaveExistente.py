from src.func.buscarDados import BuscarDados

def verificarChaveExistente(colecao, chave):
    listaDados = BuscarDados(colecao)
    for dado in listaDados:
        if "chave" in dado and dado["chave"] == chave:
            return True
    return False
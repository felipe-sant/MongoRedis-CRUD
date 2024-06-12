from src.utils.limparTerminal import limparTerminal
from src.func.compra.cadastrarCompra import cadastrarCompra
from src.func.compra.listarCompra import listarCompra
from src.func.compra.deletarCompra import deletarCompra
from src.func.compra.atualizarCompra import atualizarCompra
from src.func.sistemaDeLogin.checarSessao import checarSessao

def menuCompra():
    while True:
        if not checarSessao():
            return
        
        limparTerminal()
        print("=-" * 30)
        print("Menu Compras")
        print("1 - Cadastrar Compra")
        print("2 - Listar Compras")
        print("3 - Atualizar Compra")
        print("4 - Deletar Compra")
        print("0 - Voltar")
        print("=-" * 30 + "\n")
        
        opcao = str(input("Digite a opção desejada: "))
        
        match opcao:
            case "1":
                cadastrarCompra()
            case "2":
                listarCompra()
            case "3":
                atualizarCompra()
            case "4":
                deletarCompra()
            case "0":
                break
            case _:
                print("\nOpção inválida\n")
                input()
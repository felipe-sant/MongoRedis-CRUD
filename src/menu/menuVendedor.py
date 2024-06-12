from src.utils.limparTerminal import limparTerminal
from src.func.vendedor.listarVendedor import listarVendedor
from src.func.vendedor.atualizarVendedor import atualizarVendedor
from src.func.vendedor.deletarVendedor import deletarVendedor
from src.func.vendedor.sincronizacao.moverVendedoresParaMongo import moverVendedoresParaMongo
from src.func.vendedor.cadastrarVendedor import cadastrarVendedor

def menuVendedor():
    while True:
        limparTerminal()
        print("=-" * 30)
        print("Menu Vendedor")
        print("1 - Cadastrar Vendedor")
        print("2 - Listar Vendedor")
        print("3 - Atualizar Vendedor")
        print("4 - Deletar Vendedor")
        print("5 - Mover Vendedores do Redis para MongoDB")
        print("0 - Voltar")
        print("=-" * 30 + "\n")

        opcao = str(input("Digite a opção desejada: "))

        match opcao:
            case "1":
                cadastrarVendedor()
            case "2":
                listarVendedor()
            case "3":
                atualizarVendedor()
            case "4":
                deletarVendedor()
            case "5":
                moverVendedoresParaMongo()
            case "0":
                break
            case _:
                print("\nOpção inválida\n")
                input()
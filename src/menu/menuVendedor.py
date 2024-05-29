from src.utils.limparTerminal import limparTerminal

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
                print("cadastrar vendendor")
            case "2":
                print("listar vendedor")
            case "3":
                print("atualizar vendedor")
            case "4":
                print("deletar vendedor")
            case "0":
                break
            case _:
                print("\nOpção inválida\n")
                input()
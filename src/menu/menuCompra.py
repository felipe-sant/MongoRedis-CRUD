from src.utils.limparTerminal import limparTerminal

def menuCompra():
    while True:
        limparTerminal()
        print("=-=" * 20)
        print("Menu Compras")
        print("1 - Cadastrar Compra")
        print("2 - Consultar Compras")
        print("3 - Atualizar Compra")
        print("4 - Deletar Compra")
        print("0 - Voltar")
        print("=-=" * 20 + "\n")
        
        opcao = str(input("Digite a opção desejada: "))
        
        match opcao:
            case "1":
                print("Cadastrar Compra")
                input()
            case "2":
                print("Consultar Compras")
                input()
            case "3":
                print("Atualizar Compra")
                input()
            case "4":
                print("Deletar Compra")
                input()
            case "0":
                break
            case _:
                print("\nOpção inválida\n")
                input()
from src.functions.limparTerminal import LimparTerminal

def MenuVendedor():
    while True:
        LimparTerminal()
        print("=-=" * 20)
        print("Menu Vendedor")
        print("1 - Cadastrar Vendedor")
        print("2 - Consultar Vendedores")
        print("3 - Atualizar Vendedor")
        print("4 - Deletar Vendedor")
        print("0 - Voltar")
        print("=-=" * 20 + "\n")
        
        opcao = str(input("Digite a opção desejada: "))
        
        match opcao:
            case "1":
                print("Cadastrar Vendedor")
                input()
            case "2":
                print("Consultar Vendedores")
                input()
            case "3":
                print("Atualizar Vendedor")
                input()
            case "4":
                print("Deletar Vendedor")
                input()
            case "0":
                break
            case _:
                print("Opção inválida")
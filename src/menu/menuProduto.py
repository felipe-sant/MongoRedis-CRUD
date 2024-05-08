from src.utils.limparTerminal import limparTerminal

def menuProduto():
    while True:
        limparTerminal()
        print("=-" * 30)
        print("Menu Produtos")
        print("1 - Cadastrar Produto")
        print("2 - Consultar Produtos")
        print("3 - Atualizar Produto")
        print("4 - Deletar Produto")
        print("0 - Voltar")
        print("=-" * 30 + "\n")
        
        opcao = str(input("Digite a opção desejada: "))
        
        match opcao:
            case "1":
                print("Cadastrar Produto")
                input()
            case "2":
                print("Consultar Produtos")
                input()
            case "3":
                print("Atualizar Produto")
                input()
            case "4":
                print("Deletar Produto")
                input()
            case "0":
                break
            case _:
                print("\nOpção inválida\n")
                input()
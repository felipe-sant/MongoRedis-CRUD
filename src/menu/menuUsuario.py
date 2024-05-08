from src.functions.limparTerminal import limparTerminal

def menuUsuario():
    while True:
        limparTerminal()
        print("=-=" * 20)
        print("Menu Usuários")
        print("1 - Cadastrar Usuário")
        print("2 - Consultar Usuários")
        print("3 - Atualizar Usuário")
        print("4 - Deletar Usuário")
        print("0 - Voltar")
        print("=-=" * 20 + "\n")
        
        opcao = str(input("Digite a opção desejada: "))
        
        match opcao:
            case "1":
                print("Cadastrar Usuário")
                input()
            case "2":
                print("Consultar Usuários")
                input()
            case "3":
                print("Atualizar Usuário")
                input()
            case "4":
                print("Deletar Usuário")
                input()
            case "0":
                break
            case _:
                print("Opção inválida")
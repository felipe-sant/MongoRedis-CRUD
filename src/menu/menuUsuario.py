from src.utils.limparTerminal import limparTerminal
from src.func.usuario.cadastrarUsuario import cadastrarUsuario
from src.func.usuario.consultarUsuario import consultarUsuario
from src.func.usuario.excluirUsuario import excluirTodosUsuarios, excluirUsuario
from src.func.usuario.atualizarUsuario import atualizarUsuario

def menuUsuario():
    while True:
        limparTerminal()
        print("=-" * 30)
        print("Menu Usuários")
        print("1 - Cadastrar Usuário")
        print("2 - Consultar Usuários")
        print("3 - Atualizar Usuário")
        print("4 - Deletar Usuário")
        print("0 - Voltar")
        print("=-" * 30 + "\n")
        
        opcao = str(input("Digite a opção desejada: "))
        
        match opcao:
            case "1":
                cadastrarUsuario()
            case "2":
                consultarUsuario()
            case "3":
                atualizarUsuario()
            case "4":
                excluirUsuario()
            case "5":
                excluirTodosUsuarios()
            case "0":
                break
            case _:
                print("\nOpção inválida\n")
                input()
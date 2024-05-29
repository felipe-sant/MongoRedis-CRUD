from src.utils.limparTerminal import limparTerminal
from src.func.usuario.cadastrarUsuario import cadastrarUsuario
from src.func.usuario.listarUsuario import listarUsuario
from src.func.usuario.deletarTodosUsuariosRedis import deletarTodosUsuariosRedis
from src.func.usuario.deletarUsuario import deletarUsuario
from src.func.usuario.atualizarUsuario import atualizarUsuario
from src.func.usuario.sincronizacao.moverUsuariosParaMongo import moverUsuariosParaMongo

def menuUsuario():
    while True:
        limparTerminal()
        print("=-" * 30)
        print("Menu Usuários")
        print("1 - Cadastrar Usuário")
        print("2 - Listar Usuários")
        print("3 - Atualizar Usuário")
        print("4 - Deletar Usuário")
        print("5 - Mover Usuários do Redis para MongoDB")
        print("0 - Voltar")
        print("=-" * 30 + "\n")
        
        opcao = str(input("Digite a opção desejada: "))
        
        match opcao:
            case "1":
                cadastrarUsuario()
            case "2":
                listarUsuario()
            case "3":
                atualizarUsuario()
            case "4":
                deletarUsuario()
            case "5":
                moverUsuariosParaMongo()
            case "0":
                break
            case _:
                print("\nOpção inválida\n")
                input()
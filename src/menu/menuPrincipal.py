from src.utils.limparTerminal import limparTerminal
from src.menu.menuUsuario import menuUsuario
from src.menu.menuVendedor import menuVendedor
from src.menu.menuProduto import menuProduto
from src.menu.menuCompra import menuCompra
from src.func.sistemaDeLogin.checarSessao import checarSessao
from src.func.sistemaDeLogin.expirarSessao import expirarSessao

def menuPrincipal():
    while True:
        if not checarSessao():
            print("\nVocê não está logado! Faça login para acessar o sistema")
            input()
            return
        
        limparTerminal()
        print("==" * 30)
        print("Menu Principal")
        print("1 - CRUD Compras")
        print("2 - CRUD Produtos")
        print("3 - CRUD Usuários (com redis)")
        print("4 - CRUD Vendedores (com redis)")
        print("9 - Expirar sessão")
        print("0 - Voltar")
        print("==" * 30 + "\n")
        
        opcao = str(input("Digite a opção desejada: "))
        
        match opcao:
            case "1":
                menuCompra()
            case "2":
                menuProduto()
            case "3":
                menuUsuario()
            case "4":
                menuVendedor()
            case "9":
                expirarSessao()
                break
            case "0":
                break
            case _:
                print("\nOpção inválida\n")
                input()
from src.functions.limparTerminal import LimparTerminal
from src.menu.menuCompra import MenuCompra
from src.menu.menuProduto import MenuProduto
from src.menu.menuUsuario import MenuUsuario
from src.menu.menuVendedor import MenuVendedor

def MenuPrincipal():
    while True:
        LimparTerminal()
        print("===" * 20)
        print("Menu Principal")
        print("1 - CRUD Compras")
        print("2 - CRUD Produtos")
        print("3 - CRUD Usuários")
        print("4 - CRUD Vendedores")
        print("5 - Sincronizar Dados")
        print("0 - Sair")
        print("===" * 20 + "\n")
        
        opcao = str(input("Digite a opção desejada: "))
        
        match opcao:
            case "1":
                MenuCompra()
            case "2":
                MenuProduto()
            case "3":
                MenuUsuario()
            case "4":
                MenuVendedor()
            case "5":
                print("Sincronizar Dados")
            case "0":
                break
            case _:
                print("Opção inválida")
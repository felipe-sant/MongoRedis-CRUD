def MenuPrincipal():
    while True:
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
                print("Compras")
            case "2":
                print("Produtos")
            case "3":
                print("Usuários")
            case "4":
                print("Vendedores")
            case "5":
                print("Sincronizar Dados")
            case "0":
                break
            case _:
                print("Opção inválida")
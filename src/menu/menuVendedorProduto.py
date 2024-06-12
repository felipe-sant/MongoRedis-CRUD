from src.utils.limparTerminal import limparTerminal
from src.model.vendedor import Vendedor
from src.func.vendedor.produtos.inserirProduto import inserirProduto
from src.func.vendedor.produtos.removerProduto import removerProduto
from src.func.produto.listarProduto import listarProduto
from src.func.vendedor.produtos.atualizarProdutos import atualizarProdutos

def menuVendedorProduto(vendedor: Vendedor):
    while True:
        limparTerminal()
        print("--" * 30)
        print("Inserção de produtos")
        print("1 - Inserir Produto")
        print("2 - Remover Produto")
        print("3 - Listar Produtos do vendedor")
        print("4 - Listar Todos Produtos")
        print("0 - Voltar")
        print("--" * 30 + "\n")
        
        opcao = str(input("Digite a opção desejada: "))
        
        match opcao:
            case "1":
                inserirProduto(vendedor)
            case "2":
                removerProduto(vendedor)
            case "3":
                print()
                for produto in vendedor.produtos:
                    print("_id: " + str(produto["_id"]))
                    print("Nome: " + produto["nome"])
                    print("Preço: " + str(produto["preco"]))
                    input()
            case "4":
                listarProduto()
            case "0":
                return
            case _:
                print("\nOpção inválida\n")
                input()
    
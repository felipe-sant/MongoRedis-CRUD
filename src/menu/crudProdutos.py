from src.utils.limparTerminal import limparTerminal
from src.model.vendedor import Vendedor
from src.func.produto.listarProduto import listarProduto
from src.data.mongo.func.deletar import deletarTodosMongo
from src.func.inserirProduto import inserirProduto
from src.func.removerProduto import removerProduto

def crudProdutos(colecao, isVendedor = False):
    while True:
        limparTerminal()
        print("--" * 30)
        print("Inserção de produtos")
        print("1 - Inserir Produto")
        print("2 - Remover Produto")
        print("3 - Listar Produtos")
        print("4 - Listar Todos Produtos registrados")
        print("0 - Voltar")
        print("--" * 30 + "\n")
        
        opcao = str(input("Digite a opção desejada: "))
        
        match opcao:
            case "1":
                if isVendedor:
                    inserirProduto(colecao, isVendedor)
                else:
                    inserirProduto(colecao)
            case "2":
                removerProduto(colecao)
            case "3":
                print()
                for produto in colecao.produtos:
                    print("_id: " + str(produto["_id"]))
                    print("Nome: " + produto["nome"])
                    print("Preço: " + str(produto["preco"]))
                    input()
            case "4":
                listarProduto()
            case "0":
                break
            case _:
                print("\nOpção inválida\n")
                input()
    
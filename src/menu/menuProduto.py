from src.utils.limparTerminal import limparTerminal
from src.func.produto.cadastrarProduto import cadastrarProduto
from src.func.produto.listarProduto import listarProduto
from src.func.produto.atualizarProduto import atualizarProduto
from src.func.produto.deletarProduto import deletarProduto
from src.data.mongo.func.deletar import deletarTodosMongo

def menuProduto():
    while True:
        limparTerminal()
        print("=-" * 30)
        print("Menu Produtos")
        print("1 - Cadastrar Produto")
        print("2 - Listar Produtos")
        print("3 - Atualizar Produto")
        print("4 - Deletar Produto")
        print("0 - Voltar")
        print("=-" * 30 + "\n")
        
        opcao = str(input("Digite a opção desejada: "))
        
        match opcao:
            case "1":
                cadastrarProduto()
            case "2":
                listarProduto()
            case "3":
                atualizarProduto()
            case "4":
                deletarProduto()
            case "0":
                break
            case _:
                print("\nOpção inválida\n")
                input()
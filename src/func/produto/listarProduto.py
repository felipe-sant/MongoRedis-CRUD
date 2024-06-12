from src.func.produto.buscarTodosProdutosDoMongo import buscarTodosProdutosDoMongo
from src.data.mongo.func.buscar import buscarMongo
from bson.objectid import ObjectId
from src.utils.jsonParaProduto import JsonParaProduto
from src.func.verificarIdExistente import verificarIdExistente

def listarProduto():
    id = input("Digite o id do produto (deixe em branco para listar todos): ")
    if (id == ""):
        listaDeProdutos = buscarTodosProdutosDoMongo()
        print()
        for i in range(len(listaDeProdutos)):
            print(f"- ({i+1}/{len(listaDeProdutos)}) -")
            listaDeProdutos[i].mostrar()
            input()
        return
    else:
        try:
            objectId = ObjectId(id)
        except:
            print("\nId inválido")
            input()
            return
        if not verificarIdExistente("produto", objectId):
            print("\nProduto não encontrado")
            input()
            return
        produtoJson = buscarMongo("produto", {"_id": objectId})[0]
        produto = JsonParaProduto(produtoJson)
        print()
        produto.mostrar()
        input()
        return
        
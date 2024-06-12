from bson.objectid import ObjectId
from src.func.verificarIdExistente import verificarIdExistente
from src.data.mongo.func.buscar import buscarMongo
from src.utils.jsonParaProduto import JsonParaProduto
from src.func.produto.criarProduto import criarProduto
from src.utils.usuarioParaJson import usuarioParaJson
from src.utils.produtoParaJson import produtoParaJson
from src.data.mongo.func.atualizar import atualizarMongo

def atualizarProduto():
    id = input("Digite o id do produto: ")
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
    produtoNovo = criarProduto()
    produto.atualizar(produtoNovo)
    produtoJson = produtoParaJson(produto)
    try:
        atualizarMongo("produto", produtoJson, {"_id": objectId})
        print("\nProduto atualizado com sucesso!")
        input()
    except:
        print("\nErro ao atualizar produto")
        input()
        return
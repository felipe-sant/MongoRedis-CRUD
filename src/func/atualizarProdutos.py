from src.data.mongo.func.buscar import buscarMongo
from src.utils.jsonParaProduto import JsonParaProduto
from src.utils.produtoParaJson import produtoParaJson
from bson.objectid import ObjectId
from src.data.mongo.func.atualizar import atualizarMongo

def atualizarProdutos(colecao):
    for produto in colecao.produtos:
        objectId = ObjectId(produto["_id"])
        produtoMongoJson = buscarMongo("produto", {"_id": objectId})[0]
        produtoMongo = JsonParaProduto(produtoMongoJson)
        produtoMongo.setVendedor(colecao)
        produtoMongoJson = produtoParaJson(produtoMongo)
        try:
            atualizarMongo("produto", produtoMongoJson, {"_id": objectId})
        except:
            print(f"\nErro ao atualizar produto {produtoMongo.nome}")
            input()
            return
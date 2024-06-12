from bson.objectid import ObjectId
from src.model.vendedor import Vendedor
from src.func.verificarIdExistente import verificarIdExistente
from src.data.mongo.func.buscar import buscarMongo

def inserirProduto(vendedor: Vendedor, isVendedor = False):
    id = str(input("Digite o id do produto: "))
    try:
        objectId = ObjectId(id)
    except:
        print("Id inválido")
        input()
        return None
    if verificarIdExistente("produto", objectId):
        produto = buscarMongo("produto", {"_id": objectId})[0]
        if produto is None:
            print("Produto não encontrado")
            input()
            return None
        else:
            if produto["vendedor"] != "Não possui vendedor cadastrado" and isVendedor:
                print("Produto já possui vendedor")
                input()
                return None
            jsonProduto = {
                "_id": str(produto["_id"]),
                "nome": produto["nome"],
                "descricao": produto["descricao"],
                "preco": produto["preco"]
            }
            vendedor.addProduto(jsonProduto)
            return "Produto inserido com sucesso"
    else:
        print("Produto não encontrado")
        input()
        return None
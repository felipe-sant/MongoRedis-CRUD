from src.model.vendedor import Vendedor
from bson.objectid import ObjectId
from src.data.mongo.func.buscar import buscarMongo
from src.func.verificarIdExistente import verificarIdExistente

def removerProduto(vendedor: Vendedor):
    id = str(input("Digite o id do produto: "))
    try:
        objectId = ObjectId(id)
    except:
        print("Id inválido")
        input()
        return None
    if (verificarIdExistente("vendedor", objectId)):
        produto = buscarMongo("produto", {"_id": objectId})[0]
        if produto is None:
            print("Produto não encontrado")
            input()
            return None
        else:
            jsonProduto = {
                "_id": str(produto["_id"]),
                "nome": produto["nome"],
                "descricao": produto["descricao"],
                "preco": produto["preco"]
            }
            vendedor.removeProduto(jsonProduto)
            return "Produto removido com sucesso"
from src.func.criarChave import criarChave
from src.func.verificarChaveExistente import verificarChaveExistente
from src.utils.jsonParaVendedor import jsonParaVendedor
from src.data.redis.func.get import get
from src.func.vendedor.criarVendedor import criarVendedor
from bson.objectid import ObjectId
from src.func.verificarIdExistente import verificarIdExistente
from src.func.vendedor.sincronizacao.atualizarVendedorNoRedis import atualizarVendedorNoRedis
from src.data.mongo.func.buscar import buscarMongo
from src.func.vendedor.sincronizacao.atualizarVendedorNoMongo import atualizarVendedorNoMongo
from src.menu.crudProdutos import crudProdutos

def atualizarVendedor():
    id = input("Digite o id do vendedor: ")
    try:
        chave = criarChave("vendedor", id)
        if (verificarChaveExistente("vendedor", chave)):
            vendedor = jsonParaVendedor(get(chave))
            vendedorNovo = criarVendedor(chave)
            atualizarVendedorNoRedis(chave, vendedor, vendedorNovo)
            return
        else:
            raise
    except:
        try:
            id = ObjectId(id)
            if (verificarIdExistente("vendedor", id)):
                vendedor = jsonParaVendedor(buscarMongo("vendedor", {"_id": id})[0])
                vendedorNovo = criarVendedor(str(id))
                atualizarVendedorNoMongo(id, vendedor, vendedorNovo)
                input()
                return
            else:
                raise
        except:
            pass
    print("\nVendedor não encontrado")
    input()
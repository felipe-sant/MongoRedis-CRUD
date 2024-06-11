from src.model.vendedor import Vendedor
from src.utils.vendedorParaJson import vendedorParaJson
from src.data.mongo.func.criar import criarMongo

def adicionarVendedorAoMongo(vendedorJson: Vendedor):
    vendedor = vendedorParaJson(vendedorJson, False)
    criarMongo("vendedor", vendedor)
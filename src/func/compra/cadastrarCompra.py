from src.data.mongo.func.criar import criarMongo
from src.func.compra.criarCompra import criarCompra
from src.utils.compraParaJson import compraParaJson
from src.menu.crudProdutos import crudProdutos
from src.func.compra.usuario.setarUsuario import setarUsuario

def cadastrarCompra():
    compra = criarCompra()
    setarUsuario(compra)
    crudProdutos(compra)
    compraJson = compraParaJson(compra)
    criarMongo("compra", compraJson)
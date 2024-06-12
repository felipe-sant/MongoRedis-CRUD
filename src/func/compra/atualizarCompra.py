from bson.objectid import ObjectId
from src.func.verificarIdExistente import verificarIdExistente
from src.data.mongo.func.buscar import buscarMongo
from src.utils.jsonParaCompra import jsonParaCompra
from src.func.compra.criarCompra import criarCompra
from src.utils.compraParaJson import compraParaJson
from src.data.mongo.func.atualizar import atualizarMongo
from src.func.compra.usuario.setarUsuario import setarUsuario
from src.menu.crudProdutos import crudProdutos

def atualizarCompra():
    id = input("Digite o id da compra: ")
    try:
        objectId = ObjectId(id)
    except:
        print("\nId inválido")
        input()
        return
    if not verificarIdExistente("compra", objectId):
        print("\nCompra não encontrada")
        input()
        return
    compraJson = buscarMongo("compra", {"_id": objectId})[0]
    compra = jsonParaCompra(compraJson)
    compraNova = criarCompra()
    compra.atualizar(compraNova)
    opcao = input("Deseja mudar o usuário? (s/n): ")
    if opcao == "s":
        setarUsuario(compra)
    opcao = input("Deseja mudar os produtos? (s/n): ")
    if opcao == "s":
        crudProdutos(compra)
    compraJson = compraParaJson(compra)
    try:
        atualizarMongo("compra", compraJson, {"_id": objectId})
        print("\nCompra atualizada com sucesso!")
        input()
    except:
        print("\nErro ao atualizar compra")
        input()
        return
    
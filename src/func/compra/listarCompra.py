from bson import ObjectId
from src.utils.jsonParaCompra import jsonParaCompra
from src.data.mongo.func.buscar import buscarMongo
from src.func.verificarIdExistente import verificarIdExistente
from src.func.compra.buscarTodasComprasDoMongo import buscarTodasComprasDoMongo

def listarCompra():
    id = input("Digite o id da compra (deixe em branco para listar todas): ")
    if id == "":
        listaDeCompras = buscarTodasComprasDoMongo()
        if len(listaDeCompras) == 0:
            print("\nNenhuma compra registrada")
            input()
        print()
        for i in range(len(listaDeCompras)):
            print(f"- ({i+1}/{len(listaDeCompras)}) -")
            listaDeCompras[i].mostrar()
            input()
        return
    else:
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
        print()
        compra.mostrar()
        input()
        return
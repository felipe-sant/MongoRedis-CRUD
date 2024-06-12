from src.model.compra import Compra

def jsonParaCompra(compraJson):
    compra = Compra(
        compraJson["data_compra"],
        compraJson["usuario"],
        compraJson["produtos"],
        compraJson["_id"]
    )
    return compra
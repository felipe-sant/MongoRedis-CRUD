from src.model.vendedor import Vendedor

def jsonParaVendedor(vendedorJson):
    vendedor = Vendedor(
        vendedorJson["_id"],
        vendedorJson["nome"],
        vendedorJson["rg"],
        vendedorJson["produtos"]
    )
    return vendedor
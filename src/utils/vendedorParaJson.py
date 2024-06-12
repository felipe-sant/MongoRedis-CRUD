import json

def vendedorParaJson(vendedor, hasId = True):
    if hasId:
        vendedorParaJson = {
            "_id": vendedor.id,
            "nome": vendedor.nome,
            "rg": vendedor.rg,
            "produtos": vendedor.produtos
        }
        input()
        return json.dumps(vendedorParaJson)
    if not hasId:
        vendedorParaJson = {
            "nome": vendedor.nome,
            "rg": vendedor.rg,
            "produtos": vendedor.produtos
        }
        return vendedorParaJson
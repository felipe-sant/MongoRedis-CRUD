from src.model.produto import Produto

def pegarVendedor(vendedor):
    if vendedor == None:
        return "Não possui vendedor cadastrado"
    else:
        vendedorJson = {
            "_id": vendedor.id,
            "nome": vendedor.nome,
        }
        return vendedorJson
    
def produtoParaJson(produto: Produto):
    produtoJson = {
        "nome": produto.nome,
        "vendedor": pegarVendedor(produto.vendedor),
        "descricao": produto.descricao,
        "preco": produto.preco,
        "estoque": produto.estoque,
    }
    return produtoJson
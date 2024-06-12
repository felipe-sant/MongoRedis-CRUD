from src.model.produto import Produto

def JsonParaProduto(produtoJson):
    produto = Produto(
        produtoJson["nome"], 
        produtoJson["descricao"], 
        produtoJson["preco"], 
        produtoJson["estoque"], 
        produtoJson["vendedor"], 
        produtoJson["_id"]
    )
    return produto
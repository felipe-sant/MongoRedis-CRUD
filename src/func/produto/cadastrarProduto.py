from src.func.produto.criarProduto import criarProduto
from src.utils.produtoParaJson import produtoParaJson
from src.data.mongo.func.criar import criarMongo

def cadastrarProduto():
    produto = criarProduto()
    produtoJson = produtoParaJson(produto)
    criarMongo("produto", produtoJson)
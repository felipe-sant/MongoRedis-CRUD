from src.model.vendedor import Vendedor
from src.utils.vendedorParaJson import vendedorParaJson
from src.data.redis.func.set import set

def atualizarVendedorNoRedis(id, vendedor: Vendedor, vendedorNovo: Vendedor):
    vendedor.atualizar(vendedorNovo)
    vendedorJson = vendedorParaJson(vendedor)
    try:
        set(id, vendedorJson)
        return "Vendedor atualizado com sucesso!"
    except Exception as e:
        return f"Erro: {e}"
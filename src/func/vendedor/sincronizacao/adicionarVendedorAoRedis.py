from src.data.redis.func.set import set
from src.model.vendedor import Vendedor
from src.utils.vendedorParaJson import vendedorParaJson

def adicionarVendedorAoRedis(vendedor: Vendedor):
    vendedorJson = vendedorParaJson(vendedor)
    try:
        set(vendedor.id, vendedorJson)
        return "Vendedor cadastrado com sucesso!"
    except Exception as e:
        return f"Erro: {e}"
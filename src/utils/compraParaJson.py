def pegarUsuario(usuario):
    if usuario is None:
        return "Não possui usuário cadastrado"
    else:
        usuarioJson = {
            "_id": usuario["_id"],
            "nome": usuario["nome"],
            "endereco": usuario["endereco"],
        }
        return usuarioJson

def compraParaJson(compra):
    compraJson = {
        "usuario": pegarUsuario(compra.usuario),
        "produtos": compra.produtos,
        "data_compra": compra.data_compra,
        "valorTotal": compra.valorTotal
    }
    return compraJson
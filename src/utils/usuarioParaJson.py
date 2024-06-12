import json

def usuarioParaJson(usuario, hasId = True):
    if hasId:
        usuarioJson = {
            "_id": usuario.id,
            "nome": usuario.nome,
            "endereco": usuario.endereco,
            "rg": usuario.rg
        }
        return json.dumps(usuarioJson)
    if not hasId:
        usuarioJson = {
            "nome": usuario.nome,
            "endereco": usuario.endereco,
            "rg": usuario.rg
        }
        return usuarioJson
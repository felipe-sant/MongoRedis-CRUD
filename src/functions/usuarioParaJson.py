import json

def usuarioParaJson(usuario):
    usuarioJson = {
        "nome": usuario.nome,
        "endereco": usuario.endereco,
        "rg": usuario.rg
    }
    return json.dumps(usuarioJson)
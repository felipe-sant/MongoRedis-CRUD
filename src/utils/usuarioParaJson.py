import json

def usuarioParaJson(usuario, chave = None):
    if chave != None:
        usuarioJson = {
            "nome": usuario.nome,
            "endereco": usuario.endereco,
            "rg": usuario.rg,
            "chave": chave
        }
    else:
        usuarioJson = {
            "nome": usuario.nome,
            "endereco": usuario.endereco,
            "rg": usuario.rg
        }
    return json.dumps(usuarioJson)
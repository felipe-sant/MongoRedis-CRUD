from bson.objectid import ObjectId
from src.func.vendedor.sincronizacao.pegarTodosVendedoresDoRedis import pegarTodosVendedoresDoRedis
from src.func.verificarChaveExistente import verificarChaveExistente
from src.func.criarChave import criarChave
from src.func.verificarIdExistente import verificarIdExistente
from src.func.vendedor.sincronizacao.pegarTodosVendedoresDoMongo import pegarTodosVendedoresDoMongo
from src.func.vendedor.sincronizacao.moverVendedoresParaMongo import moverVendedoresParaMongo

def listarVendedor():
    id = input("Digite o id do vendedor (ou deixe em branco para listar todos): ")
    if id == "":
        moverVendedoresParaMongo()
        listaDeVendedores = pegarTodosVendedoresDoMongo()
        print()
        for i in range(len(listaDeVendedores)):
            print(f"- ({i+1}/{len(listaDeVendedores)}) -")
            listaDeVendedores[i].mostrar()
            input()
        return
    else:
        try:
            chave = criarChave("vendedor", id)
            print()
            if (verificarChaveExistente("vendedor", chave)):
                listaDeVendedores = pegarTodosVendedoresDoRedis()
                for vendedor in listaDeVendedores:
                    if vendedor.id == chave:
                        vendedor.mostrar()
                        input()
                return
            else:
                raise
        except:
            try:
                id = ObjectId(id)
                print()
                if (verificarIdExistente("vendedor", id)):
                    listaDeVendedores = pegarTodosVendedoresDoMongo()
                    for vendedor in listaDeVendedores:
                        if vendedor.id == id:
                            vendedor.mostrar()
                            input()
                    return
                else:
                    raise
            except:
                pass
        print("Vendedor não encontrado!")
        input()
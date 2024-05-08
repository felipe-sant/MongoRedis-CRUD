from src.func.criarChave import criarChave
from src.func.verificarChaveExistente import verificarChaveExistente
from src.data.redis.func.delete import delete
from src.data.redis.func.keys import key

def excluirUsuario():
    chaveParaExcluir = criarChave("usuario")
    try:
        if (verificarChaveExistente("usuario", chaveParaExcluir)):
            delete(chaveParaExcluir)
            print("\nUsuário deletado com sucesso!")
            input()
        else:
            raise Exception("Chave não encontrada!")
    except Exception as e:
        print(f"\nErro ao deletar usuário: {e}")
        input()

def excluirTodosUsuarios():
    chaves = key("usuario")
    for chave in chaves:
        try:
            delete(chave)
            print(f"Chave {chave} deletada com sucesso")
        except Exception as e:
            print(f"Ocorreu um erro ao deletar a chave {chave}")
    print("\nTodos os usuários foram deletados com sucesso!")
    input()
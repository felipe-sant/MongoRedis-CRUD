from src.func.criarChave import criarChave
from src.func.verificarChaveExistente import verificarChaveExistente
from src.data.redis.func.delete import delete

def excluirUsuario():
    chaveParaExcluir = criarChave("usuario")
    try:
        if (verificarChaveExistente("usuario", chaveParaExcluir)):
            delete(chaveParaExcluir)
            print("\nUsuário deletado com sucesso!")
        else:
            raise Exception("Chave não encontrada!")
    except Exception as e:
        print(f"Erro ao deletar usuário: {e}")

from src.data.mongo.func.deletar import Deletar
from src.data.mongo.func.buscar import Buscar
from src.data.mongo.func.criar import Criar
from src.data.mongo.func.atualizar import Atualizar

# print(Criar("testes",
#     {
#         "nome": "João",
#         "idade": 20
#     }
# ))

print(Atualizar("testes",
    {
        "nome": "João",
        "idade": 27
    },
    {
        "nome": "João"
    }            
    ))

dados = Buscar("testes")

for dado in dados:
    print(dado)
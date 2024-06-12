from src.data.redis.func.set import set

class Vendedor():
    def __init__(self, id, nome, rg, produtos: dict = None) -> None:
        self.id = id
        self.nome = nome
        self.rg = rg
        if produtos == None:
            self.produtos = []
        else:
            self.produtos = produtos
    
    def atualizar(self, vendedor):
        if vendedor.id != "":
            self.setId(vendedor.id)
        if vendedor.nome != "":
            self.setNome(vendedor.nome)
        if vendedor.rg != "":
            self.setRg(vendedor.rg)
        
    def setId(self, id):
        self.id = id
    
    def setNome(self, nome):
        self.nome = nome
    
    def setRg(self, rg):
        self.rg = rg
        
    def setProdutos(self, produtos):
        self.produtos = produtos
        
    def addProduto(self, produto):
        self.produtos.append(produto)
        
    def removeProduto(self, produto):
        self.produtos.remove(produto)
        
    def mostrar(self):
        print(f"id: {self.id}")
        print(f"nome: {self.nome}")
        print(f"rg: {self.rg}")
        if len(self.produtos) > 0:
            print("produtos:")
            for produto in self.produtos:
                print("\t-----------------")
                print(f"\t_id: {produto['_id']}")
                print(f"\tnome: {produto['nome']}")
                print(f"\tpreco: {produto['preco']}")

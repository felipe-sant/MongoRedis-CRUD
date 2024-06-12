class Produto:
    def __init__ (self, nome, descricao, preco, estoque, vendedor = None, id = None) -> None:
        if id == None:
            self.id = None
        else:
            self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        if vendedor == None:
            self.vendedor = None
        else:
            self.vendedor = vendedor
    
    def atualizar(self, produto):
        if produto.nome != "":
            self.setNome(produto.nome)
        if produto.descricao != "": 
            self.setDescricao(produto.descricao)
        if produto.preco != "":
            self.setPreco(produto.preco)
        if produto.estoque != "":
            self.setEstoque(produto.estoque)
        if produto.vendedor != "Não possui vendedor cadastrado":
            self.setVendedor(produto.vendedor)
    
    def setId(self, id):
        self.id = id
    
    def setNome(self, nome):
        self.nome = nome
    
    def setDescricao(self, descricao):
        self.descricao = descricao
        
    def setPreco(self, preco):
        self.preco = preco
    
    def setEstoque(self, estoque):
        self.estoque = estoque
        
    def aumentarEstoque(self, quantidade):
        self.estoque += quantidade
    
    def diminuirEstoque(self, quantidade):
        if self.estoque - quantidade < 0:
            print("Estoque insuficiente")
        else:
            self.estoque -= quantidade
        
    def setVendedor(self, vendedor):
        self.vendedor = vendedor
        
    def mostrar(self):
        print(f"_id: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Descrição: {self.descricao}")
        print(f"Preço: {self.preco}")
        print(f"Estoque: {self.estoque}")
        if type(self.vendedor) == str:
            print("Vendedor: Não possui vendedor cadastrado")
        else:
            print("Vendedor:")
            print("_id:", self.vendedor["_id"])
            print("Nome:", self.vendedor["nome"])
    
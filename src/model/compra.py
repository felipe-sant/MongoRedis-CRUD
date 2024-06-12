from datetime import date

class Compra:
    def calcularValorTotal(self):
        valor = 0
        for produto in self.produtos:
            valor += int(produto["preco"])
        self.valorTotal = valor
    
    def __init__ (self, data_compra, usuario = None, produtos = None, id = None) -> None:
        if id == None:
            self.id = None
        else:
            self.id = id
        self.data_compra = data_compra
        self.valorTotal = 0
        if usuario == None:
            self.usuario = None
        else:
            self.usuario = usuario
        if produtos == None:
            self.produtos = []
        else:
            self.produtos = produtos
            self.calcularValorTotal()
    
    def atualizar(self, compra):
        if compra.data_compra != "":
            self.setDataCompra(compra.dataCompra)
            
    def setId(self, id):
        self.id = id
    
    def setDataCompra(self, data_compra):
        self.data_compra = data_compra
    
    def setUsuario(self, usuario):
        self.usuario = usuario
        
    def setProdutos(self, produtos):
        self.produtos = produtos
        self.calcularValorTotal()
        
    def addProduto(self, produto):
        self.produtos.append(produto)
        self.calcularValorTotal()
    
    def removeProduto(self, produto):
        self.produtos.remove(produto)
        self.calcularValorTotal()
        
    def mostrar(self):
        print(f"_id: {self.id}")
        print(f"Data da compra: {self.data_compra}")
        print(f"Valor total: {self.valorTotal}")
        if self.usuario != None:
            print("Usuario:")
            print(f"_id: {self.usuario['_id']}")
            print(f"Nome: {self.usuario['nome']}")
            print(f"Endereco: {self.usuario['endereco']}")
        if len(self.produtos) > 0:
            print("Produtos:")
            for produto in self.produtos:
                print("\t-----------------")
                print(f"\t_id: {produto['_id']}")
                print(f"\tnome: {produto['nome']}")
                print(f"\tpreco: {produto['preco']}")
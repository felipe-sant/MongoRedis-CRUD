class Usuario():
    def __init__(self, id, nome:str, endereco:str, rg:str) -> None:
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.rg = rg
    
    def atualizar(self, usuario):
        if usuario.id != "":
            self.setId(usuario.id)
        if usuario.nome != "":
            self.setNome(usuario.nome)
        if usuario.endereco != "":
            self.setEndereco(usuario.endereco)
        if usuario.rg != "":
            self.setRg(usuario.rg)
    
    def setId(self, id:str):
        self.id = id
    
    def setNome(self, nome:str):
        self.nome = nome
        
    def setEndereco(self, endereco:str):
        self.endereco = endereco
        
    def setRg(self, rg:str):
        self.rg = rg
    
    def mostrar(self):
        print(f"id: {self.id}")
        print(f"nome: {self.nome}")
        print(f"endereco: {self.endereco}")
        print(f"rg: {self.rg}")
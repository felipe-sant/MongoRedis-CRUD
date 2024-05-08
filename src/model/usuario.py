class Usuario():
    def __init__(self, nome:str, endereco:str, rg:str) -> None:
        self.nome = nome
        self.endereco = endereco
        self.rg = rg
    
    def atualizar(self, usuario):
        if usuario.nome != "":
            self.setNome(usuario.nome)
        if usuario.endereco != "":
            self.setEndereco(usuario.endereco)
        if usuario.rg != "":
            self.setRg(usuario.rg)
    
    def setNome(self, nome:str):
        self.nome = nome
        
    def setEndereco(self, endereco:str):
        self.endereco = endereco
        
    def setRg(self, rg:str):
        self.rg = rg
        
    # dev functions
    
    def mostrar(self):
        print(f"nome: {self.nome}")
        print(f"endereco: {self.endereco}")
        print(f"rg: {self.rg}")
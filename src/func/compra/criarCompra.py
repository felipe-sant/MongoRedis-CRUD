from src.model.compra import Compra

def criarCompra():
    data_compra = str(input("Digite a data da compra (dd/mm/yyyy): "))
    compra = Compra(data_compra) 
    return compra
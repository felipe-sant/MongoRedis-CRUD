from src.utils.limparTerminal import limparTerminal
from src.func.sistemaDeLogin.registrar import registrar
from src.func.sistemaDeLogin.login import login
from src.func.sistemaDeLogin.definirTempoExpiracao import definirTempoExpiracao
from src.func.sistemaDeLogin.checarSessao import checarSessao
from src.menu.menuPrincipal import menuPrincipal

def menuLogin():
    if checarSessao():
        menuPrincipal()
        
    while True:
        limparTerminal()
        print("≡≡" * 30)
        print("Bem Vindo ao CRUD utilizando Redis e MongoDB!")
        print("1 - Registrar")
        print("2 - Fazer login")
        print("3 - Definir tempo de expiração do próprio login")
        print("0 - Sair")
        print("≡≡" * 30)
        
        opcao = str(input("Digite a opção desejada: "))
        
        match opcao:
            case "1":
                registrar()
            case "2":
                login()
            case "3":
                definirTempoExpiracao()
            case "0":
                limparTerminal()
                break
            case _:
                print("\nOpção inválida\n")
                input()
        
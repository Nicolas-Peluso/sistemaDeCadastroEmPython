import os
userList = []

def Painel():
    print("+=+=+=++=+=ESCOLA ASSIS=+=+=++=+=+=")
    print("Digite uma operação")
    print("1 - Cadastrar novo usuario")
    print("2 - Consultar usuario")
    print("+=+=+=++=+=+=++=+=+=++=+=+=++=+=+=+")

def Cadastrar():
    Nome = str(input("Digite seu Nome: "))
    Endereço = str(input("Digite seu Endereço: "))
    
    userList.append({"Nome": Nome, "Endereço": Endereço})
    Start()

def Consultar():
    for user in userList:
        print(user)

def Start():
    Painel()
    operacao = int(input(""))

    match operacao:
        case 1:
            Cadastrar()
        case 2:
            Consultar()
        case _:
            os.system("clear") or None #limpar o terminal
            print("Operação invalida")
            Start()

Start()

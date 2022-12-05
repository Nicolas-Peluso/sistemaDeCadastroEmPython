import os;
userList = [];

def CleanTerminal():
    os.system("clear") or None; #limpar o terminal


def Painel():
    print("+=+=+=++=+=ESCOLA ASSIS=+=+=++=+=+=");
    print("Digite uma operação");
    print("1 - Cadastrar novo usuario");
    print("2 - Consultar usuario");
    print("3 - Editar usuario");
    print("4 - Sair");
    print("+=+=+=++=+=+=++=+=+=++=+=+=++=+=+=+");

def Cadastrar():
    Nome = str(input("Digite seu Nome: "))
    Senha = str(input("Digite seu Senha: "))
    
    userList.append({"Nome": Nome, "Senha": Senha})
    CleanTerminal()
    print("Usuario cadstrado com sucesso")

def Consultar(EditOrConsult):
    #um loop para verificar de o nome de usuario existe
    UserName = str(input("Digite o Nome de Usuario (O nome deve ser o mesmo cadastrado): "));
    HasUser = False;
    Index = 0;
    UserGotPermission = False;

    #salvando o index desse usuario caso ele exista 
    for index in range(len(userList)):
        if(userList[index]["Nome"] == UserName):
            HasUser = True;
            Index = index;
            break;
    
    #usuario não encontrado
    if HasUser == False:
        CleanTerminal();
        print("usuario nao encontrado");

    #verificando se a senha do usuario confere
    while HasUser:
        Pass = str(input("Digite a senha: "));
        if(Pass == userList[Index]["Senha"]):
            UserGotPermission = True;
            break;
        CleanTerminal()

    #a função consultar tambem é usada para consultas pela função Edit entao é aqui que sera verificado quem esta usando essa função
    if(EditOrConsult == "Editar"):
        return UserGotPermission;
    else:
        #se a função for usado para consulta e se o usuario tiver a permissão sera exibido as Informações referente a sua conta
        if(UserGotPermission):
            print("Nome: ", userList[Index]["Nome"]);
            print("Senha: ", userList[Index]["Senha"]);

def Edit(Edit):
    #a função Consultr vai retornar um boolean para saber se o usuario tem permissão para editar
    UserHasPermition = Consultar(Edit);
    if(UserHasPermition == True):
        print("editar");
    else:
        print("Você não tem permissão para editar esse usuario");


while True:
    Painel()
    operacao = int(input(""));

    match operacao:
        case 1:
            Cadastrar();
        case 2:
            Consultar("Consultar");
        case 3:
            Edit("Editar");
        case 4:
            break;
        case _:
            CleanTerminal();
            print("Operação invalida");
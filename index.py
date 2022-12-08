import os;
userList = [];

def CleanTerminal():
    os.system("clear") or None; #limpar o terminal


def Painel():
    print("+=+=+=++=+=ESCOLA ASSIS=+=+=++=+=+=");
    print("DIGITE UMA OPERAÇÃO");
    print("1 - Cadastrar novo usuario");
    print("2 - Consultar usuario");
    print("3 - Editar usuario");
    print("4 - Sair");
    print("+=+=+=++=+=+=++=+=+=++=+=+=++=+=+=+");


def PainelEditar():
    print("+=+=+=++=+=ESCOLA ASSIS - PAINEL DE EDIÇÃO DE USUARIO=+=+=++=+=+=");
    print("DIGITE UMA OPERAÇÃO");
    print("1 - Editar Nome");
    print("2 - Editar Senha");
    print("3 - Sair");
    print("+=+=+=++=+=+=++=+=+=++=+=+=++=+=+=+");


def Cadastrar():
    Nome = str(input("Digite seu Nome: "))
    Senha = str(input("Digite seu Senha: "))
    
    userList.append({"Nome": Nome, "Senha": Senha})
    CleanTerminal()
    print("Usuario cadstrado com sucesso")

def Consultar(EditOrConsult):
    print("+=+=+=++=+=ESCOLA ASSIS - LOGIN=+=+=++=+=+=");
    UserName = str(input("Digite o Nome de Usuario cadastrado: "));
    HasUser = False;
    Index = -1;
    UserGotPermission = False;

    #um loop para verificar de o nome de usuario existe e salvando o index desse usuario caso ele exista 
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
        return Index;
    else:
        #se a função for usado para consulta e se o usuario tiver a permissão sera exibido as Informações referente a sua conta
        if(UserGotPermission):
            print("Nome: ", userList[Index]["Nome"]);
            print("Senha: ", userList[Index]["Senha"]);

def Edit(Edit):
    #a função Consultar vai retornar um boolean para saber se o usuario tem permissão para editar
    Index = Consultar(Edit);

    if(Index != -1):
        CleanTerminal();
        PainelEditar();
        operacao = int(input(">> "));
        
        while True:

            match operacao:

                case 1:
                    NewUserName = str(input("Digite o novo nome De usuario: "));
                    ActualUserName = userList[Index]["Nome"];
                    if(len(NewUserName) <= 0): #tratamento caso input estaja vazio
                        print("O nome de usuario não pode estar vazio");
                        
                    elif(ActualUserName == NewUserName):
                        print("O Novo nome de usuario deve ser diferente do Atual");
                         
                    # se todas as condições forem atendidas o Nome de usuario sera alterado
                    else:
                        userList[Index]["Nome"] = NewUserName;
                        CleanTerminal();
                        print("alterado com sucesso");
                        break;            

                case 2:
                    NewUserPass = str(input("Digite a nova Senha: "));
                    ActualUserPass = userList[Index]["Senha"];
                    if(len(NewUserPass) <= 0 & len(NewUserPass) <= 4):
                        print("A senha deve ser maior que 4 digitos");
                        
                    elif(ActualUserPass == NewUserPass):
                        CleanTerminal();
                        print("A nova senha não pode ser igual a senha atual.");
                    
                    # se todas as condições forem atendidas a senha sera alterada
                    else: 
                        userList[Index]["Senha"] = NewUserPass;
                        CleanTerminal();
                        print("alterado com sucesso");
                        break;                    

                case 3:
                    break;
                
                case _:
                    print("opção invalida");

while True:
    Painel()
    operacao = int(input(">> "));

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
import os;
userList = [];

    #Ja que vou ter que realizar verificações tanto na hora do cadastro quanto na edição ter uma função para isso evita código repetido
def VerifyLength(TextoParaVerificar, TipoDeVerificacao):
    if(TipoDeVerificacao == "Senha"):
        if(len(TextoParaVerificar) == 0 or len(TextoParaVerificar) <= 4):
            return False;

    if(TipoDeVerificacao == "UserName"):
        #o Nome de usuario tem um limitador de tamanho da string ja que uma string sem limite pode causar brechas de segurança
        if(len(TextoParaVerificar) == 0 or len(TextoParaVerificar) >= 25):
            return False;
    return True;

def UsuarioExiste(UserName):
    #onjetivo dessa função é verficar se o Nome de usuario existe na lista
    DadosUteis = {"UsuarioExiste": False, "index": 0};

    #essa vericação é caso esse seja o primeiro usuario cadastrado.
    if(len(userList) == 0):
        DadosUteis["UsuarioExiste"] = False;
        return DadosUteis;

    #essa função é usado para cadastro e consulta
    for index in range(len(userList)):
        if(userList[index]["Nome"] == UserName):
            DadosUteis["UsuarioExiste"] = True;
            DadosUteis["index"] = index;
            return DadosUteis;
            break;
        else:
            return DadosUteis;


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
    #print("3 - Editar Endereço");
    print("3 - Sair");
    print("+=+=+=++=+=+=++=+=+=++=+=+=++=+=+=+");


#def PainelEdiçãoEndereço():
  #  print("+=+=+=++=+=ESCOLA ASSIS - PAINEL DE EDIÇÃO DE ENDEREÇO=+=+=++=+=+=");
 #   print("DIGITE UMA OPERAÇÃO");
 #   print("1 - Editar Rua: ");
  #  print("2 - Editar Bairro: ");
  #  print("3 - Editar Numero Da casa: ");
 #   print("4 - Editar Numero do CEP: ");
  #  print("5 - Sair");
  #  print("+=+=+=++=+=+=++=+=+=++=+=+=++=+=+=+");


def Cadastrar():

    while True:
        Nome = str(input("Digite seu Nome: "));
        #usando a função VerifyLength para verificar a string Do Nome
        if (VerifyLength(Nome, "UserName") == False):
            CleanTerminal()
            print("O nome de usuario não pode estar Vazio ou a quantidade de letras é maior que 25 caracteres tente novamente");
            break;

        #UserStatus recebe o retorno da função UsuarioExiste aqui se o usuario existir um erro é emitido
        UserStatus = UsuarioExiste(Nome);
        if(UserStatus["UsuarioExiste"] == True):
            CleanTerminal()
            print("O nome de usuario deve ser unico")
            break;

        Senha = str(input("Digite sua Senha: "));
        if (VerifyLength(Senha, "Senha") == False):
            CleanTerminal();
            print("A senha deve ter mais de 4 caracteres e não pode estar vazia");
            break;
        
        Rua = str(input("Digite o nome da rua: "));
        NumeroCasa = str(input("Numero da casa: "));
        Bairro = str(input("Bairro: "));
        Cep = str(input("CEP: "));

        Endereço = {"Rua": Rua, "Numero_Da_Casa": NumeroCasa, "Bairro": Bairro, "Cep": Cep};

        userList.append({"Nome": Nome, "Senha": Senha, "Endereço": Endereço});
        CleanTerminal();
        print("Usuario cadstrado com sucesso");
        break;


def Consultar(EditOrConsult):
    print("+=+=+=++=+=ESCOLA ASSIS - LOGIN=+=+=++=+=+=");
    UserName = str(input("Digite o Nome de Usuario cadastrado: "));
    HasUser = False;
    Index = 0;
    UserGotPermission = False;

    #UserStatus recebe o retorno da função UsuarioExiste aqui se o usuario existir um erro é emitido
    #Essa variavel tem o mesmo nome nessa função e na função de cadastro ambas tem o mesmo objetivo
    UserStatus = UsuarioExiste(UserName);
    if(UserStatus["UsuarioExiste"] != False):
        HasUser = True;
        Index = UserStatus["index"];

    
    
    
    
    
    #a funça editar esta pulando a etapa de verficação de senha 






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
            print("Endereço: ", userList[Index]["Endereço"]);


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
                    if(len(NewUserPass) == 0 or len(NewUserPass) <= 4):
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
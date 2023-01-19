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
    #objetivo dessa função é verficar se o Nome de usuario existe na lista
    #essa função serve de apoio para a função de login
    DadosUteis = {};

    #essa função é usado para cadastro e consulta
    for index in range(len(userList)):
        if(userList[index]["Nome"] == UserName):
            DadosUteis = {"UsuarioExiste":  True, "index": index};
            return DadosUteis;
        else:
            return False;
    DadosUteis = {};


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

        #verifica se existe algum usuario cadastrado
        if(not len(userList) == 0):
            UserStatus = UsuarioExiste(Nome);
            if(UserStatus != False):
                CleanTerminal()
                print("Nome de usuario ja cadastrado")
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



def Login():
    print("+=+=+=++=+=ESCOLA ASSIS - LOGIN=+=+=++=+=+=");

    while True:
        UserName = str(input("Digite o Nome de Usuario cadastrado: "));
        UserStatus = UsuarioExiste(UserName);
    
        if(UserStatus == False):
            CleanTerminal()
            break;
    
        Pass = str(input("Digite a senha: "));
        if(Pass == userList[UserStatus["index"]]["Senha"]):
            return UserStatus;
        else:
            print("Senha Incorreta");
            CleanTerminal()
            break;

    CleanTerminal();
    print("usuario nao encontrado");
    return False;


def Consultar():
    UserExist = Login();
    while UserExist:
        Index = UserExist["index"];
        CleanTerminal();
        print("Nome: ", userList[Index]["Nome"]);
        print("Senha: ", userList[Index]["Senha"]);
        print("Endereço: ", userList[Index]["Endereço"]);
        break;

def Edit():
    #a função Consultar vai retornar um boolean para saber se o usuario tem permissão para editar
    UserStatus = Login();

    if(UserStatus != False):
        CleanTerminal();
        PainelEditar();
        operacao = int(input(">> "));
        
        while True:

            match operacao:

                case 1:
                    NewUserName = str(input("Digite o novo nome De usuario: "));
                    ActualUserName = userList[UserStatus["index"]]["Nome"];

                    if(ActualUserName == NewUserName):
                        print("O Novo nome de usuario deve ser diferente do Atual");
                        break;

                    if(not VerifyLength(NewUserName, "UserName")): #tratamento caso input estaja vazio
                        print("O nome de usuario não pode estar vazio e nao pode ser maior que 25 caracteres");
                         
                    # se todas as condições forem atendidas o Nome de usuario sera alterado
                    else:
                        userList[UserStatus["index"]]["Nome"] = NewUserName;
                        CleanTerminal();
                        print("alterado com sucesso");
                        break;            

                case 2:
                    NewUserPass = str(input("Digite a nova Senha: "));
                    ActualUserPass = userList[UserStatus["index"]]["Senha"];

                    if(ActualUserPass == NewUserPass):
                        CleanTerminal();
                        print("A nova senha não pode ser igual a senha atual.");

                    if(not VerifyLength(NewUserPass, "Senha")):
                        print("A senha deve ser maior que 4 digitos");
                    
                    # se todas as condições forem atendidas a senha sera alterada
                    else: 
                        userList[UserStatus["index"]]["Senha"] = NewUserPass;
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
            Consultar();
        case 3:
            Edit();
        case 4:
            break;
        case _:
            CleanTerminal();
            print("Operação invalida");
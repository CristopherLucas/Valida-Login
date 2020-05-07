nome = 'logins.txt'

def ArquivoExiste():
    """[Ele verifica se o arquivo existe]

    Returns:
        [bool] -- [Se o arquivo não existir, ele cria um e retorna o valor True]
    """    
    try:
        a = open(nome)
        a.close()
    except:
        open(nome, 'xt')
    else:
        return True


def jaCadastrado():
    """[Ele verifica se já se tem algum login cadastrado]

    Returns:
        [bool] -- [Se tiver algum usuario cadastrado ele retorna True, se não ele retorna False]
    """    
    try:
        a = open(nome, 'r')
    except:
        print('Erro.')
    else:
        if a.read() == '':
            a.close()
            return False
        else:
            return True


def novoCadastro():
    """[Ele cadastra um novo usuario]
    """    
    try:
        a = open(nome, 'w')
    except:
        print('Erro')
    else:
        try:
            print(f'{"Novo Cadastro":-^40}')
            usuario = str(input('Login: '))
            senha = int(input('Senha: '))
            a.write(f'{usuario};{senha}')
            a.close()
        except:
            print('Erro.')
        else:
            print('Novo cadastro efeituado com sucesso.')


def login():
    """[Ele faz o sistema de login do programa]
    """    
    try:
        print(f'{"Bem vindo de volta!":-^40}')
        usuario2 = str(input('Login: '))
        senha2 = int(input('Senha: '))
        validaLogin(usuario2, senha2)
    except:
        print('Erro.')
    else:
        pass


def validaLogin(login, senha):
    """[Ele valida o login]

    Arguments:
        login {[param]} -- [O nome de usuario para login]
        senha {[param]} -- [A senha para login]
    """    
    try:   
        a = open(nome)
    except:
        print('Houve um erro.')
    else:
        for c in a:
            b = c.split(';')
            if b[0] == login and int(b[1]) == senha:
                print('Login válido.')
            else:
                print('Login inválido')         

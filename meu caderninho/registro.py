from colorama import init, Fore, Back
init()

def verificador(a,b):
    if a in b:
        return a
    else:
        return False


def login_menu():
    login = int(input('''
Escolha:
1 - Login
2 - Registrar-se
3 - Encerrar
>>>>>>>>>>>>>>  '''))

    if login == 1:
        executando = login_executar()
        return executando
        print("Iniciando o menu...")

    elif login == 2:
        cpf = int(input("Digite seu cpf: "))
        senha = input("Crie sua senha: ")
        register(cpf,senha)
        executando = login_menu()
        return executando
    elif login == 3:
            executando = encerrar()
            if executando == False:
                executando = login_menu()
                return executando

                
    else:
        print("entrada inválida, digite novamente.\n")
        login_menu()


def encerrar():
    retomando = int(input(f'''
Você tem certeza?
digite 1 - {Fore.GREEN}sim{Fore.RESET}
digite 2 - {Fore.RED}não{Fore.RESET}\n'''))
    res = verificador(retomando,[1,2])    
    if res == retomando:
        if retomando == 1:
            print(f"{Fore.WHITE}{Back.RED}encerrando o sistema{Back.RESET}{Fore.RESET}")
            iniciar = input(f'caso queira iniciar novamente, digite a palavra {Fore.GREEN}iniciar{Fore.RESET}\n').strip().lower()
            if iniciar == "iniciar":
                executando = False
                return executando
            else:
                while iniciar != "iniciar":
                    print("entrada inválida, digite novamente")
                    iniciar = input(f'caso queira iniciar novamente, digite a palavra {Fore.GREEN}iniciar{Fore.RESET}\n').strip().lower()
                    if iniciar == "iniciar":
                        executando = False
                        return executando

        elif retomando == 2:
            print('iniciando o programa novamente...')
            executando = False
            return executando
    else:
        print("entrada inválida, digite novamente")
        encerrar()          




def register(cpf,senha):
    with open('login_admin.txt','a') as registros:
        print("Conta criada com sucesso!")
        registros.write(f'{cpf}, {senha}\n')
        #login_menu()


def login_read ():
    with open ('login_admin.txt','r') as registros:
        linhas = registros.readlines() 
        lista_login = []
        for linha in linhas: 
            auxiliar = linha.strip().split(',')
            login = {'cpf': int(auxiliar[0]), 'senha': auxiliar[1].strip()}
            lista_login.append(login)
        return lista_login



def login_search(lista_login):
    cpf = int(input('''Digite seu cpf: '''))
    contadora = 0
    cpf_encontrado = False
    for login in lista_login:
        if login['cpf'] == cpf:
            cpf_encontrado = True
            return contadora
        else:
            contadora += 1
    if cpf_encontrado == False:
        print('cpf errado.')
        return -1



def login_search_senha(lista_login,login_pesquisa):
    senha = input('''Digite sua senha: ''')
    senha_encontrada = False
    if lista_login[login_pesquisa]['senha'] == str(senha):
        senha_encontrada = True
        return 1
    else:
        senha_encontrada == False
        print('senha errada.')
        return -1
            

def alterar():
    login_lista = login_read()
    login_pesquisa = login_search(login_lista)
    if login_pesquisa != -1:
            login_lista[login_pesquisa]['senha'] = str(input('Digite sua nova senha: '))
            print("Senha alterada com sucesso!")
            #login_menu()
    else:
        while login_pesquisa == -1:
            cpf = int(input("Digite novamente seu cpf: "))
            login_pesquisa = login_search(cpf,login_lista)
            if login_pesquisa != -1:
                login_lista[login_pesquisa]['senha'] = str(input('Digite sua nova senha: '))
                print("Senha alterada com sucesso!")
                #login_menu()

    with open ('login_admin.txt','w') as registros:
        for login in login_lista:
           linha = f"{login['cpf']}, {login['senha']}\n"
           registros.write(linha)



def login_executar():
    lista_login = login_read()
    entrada = int(input('''
1 - Entrar
2 - Alterar senha
3 - Voltar
>>>>>>>>>>>>> '''))
    if entrada == 1:
        login_pesquisa = login_search(lista_login)
        if login_pesquisa != -1:
            login_pesquisa_senha = login_search_senha(lista_login,login_pesquisa)
            if login_pesquisa_senha != -1:
                return True
            else:
                while login_pesquisa_senha == -1:
                    login_pesquisa_senha = login_search_senha(lista_login,login_pesquisa)
                    if login_pesquisa_senha != -1:
                        return True
                    
        else:
            while login_pesquisa == -1:
                login_pesquisa = login_search(lista_login)
                if login_pesquisa != -1:
                    login_pesquisa_senha = login_search_senha(lista_login,login_pesquisa)
                    if login_pesquisa_senha != -1:
                        return True
                    else:
                        while login_pesquisa_senha == -1:
                            login_pesquisa_senha = login_search_senha(lista_login,login_pesquisa)
                            if login_pesquisa_senha != -1:
                                return True
                    
    elif entrada == 2:
        alterar()
        executando = login_executar()
        return executando


'''def login_executar():
    lista_login = login_read()
    entrada = int(input(
1 - Entrar
2 - Alterar senha
3 - Voltar
>>>>>>>>>>>>> ))
    if entrada == 1:
        cpf = int(input(Digite seu cpf: ))
        login_pesquisa = login_search(cpf,lista_login)
        if login_pesquisa != -1:
            senha = input("Digite sua senha: ")
            login_senha = login_search(senha,lista_login)
            if login_senha != -1:
                executando = True
                return executando
                print("Iniciando o menu...")
            else:
                while login_senha == -1:
                    senha = input("Digite novamente sua senha: ")
                    login_senha = login_search(senha,lista_login)
                    if login_senha != -1:
                        executando = True
                        return executando

        else:
            while login_pesquisa == -1:
                cpf = int(input("Digite novamente seu cpf: "))
                login_pesquisa = login_search(cpf,lista_login)
                if login_pesquisa != -1:
                    senha = input("Digite sua senha: ")
                    login_senha = login_search(senha,lista_login)
                    if login_senha != -1:
                        executando = True
                        return executando
                        print("Iniciando o menu...")
                    else:
                        while login_senha == -1:
                            senha = input("Digite novamente sua senha: ")
                            login_senha = login_search(senha,lista_login)
                            if login_senha != -1:
                                executando = True
                                return executando
    elif entrada == 2:
        alterar()'''


    
'''lista_login = login_read()
print(lista_login)
executando = False
while executando == False: 
    login = int(input(
#Escolha:
#1 - Login
#2 - Registrar-se
#3 - Encerrar
#>>>>>>>>>>>>>>  ))

    if login == 1:
        login_executar()
        print("Iniciando o menu...")

    elif login == 2:
        cpf = int(input("Digite seu cpf"))
        senha = input("Crie sua senha")
        register(cpf,senha)
    elif login == 3:
        encerrando()
    else:
        print("entrada inválida, digite novamente.\n")'''



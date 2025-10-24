from colorama import init, Fore, Back
init()




def verificador(a,b):
    if a in b:
        return a
    else:
        return False


def create(nome,divida,cpf):
    with open('arquivo_devedores.txt','a') as devedores:
        devedores.write(f'{nome}, {divida}, {cpf}\n') #aqui eu transformei o que será um dicionário em uma string dentro do arquivo txt 



def read ():
    with open('arquivo_devedores.txt','r') as devedores:
        linhas = devedores.readlines()
        linhas_formatadas = [] 
        lista_devedores = []
        for linha in linhas:
            texto_processado = linha.strip()
            if texto_processado:
                linhas_formatadas.append(texto_processado)
        
        if linhas_formatadas == None:
            return lista_devedores
        else:   
            for linha in linhas_formatadas: 
                auxiliar = linha.strip().split(', ')  
                devedor = {'nome': auxiliar[0],'divida':float(auxiliar[1]),'cpf':auxiliar[2]}
                lista_devedores.append(devedor)
            return lista_devedores
        

     #else:
      #      print(Isso não é possível, pois não existem devedores registrados no momento.)
      #      executando = menu_main()
       #     return executando
            








            
def search_by_name(lista_devedores): #essa função vai ser usada em update e delete para retornar o índice da lista que se encontra um nome caso ela o contenha
    nome_procurando = input('\ndeclare o cpf a ser encontrado: ')
    contadora = 0
    nome_encontrado= False
    for devedor in lista_devedores:
        if devedor['cpf'] == nome_procurando:
            nome_encontrado = True
            return contadora #estou considerando que só exista uma pessoa por nome, pois o return vai encerrar o laço(-_-)
        else:
            contadora += 1
    if nome_encontrado == False: #se for falso é porque o vetor foi percorrido e a string não foi encontrada
        print(f'{Fore.RED}cpf não encontrado{Fore.RESET}')
        return -1




        

def update():
    lista_devedores = read() #usei a função read para transformar o arquivo em uma lista de dicionários
    menu_update = int(input('''\n
o que deve ser atualizado?
digite 0- sair
digite 1- corrijir nome
digite 2- alterar divida
digite 3- corrijiar cpf
>>>>>> '''))
    if menu_update == 0:
        print(f"\n{Fore.WHITE}{Back.RED}Voltando para o menu principal...{Back.RESET}{Fore.RESET}\n") #saindo com estilo
        time.sleep(2)
    
    elif len(lista_devedores) != 0:
        if menu_update == 1:
            indice_encontrado = search_by_name(lista_devedores)
            if indice_encontrado != -1:
                lista_devedores[indice_encontrado]['nome'] = input('digite o nome corretamente: ')
            else:
                update()

               
        elif menu_update == 2:
            indice_encontrado = search_by_name(lista_devedores)
            if indice_encontrado != -1:
                mudar = int(input('''
quer aumentar ou diminuir a divida?
digite 1- subtrair divida
digite 2- aumentar divida
igite 3- voltar
>>>>>>>>>> '''))
                if mudar in [1,2,3]:
                    if mudar == 1:
                        pagamento = float(input('declare o valor pago: '))
                        lista_devedores[indice_encontrado]['divida'] = lista_devedores[indice_encontrado]['divida'] - pagamento
                        update()
                    elif mudar == 2:
                        divida_maior = float(input('declare o acréscimo da divida: '))
                        lista_devedores[indice_encontrado]['divida'] = lista_devedores[indice_encontrado]['divida'] + divida_maior
                        update()
                    
                    elif mudar == 3:
                        update()
                else:
                    while mudar not in [1,2,3]:
                        print(f"{Fore.RED}entrada inválida, digite novamente{Fore.RESET}\n")
                        mudar = int(input('''
quer aumentar ou diminuir a divida?
digite 1- subtrair divida
digite 2- aumentar divida
digite 3- voltar
>>>>>>>>>> '''))
                    if mudar == 1:
                        pagamento = float(input('declare o valor pago: '))
                        lista_devedores[indice_encontrado]['divida'] = lista_devedores[indice_encontrado]['divida'] - pagamento
                        update()
                    elif mudar == 2:
                        divida_maior = float(input('declare o acréscimo da divida: '))
                        lista_devedores[indice_encontrado]['divida'] = lista_devedores[indice_encontrado]['divida'] + divida_maior
                        update()
                    elif mudar == 3:
                        update()
                                      
            else:
                update()
                                              
            
            
        elif menu_update == 3:
            indice_encontrado = search_by_name(lista_devedores)
            if indice_encontrado != -1:
                lista_devedores[indice_encontrado]['cpf'] = input('digite o novo cpf: ')
                update()
            else:
                while indice_encontrado == -1:
                    indice_encontrado = search_by_name(lista_devedores)
                    if indice_encontrado != -1:
                        lista_devedores[indice_encontrado]['cpf'] = input('digite o novo: ')
                        update()

    
    else:
        print(f'{Fore.RED}entrada inválida{Fore.RESET}')
        update()
          
    with open('arquivo_devedores.txt','w') as arquivo:
        for devedor in lista_devedores:
           linha = f"{devedor['nome']}, {devedor['divida']}, {devedor['cpf']}\n"
           arquivo.write(linha)








           
            
def delete():
    lista_devedores = read()
    menu_delete = int(input('''
deseja mesmo perdoar alguém?[
digite 0- não perdoar dívida (erro de digitação)
digite 1- perdoar dívida (finalmente pagou)
>>>>>> '''))
    if menu_delete == 0:
        print(f"\n{Fore.WHITE}{Back.RED}Voltando para o menu principal...{Back.RESET}{Fore.RESET}\n") #saindo com estilo
        time.sleep(2)
    

    elif menu_delete == 1:
        if len(lista_devedores) != 0:
            indice_lista = search_by_name(lista_devedores)
            lista_devedores.pop(indice_lista)
        else:
            print("Não existe nenhuma conta cadastrada. Por favor, cadastre sua conta.")
            delete()

    else:
        print('entrada inválida, digite novamente\n')
        delete()     

    with open('arquivo_devedores.txt','w') as devedores:
        for devedor in lista_devedores:
            linha = f"{devedor['nome']}, {devedor['divida']}, {devedor['cpf']}\n"
            devedores.write(linha)
            



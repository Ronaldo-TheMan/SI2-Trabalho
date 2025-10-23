from crud import create,delete,read,update
from registro import login_menu, login_read, login_search, login_search_senha, login_executar, alterar, register, encerrar
from colorama import init, Fore, Back
init()

def verificador(a,b):
    if a in b:
        return a
    else:
        return False

def menu_main():
   entrada_menu = int(input('''
declare a funcionalidade a ser executada pelo sistema
digite 0- sair
digite 1- adicionar devedor
digite 2- alterar nome do devedor ou alterar divida
digite 3- perdoar devedor
digite 4- mostrar todos os devedores
>>>>>>>>>>>>>>>>>>>>>>>>>>>>> '''))
   menu_verificado = verificador(entrada_menu, [0,1,2,3,4])
   if menu_verificado == entrada_menu:
      return entrada_menu
   else:
      print("\nentrada inválida, digite novamente\n")
      digite = menu_main()
      return digite


def retomar():
    retomando = int(input(f'''
Você tem certeza?
digite 1 - {Fore.GREEN}sim{Fore.RESET}
digite 2 - {Fore.RED}não{Fore.RESET}\n'''))


    res = verificador(retomando,[1,2])    
    if res == retomando:
        if retomando == 1:
            print("saindo do menu...")
            executando = False
            return executando
                
        elif retomando == 2:
            print('voltando para o menu')
            executando = True
            return executando
    else:
        print("entrada inválida, digite novamente")
        retomar()


    
   #
   #eu posso somente colocar return menu() pois o menu() que será retornado como valor
   # e armazenado novamente na entrada_menu ue está sendo chamada no while
   # pois é como se eu estivesse atribuindo novamente o menu() a entrada_menu
   # se eu só chamar novamente a função, ela será executada naquela parte
   # e não retornará nenhum valor em nenhuma variavel local
   # portanto, colocando no else somente menu(), se tornará algo somente local, embora printe novamente o menu
   # sendo assim, ou eu retorno a função como valor, return menu(), pois ira atribuir e armazenar novamente a função menu() na variavel do laço
   # ou, posso atribuir localmente o resultado da outra chamada do menu() dentro da função e retornar o resultado, e aí sim o novo retorno será atribuido
   # pois como é algo local, eu preciso retornar o valor, pois é como se ele fosse se abrindo até ir se fechando.
   #
   






#ÁREA DO PROGRAMA



#LOGIN

    









#MENU

executando = False
executando = login_menu()
while executando == True:
    entrada_menu = menu_main()
    if entrada_menu == 0:
        executando = retomar()
        if executando == False:
            executando = login_menu()       

    elif entrada_menu == 1:
        nome = input('declare o nome do devedor: ')
        divida = float(input('declare a quantia devida: '))
        cpf = int(input('declare o cpf do devedor sem caracteres especiais: '))
        create(nome,divida,cpf)

    elif entrada_menu == 2:
        update()

    elif entrada_menu == 3:
        delete()

    elif entrada_menu == 4:
        lista_devedores = read()
        for devedor in lista_devedores:
            print(devedor)
    else:
        print('entrada inválida')










       

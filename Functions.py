from multiprocessing.connection import wait
import os
import matplotlib.pyplot as grafico
from time import sleep


def ValidaAcesso(pUsuario, pSenha):
    os.system('cls')
    tentativas = 4
    while ((pUsuario != 'usuario') or (pSenha != 'senha')):
        tentativas = tentativas - 1 
        print ('Acesso invalido    │    ' + str(tentativas) + ' tentativas restantes')
        sleep(1)
        os.system('cls')
        pUsuario = input('Usuario: ')
        pSenha = input('Senha: ')
        if (tentativas == 1):
            print('Usuario bloqueado por tentativas')   
            sleep(0.5)
            os.system('cls')
            break   
    if (tentativas > 1) :
        sleep(0.5)
        os.system('cls')
        MenuPrincipal()

def MenuPrincipal():
    opcao = 0
    Varmes = []
    mes = 0
    VarVenda = []
    Venda = 0
    novoMes = 0
    
    
    while (opcao != 6):
        os.system('cls')
        print('+' .ljust(41, '-') + '+')
        print('│ Sistema Financeiro - Controle de Vendas│') 
        print('+' .ljust(41, '-') + '+')
        print('│ 1- Cadastrar          2- Alterar       │')  
        print('│ 3- Excluir            4- Visualizar    │')
        print('│ 5- Mostrar gráfico    6- Encerrar      │') 
        print(('+' .ljust(41, '-') + '+'))
        opcao = int(input('Opção: '))
        if (opcao == 1):
            sleep(0.5)
            os.system('cls')
            mes = input('Para qual mês deseja cadastrar a venda? ')
            if (mes in Varmes):
                print('Já possui ' + mes + ' no sistema')
                sleep(1.25)
            else:
                Venda = input('Informe o valor da venda: ')
                Varmes.append(mes)
                VarVenda.append(Venda)
                print(mes + " cadastrado")
                sleep(1.25)
                                
        elif (opcao == 2):
            sleep(0.5)
            os.system('cls')
            if( mes == 0):
                print('Nenhum mês declarado')
            else:
                novoMes = input('Mês que deseja alterar: ')
                if (novoMes in Varmes):
                    for x in range(0,len(Varmes)):
                        if (Varmes[x] == novoMes):
                            VarVenda.pop(x)
                            VarVenda.insert(x, input('Novo valor:'))
                            os.system('cls')
                            print('Mês alterado')
                            sleep(1.25)
                            
                            break
                else:
                    print('Mês não encontrado')
                    sleep(1.25)
                        

        elif (opcao == 3):
            sleep(0.5)
            os.system('cls')
            mes = input('Qual mês deseja excluir? ')
            if (len(Varmes) == 0 ):
                print('Nenhum mês cadastrado')
                sleep(1.25)
            elif (mes in Varmes):
                for x in range(0,(len(Varmes))):
                    if (mes == Varmes[x]):
                        Varmes.pop(x)
                        VarVenda.pop(x)
                        print('Venda excluida')
                        sleep(1.25)
                        break
            else:
                print('Mês não cadastrado')
                sleep(1.25)

        elif (opcao == 4):
            os.system('cls')
            espera = 0
            while(espera != 1):
                if (len(Varmes) == 0 ):
                    print('Nenhum mês cadastrado')
                    sleep(3)
                else:
                    for x in range(0,(len(Varmes))):
                        print(Varmes[x] + '   ' + VarVenda[x])
                    espera = int(input('Digite 1 para sair: '))

        elif (opcao == 5):
            
            
            grafico.title('Gráfico de Vendas')
            grafico.xlabel('Mês')
            grafico.ylabel('Venda')     
            VarVenda= [float(x) for x in VarVenda]      
            grafico.plot(Varmes,VarVenda)

            grafico.show()
        
        elif (opcao == 6):
            sleep(0.5)
            os.system('cls')
            print('Sistema encerrado pelo usuario')
            sleep(1)
            os.system('cls')
            break
        
    if (opcao < 1 or opcao > 6):
        print('Opção invalida')
       


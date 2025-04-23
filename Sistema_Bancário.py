import time

opcao = 0
dinheiro = 0

while opcao!=4:
        opcao=int(input('\nO que deseja fazer?'
                    '\n1-Fazer depósito'
                    '\n2-Sacar dinheiro'
                    '\n3-Ver o saldo'
                    '\n4-Encerrar operação -----> '))
        if opcao==1:
           senha = input('\nInsira sua senha: ')
           print('Processando...')
           time.sleep(3)
           if senha == "python123":
             ad=float(input('\nInsira valor: '))
             dinheiro=dinheiro+ad

             print('Valor inserido ;)')
           else:
            print('\nSenha incorreta :(')

        elif opcao==2:
            senha = input('\nInsira sua senha: ')
            print('Processando...')
            time.sleep(3)
            if senha == "python123":
              ret=float(input('\nValor a retirar: '))
              if dinheiro<ret:
               print('Impossível sacar esse valor, verifique seu saldo na opção 3')
              else:
               dinheiro=dinheiro-ret
            else:
             print('Senha incorreta :(')

        elif opcao==3:
            senha = input('\nInsira sua senha: ')
            print('Processando...')
            time.sleep(3)
            if senha == "python123":
              print(f'\nSeu saldo é {dinheiro}')
            else:
                print('Senha incorreta :(')

        elif opcao == 4:
          print('\nTenha um ótimo dia :)')

        else:
          print('\nOpção inválida, selecione as opções presentes na tela')

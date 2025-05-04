from datetime import datetime

SENHA_CORRETA = "python123"

# Função que inicia o sistema bancário
def sistema_bancario():
    opcao = 0
    dinheiro = 0
    extrato = []
    transacoes_hoje = 0
    data_atual = datetime.now().date()

    while opcao != 4:
        agora = datetime.now()
        data_hoje = agora.date()

        # Se mudou o dia, resetamos o contador
        if data_hoje != data_atual:
            transacoes_hoje = 0
            data_atual = data_hoje

        print(f'\nTransações realizadas hoje: {transacoes_hoje}/10')
        opcao = int(input('\nO que deseja fazer?'
                          '\n1 - Fazer depósito'
                          '\n2 - Sacar dinheiro'
                          '\n3 - Ver extrato'
                          '\n4 - Encerrar operação -----> '))

        if opcao in [1, 2] and transacoes_hoje >= 10:
            print("Você excedeu o número de transações permitidas para hoje. Tente novamente amanhã.")
            continue

        if opcao == 1:
            ad = float(input('\nInsira o valor do depósito: '))
            if ad > 0:
                dinheiro += ad
                horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                extrato.append(f'[{horario}] Depósito: +R$ {ad:.2f}')
                transacoes_hoje += 1
                print('Depósito realizado com sucesso ;)')
            else:
                print('Valor inválido! O depósito deve ser positivo.')

        elif opcao == 2:
            ret = float(input('\nValor a sacar: '))
            if ret > dinheiro:
                print('Saldo insuficiente para realizar o saque.')
            elif ret <= 0:
                print('Valor inválido! O saque deve ser positivo.')
            else:
                dinheiro -= ret
                horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                extrato.append(f'[{horario}] Saque: -R$ {ret:.2f}')
                transacoes_hoje += 1
                print('Saque realizado com sucesso!')

        elif opcao == 3:
            print('\n--- Extrato ---')
            if not extrato:
                print('Nenhuma movimentação registrada.')
            else:
                for movimento in extrato:
                    print(movimento)
            print(f'\nSaldo atual: R$ {dinheiro:.2f}')

        elif opcao == 4:
            print('\nTenha um ótimo dia :)')

        else:
            print('\nOpção inválida, selecione as opções presentes na tela')

# Função para autenticação inicial
def autenticar():
    senha_inicial = input("Insira a senha para iniciar o sistema bancário: ")
    if senha_inicial == SENHA_CORRETA:
        sistema_bancario()
    else:
        print("Senha incorreta. Acesso negado.")

# Inicia o programa
autenticar()

from datetime import datetime

SENHA_CORRETA = "python123"

usuarios = []
contas = []
contador_conta = 1  # Inicializa o número da conta corrente

def criar_usuario():
    print("\n--- Cadastro de Usuário ---")
    cpf = input("Informe o CPF (somente números): ").strip()

    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("CPF já cadastrado! Usuário não pode ser duplicado.")
        return

    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
    endereco = input("Endereço (logradouro/bairro/Cidade/sigla estado): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("Usuário cadastrado com sucesso!")

def criar_conta_corrente():
    global contador_conta
    print("\n--- Abertura de Conta Corrente ---")
    cpf = input("Informe o CPF do titular da conta: ").strip()

    usuario = next((usuario for usuario in usuarios if usuario['cpf'] == cpf), None)

    if usuario:
        conta = {
            "agencia": "0001",
            "numero_conta": contador_conta,
            "usuario": usuario
        }
        contas.append(conta)
        print(f"Conta criada com sucesso! Número da conta: {contador_conta}")
        contador_conta += 1
    else:
        print("Usuário não encontrado. Cadastre o usuário antes de criar a conta.")

def realizar_deposito(dinheiro, extrato):
    ad = float(input('\nInsira o valor do depósito: '))
    if ad > 0:
        dinheiro += ad
        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato.append(f'[{horario}] Depósito: +R$ {ad:.2f}')
        print('Depósito realizado com sucesso ;)')
        return dinheiro, extrato, True
    else:
        print('Valor inválido! O depósito deve ser positivo.')
        return dinheiro, extrato, False

def realizar_saque(dinheiro, extrato):
    ret = float(input('\nValor a sacar: '))
    if ret > dinheiro:
        print('Saldo insuficiente para realizar o saque.')
        return dinheiro, extrato, False
    elif ret <= 0:
        print('Valor inválido! O saque deve ser positivo.')
        return dinheiro, extrato, False
    else:
        dinheiro -= ret
        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato.append(f'[{horario}] Saque: -R$ {ret:.2f}')
        print('Saque realizado com sucesso!')
        return dinheiro, extrato, True

def exibir_extrato(extrato, dinheiro):
    print('\n--- Extrato ---')
    if not extrato:
        print('Nenhuma movimentação registrada.')
    else:
        for movimento in extrato:
            print(movimento)
    print(f'\nSaldo atual: R$ {dinheiro:.2f}')

def sistema_bancario():
    opcao = 0
    dinheiro = 0
    extrato = []
    transacoes_hoje = 0
    data_atual = datetime.now().date()

    while opcao != 7:
        agora = datetime.now()
        data_hoje = agora.date()

        if data_hoje != data_atual:
            transacoes_hoje = 0
            data_atual = data_hoje

        print(f'\nTransações realizadas hoje: {transacoes_hoje}/10')
        try:
            opcao = int(input('''
O que deseja fazer?
1 - Fazer depósito
2 - Sacar dinheiro
3 - Ver extrato
4 - Criar usuário
5 - Criar conta corrente
6 - Listar contas
7 - Encerrar operação -----> '''))
        except ValueError:
            print('\nEntrada inválida. Por favor, insira um número.')
            continue

        if opcao in [1, 2] and transacoes_hoje >= 10:
            print("Você excedeu o número de transações permitidas para hoje. Tente novamente amanhã.")
            continue

        if opcao == 1:
            dinheiro, extrato, sucesso = realizar_deposito(dinheiro, extrato)
            if sucesso:
                transacoes_hoje += 1

        elif opcao == 2:
            dinheiro, extrato, sucesso = realizar_saque(dinheiro, extrato)
            if sucesso:
                transacoes_hoje += 1

        elif opcao == 3:
            exibir_extrato(extrato, dinheiro)

        elif opcao == 4:
            criar_usuario()

        elif opcao == 5:
            criar_conta_corrente()

        elif opcao == 6:
            print("\n--- Contas Cadastradas ---")
            if not contas:
                print("Nenhuma conta criada ainda.")
            else:
                for conta in contas:
                    print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Titular: {conta['usuario']['nome']}")

        elif opcao == 7:
            print('\nTenha um ótimo dia :)')

        else:
            print('\nOpção inválida, selecione as opções presentes na tela')

def autenticar():
    senha_inicial = input("Insira a senha para iniciar o sistema bancário: ")
    if senha_inicial == SENHA_CORRETA:
        sistema_bancario()
    else:
        print("Senha incorreta. Acesso negado.")

# Inicia o programa
autenticar()

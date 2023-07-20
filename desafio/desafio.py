menu = '''
========== MENU ==========
[D] - Depositar
[S] - Sacar
[E] - Extrato
[N] - Operações realizadas
[F] - Sair
==========================
==> '''
saldo = 0
limite_saque_dia = 500
limite_deposito_dia = 1500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3
numero_de_depositos = 0
LIMITE_DE_DEPOSITOS = 5

while True:

    opcao = input(menu)

    if opcao == "d" or opcao == "D":
        print(" Deposito ".center(40, "="))
        valor = float(input("Insira o valor a ser depositado: R$"))

        excedeu_limite_deposito = valor > limite_deposito_dia 
        excedeu_numero_deposito = numero_de_depositos >= LIMITE_DE_DEPOSITOS

        if excedeu_limite_deposito:
            print(f"Operação falhou! O valor do deposito excede o limite: R${limite_deposito_dia}")
        elif excedeu_numero_deposito:
            print("Operação falhou! Número máximo de depositos excedido.")
            print(f"Numero de operações realizada: {numero_de_depositos}")
            print(F"Limite de Depositos: {LIMITE_DE_DEPOSITOS}")
        elif valor > 0:
            saldo += valor
            numero_de_depositos += 1
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print(f"Valor depositado com sucesso: R${valor: .2f}")
            print(f"Numero de operações realizada: {numero_de_depositos}")
            
        else:
            print("valor invalido, insira um valor valido.")

    elif opcao == "s" or opcao == "S":
        print(" Sacar ".center(56, "="))

        valor = float(input("Informe o valor do saque: R$"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite_saque_dia

        excedeu_saques = numero_de_saques >= LIMITE_DE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            print(f"Saldo atual: R${saldo}")

        elif excedeu_limite:
            print(f"Operação falhou! O valor do saque excede o limite: R${limite_saque_dia}")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
            print(f"Numero de operações realizada: {numero_de_saques}")
            print(F"Limite de saques: {LIMITE_DE_SAQUES}")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_de_saques += 1
            print(f"Valor sacado com sucesso: R${valor: .2f}")
            print(f"Numero de operações realizada: {numero_de_saques}")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e" or opcao == "E":
        print()
        print(" Extrato ".center(36, "="))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print("".center(36, "="))
        print(f"Saldo: R$ {saldo:.2f}")
        print("".center(36, "="))
        
    elif opcao == "n"or opcao == "N":
        print(" Operações realizadas ".center(36, "="))
        print(f"Operações de saque realizadas: {numero_de_saques}")
        print(f"Limite de saques diario: {LIMITE_DE_SAQUES}")
        print(f"Operações de deposito realizadas: {numero_de_depositos}")
        print(f"Limite de depositos diario: {LIMITE_DE_DEPOSITOS}")
        print("".center(36, "="))        
    elif opcao == "f" or opcao == "F":
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")

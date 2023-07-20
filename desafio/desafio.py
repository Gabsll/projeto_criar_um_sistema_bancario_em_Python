menu ='''
========== MENU ==========
[D] - Depositar
[S] - Sacar
[E] - Extrato
[F] - Sair
==========================
==> '''
saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d" or menu == "D":
        print(" Deposito ".center(40, "="))     
        valor = float(input("Insira o valor a ser depositado: R$"))   
        if valor > 0:
                saldo += valor
                print(f"Valor depositado com sucesso: R${valor: .2f}")
                extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("valor invalido, insira um valor valido.")
            
    elif opcao == "s" or menu == "S":
        print(" Sacar ".center(56, "="))
        
        valor = float(input("Informe o valor do saque: R$"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_de_saques >= LIMITE_DE_SAQUES
        
         
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            print(f"Saldo atual: R${saldo}")

        elif excedeu_limite:
            print(f"Operação falhou! O valor do saque excede o limite: R${limite}")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
            print(f"Numero de operaçoes realizada: {numero_de_saques}")
            print(F"Limite de saques: {LIMITE_DE_SAQUES}")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_de_saques += 1
            print(f"Valor sacado com sucesso: R${valor: .2f}")
            print(f"Numero de operaçoes realizada: {numero_de_saques}")
        else:
            print("Operação falhou! O valor informado é inválido.")   
    
    elif opcao == "e" or menu == "E":
        print()
        print(" Extrato ".center(36, "="))
        print("Não foram realizadas movimentações." if not extrato else extrato)  
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("".center(36, "="))
    elif opcao == "f" or menu == "F":
        break
    
    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")
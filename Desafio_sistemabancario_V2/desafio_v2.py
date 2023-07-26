import textwrap


def menu():
    menu = '''
=========== MENU ===========
[D]\tDepositar
[S]\tSacar
[E]\tExtrato
[NC]\tNova conta
[LC]\tLista contas
[NU]\tNovo usuário
============================
[F]\tSair
============================
==> '''

    return input(textwrap.dedent(menu))


def main():
    limite_saque_dia = 500
    numero_de_saques = 0
    LIMITE_DE_SAQUES = 3

    limite_deposito_dia = 1500
    numero_de_depositos = 0
    LIMITE_DE_DEPOSITOS = 5

    AGENCIA = "0001"

    saldo = 0
    extrato = ""

    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == "d" or opcao == "D":
            print(" Deposito ".center(40, "="))
            valor = float(input("Insira o valor a ser depositado: R$"))
            saldo, extrato = operacao_depositar(
                saldo, valor, extrato,
                numero_de_depositos=numero_de_depositos,
                LIMITE_DE_DEPOSITOS=LIMITE_DE_DEPOSITOS,
                limite_deposito_dia=limite_deposito_dia
            )
        elif opcao == "s" or opcao == "S":
            print(" Sacar ".center(56, "="))
            valor = float(input("Informe o valor do saque: R$"))
            saldo, extrato = operacao_sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite_saque_dia=limite_saque_dia,
                numero_de_saques=numero_de_saques,
                LIMITE_DE_SAQUES=LIMITE_DE_SAQUES

            )
        elif opcao == "e" or opcao == "E":
            operacao_extrato(saldo, extrato=extrato)
        elif opcao == "nu" or opcao == "NU" or opcao == "nU" or opcao == "Nu":
            criar_usuario(usuarios)
        elif opcao == "nc" or opcao == "NC" or opcao == "nC" or opcao == "Nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "LC" or opcao == "lc" or opcao == "Lc" or opcao == "lC":
            listar_contas(contas)
        elif opcao == "f" or opcao == "F":
            break
        else:
            print("Operação invalida, por favor selecione novamente a operação desejada.")


def operacao_depositar(saldo, valor, extrato, /, *, numero_de_depositos, LIMITE_DE_DEPOSITOS, limite_deposito_dia):

    excedeu_limite_deposito = valor > limite_deposito_dia
    excedeu_numero_deposito = numero_de_depositos >= LIMITE_DE_DEPOSITOS

    if excedeu_limite_deposito:
        print(
            f"Operação falhou! O valor do deposito excede o limite: R${limite_deposito_dia}")
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

    return saldo, extrato


def operacao_sacar(*, saldo, valor, extrato, limite_saque_dia, numero_de_saques, LIMITE_DE_SAQUES):

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite_saque_dia

    excedeu_saques = numero_de_saques >= LIMITE_DE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        print(f"Saldo atual: R${saldo}")

    elif excedeu_limite:
        print(
            f"Operação falhou! O valor do saque excede o limite: R${limite_saque_dia}")
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

    return saldo, extrato


def operacao_extrato(saldo, /, *, extrato):
    print()
    print(" Extrato ".center(36, "="))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print("".center(36, "="))
    print(f"Saldo: R$ {saldo:.2f}")
    print("".center(36, "="))


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n==== Já existe usuário com esse CPF! ====")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento,
                    "cpf": cpf, "endereco": endereco})

    print("=== Usuario, criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [
        usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n ==== Usuário nao econtrado, fluxo de criação de conta encerrado! ====")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


main()

def caixa_eletronico():
    banco_de_dados = {
        1234: {"usuário": "joão","senha":"1234","saldo": 1000.00},
        1235: {"usuário": "joão","senha":"1235","saldo": 1000.00}
    }

    tentativas = 3

    try:
        conta_usuario = int(input("Digite sua conta de 4 digitos: "))
        if verificao_conta(conta_usuario,banco_de_dados):
            # para cada conta
            for numero_conta in banco_de_dados:
                # verificação se a conta do usuário é a mesma conta
                if conta_usuario == numero_conta:
                    # verificando números de tentativas
                    while tentativas > 0:
                        senha_usuario = input("Digite sua senha de 4 digitos: ").strip()
                        # verificação senha do usuário igual a senha da conta
                        if banco_de_dados[numero_conta]['senha'] == senha_usuario:
                            print("Entrou na conta com sucesso.")
                            escolhas(banco_de_dados,numero_conta)
                            return
                        else:
                            tentativas -= 1
                            print(f"Senha incorreta. Tentativas restantes: {tentativas}")
                    print("Conta bloqueada. Tente mais tarde.")
        else:
            print("Essa conta não existe.")
    except ValueError:
        print("Só é permitido digitos")
    
        
def verificao_conta (conta_usuario,banco_de_dados):
    # verificação se a conta do usuário está em contas
    return conta_usuario in banco_de_dados

def escolhas(contas,conta):
    while True:
        escolha = input("1 - Consultar saldo.\n2 - Depositar.\n3 - Sacar.\n4 - Sair\nOpção: ").strip()
        if escolha == "1":
            print(f"Seu saldo é: R$ {contas[conta]['saldo']}")
        elif escolha == "2":
            try:
                deposito = float(input("Quanto deseja depositar? "))
                contas[conta]['saldo'] += deposito
                print("Deposito feito com sucesso")
            except ValueError:
                print("Valor inválido")
        elif escolha == "3":
            try:
                saque = float(input("Quanto deseja sacar? "))
                if saque > contas[conta]['saldo']:
                    print("Saldo insuficiente")
                else:
                    contas[conta]['saldo'] -= saque
                    print("Saque feito com sucesso")
            except ValueError:
                print("Valor inválido")
        elif escolha == "4":
            print("Obrigado. Volte sempre!")
            break
        else:
            print("Essa escolha não existe. Tente novamente!")

caixa_eletronico()
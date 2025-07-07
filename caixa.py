'''
Um programa que simula o funcionamento básico de um caixa eletrônico, permitindo que o usuário:

Acesse uma conta com senha (opcional no começo);

Veja o saldo atual;

Faça depósitos;

Realize saques;

Encerre a sessão.
'''

def caixa_eletronico():
    conta_usuario = 1235 #input("Digite sua conta de 4 digitos: ")
    senha_usuario = "1235" #input("Digite sua senha de 4 digitos: ")

    contas = {
        1234: {"usuário": "joão","senha":"1234","saldo": 1000.00},
        1235: {"usuário": "joão","senha":"1235","saldo": 1000.00}
    }
    
    if verificao_conta(conta_usuario,contas):
        # para cada conta
        for conta in contas:
            # verificação se a conta do usuário é a mesma conta
            if conta_usuario == conta:
                # verificação senha do usuário igual a senha da conta
                if contas[conta]['senha'] == senha_usuario:
                    return True
                else:
                    return False
    else:
        print("Essa conta não existe")
        
def verificao_conta(conta_usuario,contas):
    # verificação se a conta do usuário está em contas
    if conta_usuario in contas:
        return True
    else:
        return False

caixa_eletronico()
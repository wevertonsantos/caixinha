'''
Um programa que simula o funcionamento básico de um caixa eletrônico, permitindo que o usuário:

Acesse uma conta com senha (opcional no começo);

Veja o saldo atual;

Faça depósitos;

Realize saques;

Encerre a sessão.
'''

def caixa_eletronico():
    conta = 1234 #input("Digite sua conta de 4 digitos: ")
    senha = 1234 #input("Digite sua senha de 4 digitos: ")

    lista_contas = [1234,5432,3214,2345]
    contas = {
        1234: {"usuário": "joão","senha":"1234","saldo": 1000.00}
    }
    if conta in lista_contas:
        ...
    else:
        print("Essa conta não existe")

caixa_eletronico()
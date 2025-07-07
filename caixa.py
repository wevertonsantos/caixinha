'''
Um programa que simula o funcionamento básico de um caixa eletrônico, permitindo que o usuário:

Acesse uma conta com senha (opcional no começo);

Veja o saldo atual;

Faça depósitos;

Realize saques;

Encerre a sessão.
'''

def caixa_eletronico():
    conta = 12345 #input("Digite sua conta: ")
    senha = "12345" #input("Digite sua senha: ")

    lista_contas = [1234,12345,3214,2345]
    if conta in lista_contas:
        ...
    else:
        print("Essa conta não existe")

caixa_eletronico()
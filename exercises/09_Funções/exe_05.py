"""
[SEM PARÂMETROS] Aproveitando o exercício 4, agora vamos incluir mais funções,
seu programa principal deve ter um menu com as seguintes opções:
Somar, Subtrair, Multiplicar, Dividir, Sair.
Todas as operações devem ser feitas em funções e a
impressão seguindo o padrão do exercício 3.
"""


def Soma():
    num = []
    print()
    for cont in range(1, 4):
        num.append(int(input(f'Digite o{cont}º numero: ')))

    return sum(num)


def Subtrair():
    num = []
    print()
    for cont in range(1, 4):
        num.append(int(input(f'Digite o{cont}º numero: ')))

    return (num[0] - num[1]) - num[2]


def Multiplicar():
    num = []
    print()
    for cont in range(1, 4):
        num.append(int(input(f'Digite o{cont}º numero: ')))

    return num[0] * num[1] * num[2]


def Dividir():
    num = []
    print()
    for cont in range(1, 4):
        num.append(int(input(f'Digite o{cont}º numero: ')))

    return (num[0] / num[1]) / num[2]


def Menu():
    print("""\nMenu Principal
        [1]Somar
        [2]Subtrair
        [3]Multiplicar
        [4]Dividir
        [5]Sair
        """)


# __________ Programa princicpal __________

while True:
    Menu()
    opc = int(input('Opcao: '))

    if opc == 1:
        Soma()

    elif opc == 2:
        print(f'Subtraindo os valores, temos: {Subtrair()}')

    elif opc == 3:
        print(f'Multiplicando os valores, temos: {Multiplicar()}')

    elif opc == 4:
        print(f'Dividindo os valores, temos: {Dividir()}')
    else:
        print('Encerrando o sistema...')
        break

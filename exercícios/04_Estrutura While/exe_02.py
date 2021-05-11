"""
Crie um programa de operações matemáticas, ele deve receber 2 valores
informados pelo usuário e um menu com opções, onde o usuário possa
escolher: Somar, subtrair, dividir, multiplicar e sair.
"""

num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))

while True:
    print('''\033[33m\nMENU PRINCIPAL 
    SR - Somar
    SB - Subtrair
    DR - Dividir
    MR - Multiplicar
    NN - Novos números
    SA - Sair
    \033[m''')
    opc = str(input('Opção: ')).upper().strip()
    print()

    if opc == 'SR':
        print(f'{num1} + {num2}  = {num1 + num2}')
    elif opc == 'SB':
        print(f'{num1} - {num2}  = {num1 - num2}')
    elif opc == 'DR':
        print(f'{num1} / {num2}  = {num1 / num2}')
    elif opc == 'MR':
        print(f'{num1} * {num2}  = {num1 * num2}')
    elif opc == 'NN':
        num1 = int(input('Digite o 1º número: '))
        num2 = int(input('Digite o 2º número: '))
    elif opc == 'SA':
        print('O programa foi encerrado!')
        break

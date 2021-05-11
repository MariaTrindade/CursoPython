"""
Faça um programa que leia um número inteiro e na sequencia mostre se ele é
ou não um número primo. (Números primos são divisíveis por 1 e eles mesmos apenas).
"""
from time import sleep
num = int(input('Digite um número: '))
primo = 0

for cont in range(1, num + 1):
    # print(f'{num} / {cont} = {num % cont}')

    if num % cont == 0:
        print('\033[32m', end=' ')
        sleep(1)
        primo += 1
    else:
        print('\033[31m', end=' ')
        sleep(1)
    print(cont, end=' ')


if primo == 2:
    print(f'\n\n\033[m{num} Sendo divisível por {primo} números, ele é número primo!')
else:
    print(f'\n\n\033[m{num} Sendo divisível por {primo} números, ele não é número primo!')








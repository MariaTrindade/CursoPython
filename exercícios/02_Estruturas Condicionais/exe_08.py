"""
Faça um programa que peça o preço de 3 produtos e informe ao usuário qual produto
ele deve comprar, sendo que, o usuário deseja comprar aquele que for mais barato.
"""


'''
arroz = float(input('Digite o valor do Arroz: '))
feijao = float(input('Digite o valor do Feijão: '))
batata = float(input('Digite o valor da batata: '))

if batata < feijao and batata < arroz:
    print(f'\nVocê deve comprar batata.')
if feijao < arroz and feijao < batata:
    print(f'\nVocê deve comprar feijão.')
if arroz < feijao and arroz < batata:
    print(f'\nVocê deve comprar arroz.')
'''


produto1 = str(input('Digite o produto: '))
valor1 = float(input(f'Digite o valor do(a) {produto1}: '))
produto2 = str(input('Digite o produto: '))
valor2 = float(input(f'Digite o valor do(a) {produto2}: '))
produto3 = str(input('Digite o produto: '))
valor3 = float(input(f'Digite o valor do(a) {produto3}: '))

n_maisbarato = produto1
v_maisbarato = valor1

if valor2 < valor1 and valor2 < valor3:
    n_maisbarato = produto2
    v_maisbarato = valor2


if valor3 < valor1 and valor3 < valor2:
    v_maisbarato = valor3
    n_maisbarato = produto3

print(f'\nCom valor R${v_maisbarato:.2f} o produto a ser comprado é: {n_maisbarato}')


'''



p1 = float(input('Digite o valor do produto 1: '))
p2 = float(input('Digite o valor do produto 2: '))
p3 = float(input('Digite o valor do produto 3: '))

menor_valor = 0

if p1 == p2 == p3:
    print('\nOs 3 valores são iguais')

elif p1 == p2:
    if p1 < p3:
        print('\np1 e p2 são os menores valores.')
    else:
        print('\np3 é o menor valor.')

elif p1 == p3:
    if p1 < p2:
        print('\np1 e p3 são os menores valores.')
    else:
        print('\np2 é o menor valor.')

elif p2 == p3:
    if p2 < p1:
        print('\np2 e p3 são os menores valores.')
    else:
        print('\np1 é o menor valor.')

elif p1 != p2 != p3 != p1:
    if (p1 < p2) and (p1 < p3):
        print('\np1 é o menor valor.')
    elif (p2 < p1) and (p2 < p3):
        print('\np2 é o menor valor.')
    else:
        print('\np3 é o menor valor.')


'''



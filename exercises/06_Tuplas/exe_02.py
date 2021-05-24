'''
Crie um programa que sorteie 10 números aleatórios, armazene-os em uma
tupla. Ao final mostre o maior e menor valor que foi armazenado nesta
tupla.
'''
'''
from random import randint

temporaria = []

for cont in range(10):
    temporaria.append(randint(0, 100))

sorteados = tuple(temporaria)

print(f'Valores sorteados: ', end='')
for s in sorteados:
    print(s, end=' ')
print(f'\nMaior valor sorteado: {max(sorteados)}')
print(f'Menor valor sorteado: {min(sorteados)}')
print(f'Coleção do tipo: {type(sorteados)}')
'''

numeros_aleatorios = []

for n in range(4):
    numeros_aleatorios.append(int(input(f'Digite {n + 1} numero: ')))

numeros = tuple(numeros_aleatorios)
print(f'Maior numero inserido: {max(numeros_aleatorios)}')

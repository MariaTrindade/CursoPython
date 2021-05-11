"""
Faça um programa que mostre a soma dos valores pares entre 0 e 50.
O mesmo para os valores ímpares.
"""
pares = impares = 0

for cont in range(51):

    if cont % 2 == 0:
        pares += cont
    else:
        impares += cont

print(f'Somando valores pares no intervalo 0 a 50, temos: {pares}')
print(f'Somando os valores ímpares no intervalo 0 a 50, temos: {impares}')

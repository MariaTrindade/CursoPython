"""
Faça um programa que leia 10 números inteiros e ao final mostre apenas aqueles que
forem pares, os valores impares devem ser ignorados. Mostre também a soma de todos
os valores para inseridos.
"""

soma = 0
pares = []

for cont in range(3):
    num = int(input('Digite um número inteiro: '))
    soma += num

    if num % 2 == 0:
        pares.append(num)


print('\nNúmeros pares inseridos: ', end='')
for num in pares:
    print(num, end=' ')
print(f'\nSomando números inseridos, temos: {soma}')
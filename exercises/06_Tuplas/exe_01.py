'''
Crie um programa que peça 10 números inteiros, armazene-os em uma tupla.
Ao final mostre:
a) Quantas vezes apareceu o número 10
b) Caso tenha o valor 3, mostre em qual posição ele foi inserido.
c) Todos os números pares.
d) A soma dos números ímpares.
'''

lista_numeros = []
impar = 0

for n in range(5):
    lista_numeros.append(int(input(f'Digite {n + 1}º número: ')))

numeros = tuple(lista_numeros)

print(f'\n\nVezes que o valor 10 apareceu: {numeros.count(10)}')

if 3 in numeros:
    print(f'Encontrei o número 3 na posição: {numeros.index(3) + 1}')
else:
    print('Ops, não encontrei o número 3')

print('Números pares: ', end='')
for num in numeros:
    if num % 2 == 0:
        print(num, end=' ')
    else:
        impar += num

print(f'\nSomando todos os números ímpares, temos: {impar}')
print(f'Somando todos os números, temos: {sum(numeros)}')

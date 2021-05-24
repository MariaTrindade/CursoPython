"""
Faça um Programa que tenha uma lista com 20 números inteiros
aleatórios no intervalo 0 – 50 e armazene-os. Armazene os números
pares na lista PAR e os números IMPARES na lista ímpar,
imprima as 3 listas.
"""
par = []
impar = []
numeros = []

while True:
    num = int(input('Digite um número: '))
    if (num >= 0) and (num <= 50):
        numeros.append(num)
    if len(numeros) == 10:
        break

# ------- Fora do while --------

for numero in numeros:
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

# ------- Imprimindo resultado --------

print(f'\nTodos os números: {numeros}\nNúmeros pares: {par}\nNúmeros ímpares: {impar}\n')

print('Todos os números: ', end='')
for num in numeros:
    print(num, end=' ')

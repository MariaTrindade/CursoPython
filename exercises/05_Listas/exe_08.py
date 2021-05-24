"""
Faça um Programa que leia um vetor A com 10 números inteiros,
calcule e mostre a soma dos quadrados dos elementos do vetor.
"""
vet_a = []
soma = 0

for cont in range(5):
    vet_a.append(int(input('Digite um número: ')))

for numero in vet_a:
    print(f'Número: {numero} | Elevado ao quadrado, temos: {numero ** 2}')
    soma += numero ** 2

print(f'\nSomando os todos n², temos: {soma}')
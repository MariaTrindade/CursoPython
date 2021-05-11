"""
Crie um programa que peça vários números ao usuário e interrompa
quando o usuário digitar 999, ao final, mostre a soma de todos
os valores digitados, sem o FLAG.
"""

soma = 0

while True:
    num = int(input('Digite um número: '))

    if num == 999:
        break

    soma += num

print(f'Somando os números: {soma}')

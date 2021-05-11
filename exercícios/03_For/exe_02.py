"""
Faça um programa que leia 5 números e ao final,
mostre o maior e menor número digitado.
"""

maior = menor = 0

for cont in range(5):
    numero = int(input(f'Digite o {cont + 1}º número: '))
    if cont == 0:           # Verifica se é o primeiro número.
        maior = numero
        menor = numero

    if numero > maior:     # Verifica se o número digitado é maior que o armazenado
        maior = numero

    if numero < menor:     # Verifica se o número digitado é menor que o armazenado
        menor = numero

    print(f'\n\033[33mNúmero digitado: {numero}\nMaior número neste momento: {maior}\n'
          f'Menor número neste momento: {menor}\n\033[m')





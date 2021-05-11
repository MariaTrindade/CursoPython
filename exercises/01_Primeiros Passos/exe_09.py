"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

a. O produto do dobro do primeiro com metade do segundo.
b. A soma do triplo do primeiro com o terceiro.
c. O terceiro elevado ao cubo.
"""

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
num3 = float(input('Digite um número decimal: '))

a = (num1 * 2) * (num2 / 2)
b = num1 * 3 + num3
c = num3 ** 3

print(f'\nResultados:\na) {a}\nb) {b}\nc){c}')

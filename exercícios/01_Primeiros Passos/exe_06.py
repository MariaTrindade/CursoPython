"""
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. (A = r² • pi)
"""

from math import pi

raio = float(input('Informe o raio do círculo: '))

area = raio ** 2 * 3.14

area1 = raio ** 2 * pi

print(f'\nDado o raio {raio}, temos área de: {area:.2f}')
print(f'Dado o raio {raio}, temos área de: {area1:.2f}')

print(f'\nDado o raio {raio}, temos área de: {raio ** 2 * 3.14:.2f}')
print(f'Dado o raio {raio}, temos área de: {raio ** 2 * pi:.2f}')
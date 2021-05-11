"""
 Faça um programa que leia ano de nascimento de 5 pessoas e no final
 mostra quantas pessoas já atingiram a maior idade e para aquelas que
 ainda atingiram, mostre a média em anos que faltam para chegarem a maior idade.
"""

from datetime import date

ano_atual = date.today().year
maior = menor = soma = 0

for cont in range(3):
    ano_nasc = int(input('Digite seu ano de nascimento: '))

    if (ano_atual - ano_nasc) >= 18:
        maior += 1
    else:
        menor += 1
        soma += 18 - (ano_atual - ano_nasc)

media = soma / menor

print(f'\nTotal de pessoas com mais de 18 anos: {maior}\n'
      f'Total de pessoas com menos de 18 anos: {menor}\n'
      f'Média em anos restante para chagar aos 18 anos: {media:.1f}')

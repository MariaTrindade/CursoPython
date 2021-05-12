"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""

nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 1ª nota: '))
nota3 = float(input('Digite a 1ª nota: '))
nota4 = float(input('Digite a 1ª nota: '))

media = (nota4 + nota3 + nota2 + nota1) / 4

print(f'\nSua média bimestral é: {media:.1f}')

print(f'Sua média bimestral é: {(nota1 + nota2 + nota3 + nota4) / 4}')

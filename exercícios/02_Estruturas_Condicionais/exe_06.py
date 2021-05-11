"""
Faça um programa que receba 4 notas, calcule a média do aluno e mostre na tela:
A média do aluno e a situação final, sendo: Aprovado com nota igual ou superior a 7,
em recuperação se a nota estiver entre 6.9 e 5 e reprovado com nota menor que 5.
"""

nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
nota3 = float(input('Digite a 3ª nota: '))
nota4 = float(input('Digite a 4ª nota: '))

media = (nota1+nota2+nota3+nota4)/4

if media >= 7:
    status = 'APROVADO'
elif (media <= 6.9) and (media >= 5):
    status = 'RECUPERAÇÃO'
else:
    status = 'REPROVADO'


print(f'\nA média é: {media:.1f}')
print(f'Situação do aluno: {status}')
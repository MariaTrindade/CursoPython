"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados:

11% para o Imposto de Renda
8% para o INSS
5% para o sindicato

Faça um programa que nos dê:

a. Salário bruto.
b. Quanto pagou ao INSS.
c. Quanto pagou ao sindicato.
d. O salário líquido.
e. Calcule os descontos e o salário líquido.
"""

salario_hora = float(input('Informe quanto você recebe por hora: '))
horas_trabalhadas = float(input('Informe quantas horas foram trabalhadas: '))

salario_bruto = salario_hora * horas_trabalhadas

imposto_renda = 11 * salario_bruto / 100
inss = 8 * salario_bruto / 100
sindicato = 5 * salario_bruto / 100

print('\n')
print('*' * 40)
print('Holerite'.center(40))
print('*' * 40)

print(f'Salário Bruto: R${salario_bruto:.2f}')
print('-' * 40)
print(f'Imposto de Renda: R${imposto_renda:.2f}')
print(f'INSS: R${inss}')
print(f'Sindicato: R${sindicato}')
print('-' * 40)
print(f'Total de descontos: R${imposto_renda+inss+sindicato:.2f}')
print('-' * 40)
print(f'Salário liquido: R${salario_bruto-imposto_renda-inss-sindicato:.2f}')
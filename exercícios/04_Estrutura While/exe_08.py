"""
Crie um programa que peça para n alunos a sua idade, ao final o programa deverá verificar
se a média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então, dizer se
a turma é jovem, adulta ou idosa, conforme a média calculada. Flag = idade 0
"""

soma_idade = quant_alunos = media_turma = 0

while True:
    idade = int(input('Digite a Idade ou 0 para sair: '))

    if idade == 0:
        break

    soma_idade += idade
    quant_alunos += 1

if soma_idade == 0:
    print('\nNão temos dados suficientes para calcular...')
else:
    media_turma = soma_idade / quant_alunos

    if (media_turma > 0) and (media_turma <= 25):
        print('\nA turma é jovem.')

    elif (media_turma >= 26) and (media_turma <= 60):
        print('\nA turma é adulta.')
    else:
        print('\nA turma é idosa.')

    print(f'Soma: {soma_idade}\nQuantidade de alunos: {quant_alunos}\n'
        f'Média de idade da turma: {media_turma}')

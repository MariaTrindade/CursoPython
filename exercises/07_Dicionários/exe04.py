"""
Crie um programa que leia nome e média de um aluno.
Armazene todos os dados em um dicionário.
Ao final, mostre o resultado de maneira organizada.
"""
'''
aluno = {'nome': 'Leonardo', 'media': 9.5}

for c, v in aluno.items():
    print(f'{c:<5} ====> {v}')
'''
aluno = dict()
notas = list()
aluno['nome'] = str(input('Digite seu nome: ')).title()
for cont in range(4):
    notas.append(float(input(f'Digite a {cont + 1}ª nota: ')))
aluno['notas'] = notas
aluno['media'] = (sum(aluno['notas']) / len(aluno['notas']))
if aluno['media'] >= 7:
    print(f"\nO {aluno['nome']}, foi Aprovado!")
elif (aluno['media'] >= 5) and (aluno['media'] < 7):
    print(f"\nO {aluno['nome']}, está em Recuperação!")
else:
    print(f'\nO {aluno["nome"]}, foi Reprovado!')
for c, v in aluno.items():
    print(f'{c:<5} ==> {v}')

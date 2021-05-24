"""
Faça um Programa que peça as quatro notas de 10 alunos,
calcule e armazene numa lista a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0.
"""
notas = []
turma = list()

for a in range(2):
    nome = str(input('Nome do aluno: ')).title()
    for n in range(4):
        notas.append(float(input(f'{n + 1}ª nota: ')))
    turma.append([nome, sum(notas) / len(notas)])
    print()

# ------ imprimindo -------

print(f"\n{'Nº':<3}| {'NOME':<20} | {'MÉDIA':>5}")
for c, v in enumerate(turma):
    print(f'{c:<3}| {v[0]:<20} | {v[1]:5.1f}')

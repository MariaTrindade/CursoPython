"""
Aprimore o programa anterior, fazendo com que possam ser cadastrados
nome e média de 3 alunos e ao final imprima de maneira organizada o boletim da turma.
"""

aluno = dict()
turma = []

for c in range(3):
    aluno.clear()
    aluno['nome'] = str(input('Nome: ')).title()
    aluno['media'] = float(input(f'Média da(o) {aluno["nome"]}: '))
    print()
    turma.append(aluno.copy())

print(turma)


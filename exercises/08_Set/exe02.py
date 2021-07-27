"""
Crie um programa para uma escola, crie 3 turmas, cadastre pelo menos 5 alunos em cada uma,
(lembrando que 1 aluno pode estar matriculado em várias turmas, os Alunos devem ter nome e sobrenome.
Ao final apresente de forma organizada os alunos de cada turma, aqueles que fazem mais de 1 curso,
aqueles que fazem apenas 1 curso, todos os alunos da escola e nome e o número total.
"""

turma1 = list()
turma2 = list()
turma3 = list()

for cont in range(2):
    turma1.append(str(input('Turma1 Nome completo: ')).title())
    turma2.append(str(input('Turma2 Nome completo: ')).title())
    turma3.append(str(input('Turma3 Nome completo: ')).title())

turma1set = set(turma1)
turma2set = set(turma2)
turma3set = set(turma3)

print(f'Total de alunos turma1: {len(turma1)}')
print(f'Total de alunos turma2: {len(turma2)}')
print(f'Total de alunos turma3: {len(turma3)}')
print(f'Total geral de alunos : {len(turma1)+ len(turma2) + len(turma3)}')
print()

print('Alunos da turma1: ', end='')
for nome in turma1:
    print(nome, end='. ')

print('\nAlunos da turma2: ', end='')
for nome in turma2:
    print(nome, end='. ')

print('\nAlunos da turma3: ', end='')
for nome in turma3:
    print(nome, end='. ')

totAlunos = turma1set | turma2set | turma3set | turma1set
soturma1 = turma1set.difference(turma2set).difference(turma3set)
soturma2 = turma2set.difference(turma3set).difference(turma1set)
soturma3 = turma3set.difference(turma1set).difference(turma2set)

print('\nAlunos que fazem apenas 1 turma: ', end='')
for nome in soturma1:
    print(nome, end='. ')
for nome in soturma2:
    print(nome, end='. ')
for nome in soturma3:
    print(nome, end='. ')

print(f'\nSomente Turma 1: {soturma1}\nSomente Turma 2: {soturma2}\nSomente Turma 3: {soturma3}')
print(f'\nTodos os alunos: {totAlunos}')
todosCursos = turma1set & turma2set.intersection(turma3set)
print(f'Todos os Alunos: {todosCursos}')

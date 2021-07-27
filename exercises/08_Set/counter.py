from collections import Counter

turma1 = []
turma2 = []
turma3 = []

for a in range(3):
    turma1.append(str(input('Turma1 * Aluno: ')).title()) 
    turma2.append(str(input('Turma2 * Aluno: ')).title())
    turma3.append(str(input('Turma3* Aluno: ')).title())

escola = turma1 + turma2 + turma3

# print(Counter(escola))

for nome, rep in Counter(escola).items():
    if rep == 3:
        print(f'Alunos que estudam em 3 turmas: {nome}')
        # print(f'Parabéns {nome} por estudar em todas as turmas!')
    elif rep == 1:
        print(f'Alunos que estudam em apenas 1 turma: {nome}')
    else:
        print(f'Alunos que estudam em apenas 2 turmas: {nome}')
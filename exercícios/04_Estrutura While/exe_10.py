"""
Crie um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve
perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e
assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa).
Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema.
Após todos os alunos terem respondido informar:
    a. Maior e Menor Acerto;
    b. Total de Alunos que utilizaram o sistema;
    c. A Média das Notas da Turma.
Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
"""

gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
respostas = []
alunos = []
turma = []
nota = 0

while True:
    nome = str(input('Nome: ')).strip().title()
    alunos.append(nome)

    for r in range(1, 11):
        respostas.append(str(input(f'{r}ª resposta: ')).upper().strip())

    for e in range(len(gabarito)):

        if respostas[e] == gabarito[e]:
            nota += 1

    alunos.append(nota)

    sair = str(input('\nTecle S para sair ou N para aluno: ')).upper().strip()

    if sair == 'S':
        break


print(alunos)
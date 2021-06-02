"""
Aprimore o programa anterior, fazendo com que possam ser cadastrados
vários alunos e ao final imprima de maneira organizada o boletim da turma.
"""

aluno = dict()
turma = list()

while True:
    aluno.clear()
    aluno['nome'] = str(input('Nome: ')).title()
    aluno['media'] = float(input(f'Média da(o) {aluno["nome"]}: '))
    print()
    turma.append(aluno.copy())

    while True:
        saida = str(input('Cadastrar novo aluno? [S | N]: ')).upper()[0]
        if saida in 'SN':
            break
        print('Ops, dado inválido!')

    if saida == 'N':
        break

# imprimindo o boletim
print()
print('=' * 46)
print('\033[32mBOLETIM\033[m'.center(54))
print('=' * 46)

for dado in turma:
    for chave, valor in dado.items():
        if chave == 'media':
            chave = chave.replace('media', 'Média')

        print(f' {chave.title():<5} ===> {valor}')

        if chave == 'Média':
            print('-' * 46)

print('\033[32mEBONY SCHOOL\033[m'.center(54))
print('=' * 46)























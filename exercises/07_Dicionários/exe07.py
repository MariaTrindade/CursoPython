"""
Aprimore o programa anterior, fazendo com que ao final,
após impressão do boletim, também parabenize o aluno com a maior média da turma.
"""
aluno = dict()
turma = []
maior = 0
n_maior = ''

while True:
    aluno.clear()
    aluno['nome'] = str(input('Nome: ')).title()
    aluno['media'] = float(input(f'Média da(o) {aluno["nome"]}: '))
    print()

    # pegando nome do aluno com maior média
    if aluno['media'] > maior:
        maior = aluno['media']
        n_maior = aluno['nome'].split()

    turma.append(aluno.copy())

    while True:
        saida = str(input('Cadastrar novo aluno? [S/N]: ')).upper()[0]
        if saida in 'SN':
            break
        print('\033[31mOps, dado inválido!\033[m')
    if saida == 'N':
        break

# Imprimindo o boletim de maneira organizada
print('=' * 46)
print('\033[33mBOLETIM\033[m'.center(54))
print('=' * 46)

for aluno in turma:
    for c, v in aluno.items():
        if c == 'media':
            c = c.replace('media', 'Média')
        print(f' {c.title():<5} ===> {v}')
        if c == 'Média':
            print('-' * 46)

print(f'Parabéns \033[32m{n_maior[0]}\033[m por ter a maior média da turma!')
print('=' * 46)
print('\033[33mEBONY SCHOOL\033[m'.center(54))
print('=' * 46)

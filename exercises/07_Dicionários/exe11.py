"""
Crie um programa que leia o nome, ano de nascimento, e carteira de trabalho, armazene essas informações
em um dicionário, lembrando que deve-se armazenar a data de nascimento e ao mostrar, apresentar a idade.
No campo CTPS, caso o usuário possua, deve ser perguntado em quantas empresas ele trabalhou e por quanto meses.
Se o mesmo estiver trabalhando no momento, solicitar também a data da contratação e salário.

Ao final, apresente todos os dados deste usuário, calcule e apresente quanto tempo será necessário para ele
se aposentar. Considere para aposentadoria, idade superior a 60 ou 40 anos de contribuição.
"""
from datetime import date

usuario = dict()
ano_atual = date.today().year
soma_ano = soma_mes = tot_antiga = tot_atual = tot_geral = 0

while True:
    usuario['nome'] = str(input('Nome: ')).title()
    usuario['ano_nasc'] = int(input('Ano de nascimento: '))
    usuario['idade'] = ano_atual - usuario['ano_nasc']

    while True:
        usuario['ctps'] = str(input('CTPS? [S / N]: ')).upper()[0]
        if usuario['ctps'] in 'SN':
            break
        print('\033[31mOps, dado inválido!\n\033[m')

    if usuario['ctps'] == 'S':
        while True:
            atual_empresa = str(input('\nVocê está trabalahando no momento? [S / N]: ')).upper()[0]
            if atual_empresa in 'SN':
                break

        if atual_empresa == 'S':
            atual_ano = int(input('\nOk, vamos cadastrar alguns dados da sua empresa atual\n'
                                  'Ano(s): '))
            atual_mes = int(input('Més: '))
            atual_sal = float(input('Salário: '))

            tot_atual = atual_ano * 12 + atual_mes

        print('\nOk, vamos cadastrar alguns dados de empresas passadas.')
        total_empresa = int(input('Em quantas empresas vc trabalhou: '))

        for cont in range(total_empresa):
            print(f'\n{cont + 1}ª EMPRESA:')
            ano = int(input('Ano(s): '))
            mes = int(input('Mês(es): '))
            print('-' * 30)
            soma_ano += ano
            soma_mes += mes

        tot_antiga = soma_ano * 12 + soma_mes

    tot_geral = (tot_antiga + tot_atual) / 12

    print()
    print('=' * 50)
    print('DADOS PESSOAIS DO USUÁRIO'.center(50))
    print('-' * 50)

    for c, v in usuario.items():
        print(f'{c:_<16} {v}')

    print()
    print('=' * 50)
    print('DADOS PROFISSIONAIS DO USUÁRIO'.center(50))
    print('-' * 50)

    print(f'Tempo total de contrinuição: {tot_geral:.1f} ano(s)')
    print()
    print('APOSENTADORIA POR IDADE'.center(50))
    print('-' * 50)
    print(f'Restam: {60 - usuario["idade"]}')
    print()
    print('APOSENTADORIA POR CONTRIBUIÇÃO'.center(50))
    print('-' * 50)
    print(f'Restam: {40 - tot_geral}')
    break
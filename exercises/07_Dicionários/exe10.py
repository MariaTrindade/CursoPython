"""
Crie um programa que leia nome, sexo e idade de várias pessoas. Armazene todos os dados de cada
pessoa em um dicionário e todos os dicionários em uma lista. Ao final apresente:
A) Total de pessoas cadastradas.
B) A média de idade dos homens, mulheres e totais.
C) Uma lista com todas as mulheres cadastradas.
D) Uma lista com todas as pessoas maiores de 18 anos.
"""

pessoa = dict()
pessoas = list()
mulheres = list()
homens = list()
maiores_18 = list()
soma_id_h = soma_id_m = 0

while True:
    pessoa['nome'] = str(input('Nome: ')).title()
    pessoa['sexo'] = str(input('Sexo [M, F, O]: ')).upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    print()

    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
        soma_id_m += pessoa['idade']
    elif pessoa['sexo'] == 'M':
        homens.append(pessoa['nome'])
        soma_id_h += pessoa['idade']

    if pessoa['idade'] >= 18:
        maiores_18.append(pessoa['nome'])

    pessoas.append(pessoa.copy())
    pessoa.clear()

    while True:
        saida = str(input('Cadastrar nova pessoa? [S | N]: ')).upper()[0]
        if saida in 'SN':
            break
        print('Ops, dado inválido!\n')

    if saida == 'N':
        break

# ___________ imprimindo informações ___________
print()
print('=' * 40)
print(f'Total de pessoas cadastradas: {len(pessoas)}')

if len(mulheres) > 0:
    print('Mulheres cadastradas: ', end='')
    for nome in mulheres:
        print(f'{nome}. ', end='')

if len(maiores_18) > 0:
    print('\nMaiores de 18 anos: ', end='')
    for nome in maiores_18:
        print(f'{nome}. ', end='')

if len(homens) > 0:
    print(f'\nMédia de idade dos homens: {soma_id_h / len(homens)}')
if len(mulheres) > 0:
    print(f'Média de idade das mulheres: {soma_id_m / len(mulheres)}')

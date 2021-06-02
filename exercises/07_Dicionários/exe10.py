"""
Crie um programa que leia nome, sexo e idade de várias pessoas.
Armazene todos os dados de cada pessoa em um dicionário e
todos os dicionários em uma lista. Ao final apresente:
A) Total de pessoas cadastradas.
B) A média de idade dos homens, mulheres e totais.
C) Uma lista com todas as mulheres cadastradas.
D) Uma lista com todas as pessoas maiores de 18 anos.
"""

pessoa = dict()
pessoas = list()

while True:
    pessoa['nome'] = str(input('Nome: ')).title()
    pessoa['sexo'] = str(input('Sexo [M, F, O]: ')).upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    print()
    pessoas.append(pessoa.copy())
    pessoa.clear()

    while True:
        saida = str(input('Cadastrar nova pessoa? [S | N]: ')).upper()[0]
        if saida in 'SN':
            break
        print('Ops, dado inválido!\n')

    if saida == 'N':
        break

# imprimindo informações...
print()
print('=' * 40)
print(f'Total de pessoas cadastradas: {len(pessoas)}')


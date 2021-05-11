"""
Crie um programa onde o computador escolhe um número entre 1 e 15 e o usuário tenta adivinhar.
No final, mostre quantas tentativas foram necessárias para acertar.
Obrigatório utilizar while com expressão
"""

from random import randint

num = cont = 0
pc = randint(1, 15)

print('Vamos começar hem... eu já escolhi um número!'.upper())
print('*' * 45, '\n')

while num != pc:
    num = int(input('Qual é seu chute: '))

    if num == pc:
        print(f'\033[32m\nAhhh! legal, você acertou... eu escolhi {pc}\033[m')

    else:
        print('\033[31mOps, não foi este... tente novamente...\033[m')
        cont += 1

print(f'Você precisou de {cont+1} chances para acertar!')

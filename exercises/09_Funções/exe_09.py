"""
[SEM PARÂMETROS] Vamos trabalhar com vários returns, crie um programa de adivinhação de número, o pc
deverá escolher um número aleatoriamente entre 0 e 10, em seguida o usuário deverá tentar acertar
este número, retorne uma mensagem para cada tentativa que o usuário fizer, informando
se é maior ou menor e encerre o programa quando ele acertar o número, neste caso,
uma mensagem de despedida deve ser apresentada.
"""
from random import randint


def jogo1():
    toterro = 1
    pc = randint(0, 11)

    print('\nBlz, já escolhi um número, agora tente acertar...\n')

    while True:
        usuario = int(input('Qual é seu chute: '))

        if usuario != pc:
            toterro += 1

            if usuario > pc:
                print('...é menor!!!\n')
            else:
                print('...é maior!!!\n')

        else:
            print(f'\nLegal eu pensei {pc}, vc acertou!')
            print(f'Vc precisou de {toterro} para acertar.')
            break


# ====================================================================

while True:
    print('''\nMENU de JOGOS
[ 1 ] Acerte o número
[ 2 ] Serpente
[ 3 ] Campo minado''')

    jogo = int(input('Opção: '))

    if jogo == 1:
        jogo1()
    elif jogo == 2:
        print('Ops, jogo 2 ainda não foi criado.')
    elif jogo == 3:
        print('Ops, o jogo 3 ainda não foi criado.')
    else:
        break

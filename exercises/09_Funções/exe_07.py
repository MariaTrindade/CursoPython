"""
[SEM PARÂMETROS] Agora vamos brincar de cara ou coroa,
seu programa deve perguntar ao usuário se
ele quer cara ou coroa, em seguida sua função deve ser
chamada para gerar o resultado, em seguida informe ao
usuário se ele ganhou ou perdeu.
"""
from random import randint


def caraCoroa():
    usuario = int(input('''Tecle: 
    [1] CARA 
    [2] COROA
    : '''))

    moeda = randint(1, 2)

    if moeda == usuario:
        result = '\033[32mVenceu!!! \033[7m:)\033[m'
    else:
        result = '\033[31mPerdeu!!! \033[7m:(\033[m'

    if moeda == 1:
        status = 'CARA'
    else:
        status = 'COROA'

    print(f'\nDeu {status}! Você {result}')


# ===================================================

caraCoroa()

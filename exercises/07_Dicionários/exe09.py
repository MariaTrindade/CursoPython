"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Armazene essas informações em um dicionário. Ao fim, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado, informe o nome deste usuário.
"""
from random import randint
from operator import itemgetter
from time import sleep

jogadas = dict(
    jogador1=randint(1, 6),
    jogador2=randint(1, 6),
    jogador3=randint(1, 6),
    jogador4=randint(1, 6)
)

resultado = list()
resultado = sorted(jogadas.items(), key=itemgetter(1), reverse=True)

print('Vamos lá!'.center(40))
for c, v in jogadas.items():
    print(f'{c} ===> {v}')
    sleep(0.5)

print('\nLegal... agora vamos carregar o ranking!\n')
sleep(0.5)

print(f'RANKING'.center(40))
sleep(3)
for c, v in enumerate(resultado):
    print(f'{c + 1}º LUGAR ===> {v[0]} tirou {v[1]} no dado!')
    sleep(1)
"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Armazene essas informações em um dicionário. Ao fim, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado, informe o nome deste usuário.
"""
from random import randint

"""
jogadas = dict(
                jogador1=randint(1, 6),
                jogador2=randint(1, 6),
                jogador3=randint(1, 6),
                jogador4=randint(1, 6)
              )

for c, v in jogadas.items():
    print(f'O {c.title()} tirou: {v} no dado.')
"""

jogadores = dict()
jogador = dict()

for cont in range(4):
    jogador['nome'] = str(input('Nome: ')).title()
    jogador['tirou'] = randint(1, 6)

    jogadores[f'{cont + 1}º Jogador'] = jogador.copy()
    jogador.clear()

print()
for v in jogadores.values():
    for c, v in v.items():
        print(f'{c} --> {v}', end=' ')
        if c == 'tirou':
            print()


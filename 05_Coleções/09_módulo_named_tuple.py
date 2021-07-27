"""
Módulo Collections - Named Tuple

-> São tuplas nomeadas, podemos específicar nomes e parâmetros.

"""
from collections import namedtuple

# Criando uma tupla nomeada

#                     nome da tupla     parâmetro
cachorro = namedtuple('cachorro', 'nome raca idade')
gato = namedtuple('gato', 'nome, raca, idade, cor')
passaro = namedtuple('passaro', ['nome', 'raca', 'idade', 'tamanho'])

# Utilizando...

bob = cachorro(nome='Bob', raca='Chow-Chow', idade='1')
juca = gato(nome='Juca', raca='Viralata', idade='2', cor='preto')
piu = passaro(nome='Piu', raca='trinca-ferro', idade='3', tamanho='Médio')


print(bob)
print(bob[0])
print(bob[1])
print(bob[2])

print()

print(f'Nome do meu cachorro é {bob.nome}')

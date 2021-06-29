"""
LIB Collections
MÓDULO COUNTER
    - Retorna um "dicionário", porém o type será collections-counter
    - Geralmente utilizado para recorrêcias
    - Quando precisamos processar dados massivos
"""
from collections import Counter

frase = 'Python é legal'.lower()
print(frase.count('o'))

lista = ['Leonardo Alves', 'Juca Alves', 'Maria Alfredo',
         'Fernanda Almeida', 'Juca Alves', 'Leonardo Alves',
         'Maria Trindade', 'Maria Trindade', 'Paola Souza',
         'Paola Souza', 'Paola Souza', 'Manoel Bispo']


resposta = Counter(lista)
print(type(resposta))

for chave, valor in resposta.items():
    if valor == 1:
        print(f'{chave} ==> {valor}')

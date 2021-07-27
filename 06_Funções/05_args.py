"""
*Args
    - parâmentro de entrada de uma função
    - pode ser chamado de qualquer coisa desde que comece com *

Exemplo
    - *xis
    - Por convenção, utilizamos sempre args, ou seja, *args

    - Coloca os valores extras dentro de uma tupla;
"""


def mostraTudo(*args):
    print(args)


mostraTudo()
mostraTudo(1)
mostraTudo(1, 'leo')
mostraTudo(1, 'leo', True, 10.58)


def somaTudo(*args):
    total = 0
    for numero in args:
        total += numero
    return total
    # return sum(args)


print(somaTudo())
print(somaTudo(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# Erro quando tento passar uma lista diretamente
def somaTudo(*args):
    return sum(args)


numeros = [1, 2, 3, 4, 5, 6]
# print(somaTudo(numeros)) # Gera erro, esta lista será o item 1 da tupla

# corrigindo com desempacotador
print(somaTudo(*numeros))  # informamos que estamos passando uma coleção

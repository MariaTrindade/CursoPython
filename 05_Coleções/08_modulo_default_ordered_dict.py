"""
Módulo collections - Ordered Dict

- Em dicionários,por padrão a ordem de inserção de dados não é garantida.

==> O ordereddict garante a ordem de inserção dos elementos.

- Tudo o que vimos com dicionários, funcionam com ordereddict também.
"""

from collections import OrderedDict

'''
dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3})
for c, v in dicionario.items():
    print(f'{c} ===> {v}')
'''

# confirmando que o dict normal não se importa com a ordem
teste1 = {'a': 1, 'b': 2}
teste2 = {'b': 2, 'a': 1}

print(teste1 == teste2)

# confirmando que o OrderedDict mantem a ordem de inserção
teste1 = OrderedDict({'a': 1, 'b': 2})
teste2 = OrderedDict({'b': 2, 'a': 1})

print(teste1 == teste2)



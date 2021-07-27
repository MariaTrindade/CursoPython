"""
Módulo collections - Ordered Dict

- Em dicionários, por padrão a ordem de inserção de dados não é garantida.

==> O ordereddict garante a ordem de inserção dos elementos.

- Tudo o que vimos com dicionários, funcionam com ordereddict também.
"""

from collections import OrderedDict

teste1 = {'a': 1, 'b': 2}
teste2 = {'b': 2, 'a': 1}
#print(teste1 == teste2)

teste3 = OrderedDict({'a': 1, 'b': 2})
teste4 = OrderedDict({'b': 2, 'a': 1})
print(teste3 == teste4)

cadastro = dict(nome='leonardo', cpf=216546)

nome = cadastro['cpf']
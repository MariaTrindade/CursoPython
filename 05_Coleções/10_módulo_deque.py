"""
LIB Collections
Módulo Deque
    - Lista de alta performance
    - AppendLeft - Adiciona no início da lista
    -
"""

from collections import deque

nomes = deque('Leonardo')

nomes.append('Y')
nomes.appendleft('W')

print(f'Item removido: {nomes.pop()}')
print(f'Lista pós remoção: {nomes}')
# nomes.popleft()

for i, v in enumerate(nomes):
    print(f'{i} - {v}')



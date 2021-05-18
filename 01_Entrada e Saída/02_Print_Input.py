"""
Print >>> Mostrar dado
Input >>> Obter um dado do usário
"""

# nome = 'leonardo alvES'.title().strip().split()
# print('Muito prazer, {}'.format(nome))
# print(f'Muito prazer, {nome[1]}')

# Com split: Gerando índice
#       0               1
# L e o n a r d o   a l v e s


# 0 1 2 3 4 5 6 7 8 9 10 11 12 13     Python sempre cria um índice interno quando inserimos um dado.
# L e o n a r d o   a  l  v  e  s


nome1 = input('Qual seu nome: ')

# Sintaxe antiga
print('Muito prazer, {}'.format(nome1))

# Sintaxe atual
print(f'Muito prazer, {nome1}')

"""
Módulo collections - Default Dict

- Uzamos sempre que houver a necessidade de processamento de dados de alta performance

- Tudo que fazemos com dicionários normais, funcionam também.

- Caso tente acessar uma chave que não existe, não retorna erro e sim
faz a criação desta chave automáticamente.

==> LAMBDAS são funções sem nome, que podem ou não receber parâmetros de entrada
e retornar valores.
"""

from collections import defaultdict

# ex1
# dicionario = {'curso': 'Python'}
# print(dicionario['outro'])  # vai retornar erro de chave

# criando com defaultdict

dicionario1 = defaultdict(lambda: 'n/s')
print(dicionario1['nome'])  # A chave que não existia, foi criada.
print(dicionario1['tel1'])  # A chave que não existia, foi criada.
print(dicionario1['Tel2'])
print(dicionario1['email'])

# print(dicionario1)  # imprimindo o dict pós inclusões

dicionario1['nome'] = 'leonardo'
dicionario1['tel1'] = 1314564654652

print()

for c, v in dicionario1.items():
    if v != 'n/s':
        print(f'{c} ==> {v}')


print(f'\nDados não preenchidos: ', end='')
for c, v in dicionario1.items():
    if v == 'n/s':
        print(f'{c}', end='. ')


















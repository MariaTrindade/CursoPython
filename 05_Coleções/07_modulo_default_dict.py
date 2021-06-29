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
dicionario1 = defaultdict(lambda: 'inválido')
print(dicionario1['outro'])  # A chave que não existia, foi criada.
print(dicionario1['ninguém'])  # A chave que não existia, foi criada.
print(dicionario1)  # imprimindo o dict pós inclusões

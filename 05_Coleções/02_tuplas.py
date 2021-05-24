"""
Tuplas >>> Tuple

Tuplas não são mutáveis, uma vez criada, permanecerá tal qual durante a execução do código.
- Aceita assim como as listas, quaisquer tipos de dados.

Sintaxe's
variável = ()
variável = tuple()

Tuplas são definidas por , e não por uso de parenteses.

Métodos de adição, remoção, alteração, ordenação em tuplas não existem.

Utilizamos em coleções que não sofrem alterações.
Ex: meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

    dias_da_semana = ('Domingo', 'Segunda', 'Terça', 'Quarta', Quinta', Sexta', Sábado')
"""
'''
# Criando uma lista
lista = []
lista1 = list()

# Criando uma tupla
tupla = ('leonardo')
tupla1 = tuple()

# quando utilizar uma funcão/método direto na criação da tupla, é necessário ustilizar
# o padrão de criação LIST()
num = (range(10))
num1 = tuple(range(10))
print(num1)

# As tuplas aceitam dados de tipos variados. Pode-se criá-la sem os parenteses, mas por
# padrão de boas práticas, sempre uzaremos os parenteses.
tupla = (1, 2, 'leo', 10.8)
print(tupla)

# Métodos que não funcionam: Sort Reverse, append, pop, remove, clear
num = (1, 5, 3, 4, 8, 4, 4, 15)

print(num.count(4))  # quantas vezes o número 4 aparece nesta tupla
print(sum(num))      # somando todos os valores desta tupla
print(max(num))      # maior valor dentro desta tupla
print(min(num))      # menor valor dentro desta tupla

# Concatenenado tuplas
num1 = (1, 2, 3)
num2 = (4, 5, 6)
num1 = num1 + num2

print(6 in num1) # verificando se existe o valor 6 dentro da tupla.

# iterando sobre tuplas.
meses = (
    'Janeiro',
    'Fevereiro',
    'Março',
    'Abril',
    'Maio',
    'Junho',
    'Julho',
    'Agosto',
    'Setembro',
    'Outubro',
    'Novembro',
    'Dezembro'
)

for mes in meses:
    print(mes)

for chave, valor in enumerate(meses):
    print(f'{chave} -> {valor}')


nomes = ('Leonardo', 'Maria', 'João')

for nome in nomes:
    print(f'Bom dia, {nome}!')

for c, v in enumerate(nomes):
    print(f'Neste índice {c}, temos: {v} ')



meses = (
    'Janeiro',
    'Fevereiro',
    'Março',
    'Abril',
    'Maio',
    'Junho',
    'Julho',
    'Agosto',
    'Setembro',
    'Outubro',
    'Novembro',
    'Dezembro'
)
#print(meses[0])   # acessando o primeiro valor desta tupla >>> Janeiro
#print(meses[-1])  # acessando o último valor desta tupla >>> Dezembro

# acessando o índice de um determinado valor dentro da tupla. Ps. mais aconselhavel
# utilizar um bloco TRY para que ele tente encontrar este índice, caso não o encontre
# crie uma EXCEPT para tratamento deste erro.

print(meses[5])

print(meses.index('Setembro'))

'''

nomes = ('leonardo', 'maria', 'juca', 'joana')


for nome in nomes:
    vac = str(input(f'{nome}, vc já tomou a vacina? '))























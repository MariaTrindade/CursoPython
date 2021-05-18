"""
Listas
Em outras linguagens é conhecida como Array, Vetor ou matriz...

* Dinâmica >>> Não possui tamanho fixo e não preciso informar este tamanho.
* Aceita qualquer tipo de dado.

* Sintaxe:
        [] ou list()

* SORT >>> Ordena os dados de uma lista.
* REVERSE >>> Inverte a lista.
* APPENDD >>> Atribui a lista, um elemento por vez. Podendo ser inclusive outra lista...
* INSERT >>> Atribui vários elementos, integrando à lista original.
* POP >>> Remove um valor da lista por índice.
* REMOVE >>> Remove um valor da lista por valor.
* ENUMERATE >>> Acesso à chave e valor.
* SHALLOW COPY
* CLEAR >>> Limpa a lista.

** LIMITAÇÃO >>> Busca deve ser feita sempre por índices...
"""

lista4 = []                           # >>> Lista vazia
lista1 = [27.5, True, 'Leo', [5, 6]]  # >>> Lista com dados de vários tipos diferentes
lista2 = ['l', 'e', 'o']              # >>> Lista com 3 elementos de texto
lista3 = ['leo']                      # >>> Lista com 1 único elemento
lista6 = list('leo')                  # >>> Lista com 1 único elemento, criada com padrão list
lista5 = list(range(11)               # >>> Métodos só funcionam na criação quando é feito com padrão list

# Índices     0         1        2
nomes = ['Leonardo', 'Maria', 'João']

print(f'Oi, {nomes[0]}, bom dia!')  # >>> Nome[índice do valor que deseja mostrar]
print(f'Oi, {nomes[1]}, bom dia!')
print(f'Oi, {nomes[2]}, bom dia!\n')

for nome in nomes:                   # >>> para cada nome da lista de nomes...
    print(f'Oi, {nome}, bom dia!')   # >>> mostre esta mensagem...

# ___________________________________________________________________________________________

lista7 = [1, 5, 6, 4, 3, 8, 7]

lista7.sort()       # >>> Ordenando valores de uma lista
print(lista7)

lista7.reverse()         # >>> Valores invertidos
print(lista7)

print(lista7.count(3))          # >>> Contando valores

# ___________________________________________________________________________________________

lista8 = [1, 3, 4, 5]

lista8.append(6)            # >>> Inserindo um valor na lista (Append só aceita 1 elemento)
lista8.append([7, 8])       # >>> Inserindo uma lista com vários itens. (1 único elemento)
lista8.insert(1, 2)         # >>> Inserindo um valor na lista no índice 1
lista8.pop()                # >>> Removendo o último valor da lista
lista8.pop(4)               # >>> Removendo o valor no índice 4 da lista
lista8.remove(4)            # >>> Removendo o valor 4 da lista
lista8.clear()              # >>> Zerando a lista

print(lista8)

# ___________________________________________________________________________________________

numeros = []
numeros.append('Leonardo')
numeros.append('Maria')
numeros.append('Maria')

for chave, valor in enumerate(numeros):  # >>> Acessando chave e valor de uma lista
    print(f'{chave}º = {valor}')

nomes = []

for cont in range(3):
    nomes.append(str(input('Nome: ')).title().strip())

    # nome = str(input('Nome: '))
    # nomes.append(nome)

for nome in nomes:
    print(nome)

# ___________________________________________________________________________________________

a = [1, 2, 3]
b = [4, 5, 6]

c = b + a       # >>> atribuindo a junção de duas lista à uma.

print(c)

# ___________________________________________________________________________________________

a = [1, 2, 3]
b = a[:]         # >>> Copiando os valores da lista A para B.
b = a            # >>> Copiando os valore de lista A para B criando uma igualdade entre elas.
b.append(4)

print(f'Lista A: {a}')
print(f'Lista B: {b}')

# Desafio de aula: cadastrar quanto foi gasto nos almoços da semana:

import matplotlib.pyplot as plt
import numpy as np

dia_semana = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']
gasto = []

for dia in dia_semana:
    gasto.append(float(input(f'{dia} >>> R$ ')))

plt.plot(dia_semana, gasto, 'r')
plt.xlabel('Dias da semana')
plt.ylabel('Dinheiro gasto')
plt.show()




















"""
Conjuntos --> SET
- Igual aos conjuntos em matemática

Sintaxe:
variavel = {}
variável = set() Também utilizado para conversão de outras coleções para SET

- Aceita todos os tipos de dados, mas não dados repetidos
"""

# Sintaxe dicionários
dicionario = {'chave': 'valor'}
dicionario1 = dict(chave='valor')


# Sintaxe conjuntos
conjunto = {1, 2, 3, 4, True, 'valor'}


# Ex1 - Convertendo uma string em SET
frase = 'Leonardo Alveeeeeees'
print(len(frase))

frase_conv = set(frase)

print(frase_conv)
print(type(frase_conv))
print(len(frase_conv))


# ex2 - Convertendo uma lista em SET - Note que o número 5 não será duplicado no SET
lista = [1, 2, 3, 4, 5, 5, 6]
print(lista)
print(set(lista))


# Ex3 - Fazendo analises com SET
cidade = ['Rio de Janeiro', 'São Paulo', 'Juiz de Fora', 'Petrolina', 'Salvador',
          'Juiz de Fora', 'Rio de Janeiro', 'Petrolina', 'Salvador', 'São Paulo', 'São Paulo', 'São Paulo',
          'Juiz de Fora', 'Rio de Janeiro', 'Petrolina', 'Rio de Janeiro', 'Salvador', 'Juiz de Fora',
          'Petrolina', 'Salvador', 'Rio de Janeiro', 'Rio de Janeiro', 'Rio de Janeiro', 'Rio de Janeiro',
          'São Paulo', 'São Paulo', 'São Paulo', 'São Paulo', 'Rio de Janeiro', 'Rio de Janeiro', 'Rio de Janeiro',
          'São Paulo', 'Rio de Janeiro', 'São Paulo', 'Rio de Janeiro', 'São Paulo']

# O total neste caso pode ser retirado da lista completa
print(f'Total de visitantes: {len(cidade)}')

# validando quantas vezes o elemento 'Rio de janeiro" foi inserido na lista
tot_RJ = 0
for c in cidade:
    if c == 'Rio de Janeiro':
        tot_RJ += 1

print(f'Visitantes do Rio de Janeiro: {tot_RJ}')

# Como o set não repete o mesmo item, aqui podemos pegar cada um q foi inserido
cidade_semRepetir = set(cidade)

print(f'Cidades que visitaram hoje: {cidade_semRepetir}')
print(f'Total de cidades que visitaram hoje: {len(set(cidade))}')


# Mostrando alguns métodos que funcionam com SETś
conjunto = {1, 3, 4}
print(conjunto)

conjunto.pop()
print(conjunto)

conjunto.add(6)
conjunto.add('leo')
print(conjunto)  # 3, 4, 6

conjunto.discard(3)
conjunto.remove(6)
conjunto.remove('leonardo')  # erro
conjunto.discard('leoanrdo')  # não gera erro
print(conjunto)

conjunto = {10, 20, 30}
print(max(conjunto))
print(min(conjunto))
print(len(conjunto))
print(sum(conjunto))


# Ex4 - Union - Intersection - difference
cursoPython = ['Leonardo A.', 'Maria', 'Juca', 'Alfredo', 'Leonardo B.']
cursoBancodeDados = ['Leonardo A.', 'Beto', 'Joana', 'Maria', 'Felipe', 'Juca']
curso3 = ['Zacarias']

cursoPythonSet = set(cursoPython)
cursoBDSet = set(cursoBancodeDados)
curso3Set = set(curso3)

print(f'Total de alunos de Python: {len(cursoPython)}')
print(f'Total de alunos de Banco de Dados: {len(cursoBancodeDados)}')

totAlunos = cursoPythonSet.union(cursoBDSet).union(curso3Set)
totAlunos1 = cursoBDSet | cursoPythonSet | curso3Set
print(f'Alunos que fazem apenas 1 curso: {totAlunos}')
print(f'Alunos que fazem apenas 1 curso: {totAlunos1}')

ambosCursos = cursoPythonSet.intersection(cursoBDSet)
ambosCursos1 = cursoBDSet & cursoPythonSet
print(f'Alunos que fazem os 2 cursos: {ambosCursos}')
print(f'Alunos que fazem os 2 cursos: {ambosCursos1}')

soPython = cursoPythonSet.difference(cursoBDSet)
print(f'Somente Python: {soPython}')














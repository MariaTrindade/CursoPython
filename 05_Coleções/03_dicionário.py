"""
Dicionários - Em outras linguagens, conhecido como MAPA.

Sintaxe
exemplo1 = {}
exemplo2 = dict()

Aceita qualquer tipo de dado.
As chaves não podem ser repetidas.
"""
_________________________________________________________________

# Sintaxe de criação.
lista = []
lista1 = list()

tupla = ()
tupla1 = tuple()

dicionario = {'br': 'Brasil'}
dicionario1 = dict(br='Brasil')

print(type(dicionario))
_________________________________________________________________

# Exemplo 1: Dicionário com países e suas respectivas siglas.
paises = {
    'br': 'Brasil',
    'eua': 'Estados Unidos',
    'py': 'Paraguai'
}

# pedindo para o ususário digitar um sigla
resp = str(input('Informe a sigla de um país: ')).lower().strip()

# Fazendo uma busca pela sigla que foi digitada pelo usuário de 2 formas

# Menos usual | retorna erro casa a chave não seja encontrada.
print(f'País de nascimento: {paises[resp]}')

# Mais usual | retorna NONE caso a chave não seja encontrada.
print(f'Pais de nascimento: {paises.get(resp)}')
_________________________________________________________________

# Exemplo 2: Verificando se a sigla existe utilizando um if.
paises = {
    'br': 'Brasil',
    'eua': 'Estados Unidos',
    'py': 'Paraguai'
}

resp = str(input('Digite uma sigla: ')).lower().strip()

# Vale lembrar que o método GET permite este processo de maneira
# mais inteligente | um exemplo disso logo abaixo.
if resp:
    print(f'Econtrei... {resp}')
else:
    print('Não encontrei a sigla digitada')
_________________________________________________________________

# Verificando se a chave existe utilizando o método GET.
# GET > permite que um senão seja adicionado como abaixo.
resposta = paises.get('br', 'Ops não encontrei a sigla!')
print(f'País: {resposta}')

# Caso não seja passado um senão, o método retornará NONE
print(paises.get('BR'))  # none
_________________________________________________________________

# criando um dicionário tendo uma tupla como chave.
# É possível misturar todas as coleções quando houver necessidade.
localidade = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em Nova York'
}
_________________________________________________________________

# Inserindo, alterando e deletando elementos de um dicionário
receita = {
            'JAN': 2.000,
            'FEV': 4.000,
            'MAR': 8.000
          }

# inserindo elementos
receita['ABR'] = 16.000  # mais usual
receita.update({'MAI': 32.000})

# atualizar os elementos
receita.update({'MAI': 40.000})
receita['MAI'] = 30.000

# deletar os elementos
receita.pop('MAI')  # chave e valor
receita.popitem()  # última chave e valor

print(receita)
_________________________________________________________________

# Exercício de aula
"""
Simulando uso de carrinho de compras.
Atributos do produto:
    -nome           -cor           -quantidade em estoque
    -quantidade     -peso          -impostos
    -preço          -categoria     -preço de compra
"""

# lista
carrinho_lista = []
produto1 = ['Playstation5', 1, 5.000, 'branco', 1.8, 'Jogos', 'Console', 1.8, 4, 10.7, 400, 3.000]
produto2 = ['Xbox Series X', 1, 4.500, 'preto', 2, 'Jogos', 'Console', 1.8, 4, 10.7, 350, 2.500]

carrinho_lista.append(produto1)
carrinho_lista.append(produto2)

print(carrinho_lista)

# tuple
produto1 = ('Playstation5', 1, 5.000, 'branco', 1.8, 'Jogos', 'Console', 1.8, 4, 10.7, 400, 3.000)
produto2 = ('Xbox Series X', 1, 4.500, 'preto', 2, 'Jogos', 'Console', 1.8, 4, 10.7, 350, 2.500)
carrinho_tupla = (produto1, produto2)

print(carrinho_tupla)

# dicionário
carrinho_lista = []

# Note que em um dicionário, fica muito mais fácil acessar os valores a partir das chaves e não
# dos índices como seria feito em outras coleções.
produto1 = {
    'nome_prod': 'Playstation 5',
    'quantidade': 1,
    'preco': 5.000,
    'cor': 'branco',
    'peso': 1.8,
    'categoria': 'Jogos',
    'subcategoria': 'Console',
    'estoque': 400,
    'imposto1': 1.8,
    'imposto2': 4,
    'imposto3': 10.7,
    'pre_compra': 3.000
}

carrinho_lista.append(produto1)

# acessando o dicionario (produto1) dentro do carrinho.
for produto in carrinho_lista:
    # acessando cada item dentro do dicionário (produto1).
    for chave, valor in produto.items():
        print(f'{chave:<12} >>> {valor}')
_________________________________________________________________

# 3ª forma de criar um dicionário | menos usual
# Ideal para criar um dicionário com várias chaves de uma vez,
# quando todas precisam iniciar com o mesmo valor.
usuario = {}.fromkeys(['nome', 'telefone', 'email'], '')
print(usuario)


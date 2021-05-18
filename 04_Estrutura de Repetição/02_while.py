"""
While >>> Utilizada quando se sabe a quantidade de repetições e
quando não se sabe.
* Necessário atentar para o critério de parada.

Sintaxe >>>  while expressão_bool:
                    Execução.

Expressão será executada enquanto for verdadeira.
Expressão Booleana >>> Toda expressão onde o resultado
for Verdadeiro ou Falso.

Ex.
resposta = ''
    while resposta != 'SIM':
            resposta = 'input'
"""
# repetindo um texto 5 vezes com while
numero = 0

while numero < 5:
    print('Aline')
    numero += 1

# repetindo um texto 5 vezes com for
for nome in range(5):
    print('Aline')


# validando uma senha de forma simples
senha = '123456'
resposta = ''

while resposta != senha:
    resposta = str(input('Senha: '))


# contagem até 10
for cont in range(11):
    print(cont)
print('Acabei...')









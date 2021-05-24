"""
Faça um Programa com uma lista de 10 caracteres,
e diga quantas consoantes foram lidas. Imprima as consoantes.
"""

c = 0

consoantes = []

while c < 10:
    caracter = str(input('Digite um caracter: ')).lower()[0]

    if caracter not in 'aeiou':
        consoantes.append(caracter)

    c += 1

print('\nTotal de consoantes: ', end='')
for letra in consoantes:
    print(letra, end=' ')
print(f'\nTemos {len(consoantes)} consoantes.')

"""
Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços
em branco), conte:
a. quantos espaços em branco existem na frase.
b. quantas vezes aparecem as vogais a, e, i, o, u.
"""

frase = str(input('Digite uma frase: ')).strip().upper()

contador_vogais = 0

for palavra in frase:
    for letra in palavra:
        if letra in 'AÁÀÃÂEÉIÍOÓÕÔUÚ':
            contador_vogais += 1


print(f'\nAnalisando a frase: {frase}')
print(f'\nTotal de Espaços: {frase.count(" ")}')
print(f'Total de vogais: {contador_vogais}')


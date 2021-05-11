"""
 Faça um programa que identifique se uma frase é não palíndromo.
"""

# anotaramamaratona
# >>>>
# <<<<

frase = str(input('Digite uma palavra/frase: ')).upper()
palavras = frase.split()
juntas = ''.join(palavras)
invertida = ''


print(f'\nFrase normal: {frase}')
print(f'Frase separa em palavras: {palavras}')
print(f'Frase juntada: {juntas}')

for letra in range(len(juntas)-1, -1, -1):
    invertida += juntas[letra]

print(f'Frase invertida: {invertida}')

if invertida == juntas:
    print('\nA frase e/ou palavra é um palíndromo!')
else:
    print('\nA frase e/ou palavra não é um palíndromo!')








"""
Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no
conteúdo.
"""

string1 = str(input('Digite a primeira frase: ')).upper().strip()
string2 = str(input('Digite a segunda frase: ')).upper().strip()

print(f'\nA frase: {string1}\nEsta frase tem: {len(string1) - string1.count(" ")} caracteres.')
print(f'\nA frase: {string2}\nEsta frase tem: {len(string2) - string2.count(" ")} caracteres.')

'''
if len(string1) == len(string2):
    print('\nAs duas são iguais em tamanho!')
else:
    print('\nAs duas são diferentes em tamanho!')

if string1 == string2:
    print('As duas são iguais em conteúdo!')
else:
    print('As são diferentes em conteúdo!')
'''

if string1 == string2:
    print('\nAs duas frases são iguais no tamanho e no conteúdo!')
elif len(string1) == len(string2):
    print('\nAs duas frases são iguais no tamanho e diferentes no conteúdo!')
else:
    print('\nAs duas frases são diferentes no tamanho e conteúdo!')




'''
frase = '      leonardo alves     '.strip().upper()

tamanho = len(frase)
contando_espacos = frase.count(' ')

print(f'tamanho: {tamanho}')
print(f'Total de espaços no texto: {contando_espacos}')
print(f'Total de letras: {tamanho - contando_espacos}')
'''
'''
Faça um Programa que leia 4 notas, mostre as notas e a média na tela,
de forma que, todas as notas sejam armazenadas em uma lista antes dos cálculos.
'''
'''
lista = [1,2,3,4]
medias_das_notas = 0

for nota in lista:
    notas = float(input('Digite uma nota: '))
    soma_das_notas = notas
    
media_das_notas = soma_das_notas
print(f'Medias das notas {media_das_notas/soma_das_notas}')
'''

notas = []

for n in range(4):
    notas.append(float(input(f'Digite a {n + 1}ª nota: ')))

print(f'Notas: {notas}\nMédia do aluno {sum(notas) / len(notas)}')


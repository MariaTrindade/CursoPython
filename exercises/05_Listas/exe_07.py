"""
Faça um Programa que peça a idade e a altura de 5 pessoas,
armazene cada informação na sua respectiva lista.
Imprima a idade e a altura na ordem inversa a ordem lida.
"""

pessoas = []

for c in range(3):
    idade = int(input('Idade: '))
    altura = float(input('Altura: '))

    pessoas.append([idade, altura])

# pessoas.reverse()

for i, v in enumerate(pessoas):
    print(f'{i + 1}ª Pessoa | Idade: {v[0]} | Altura: {v[1]}')



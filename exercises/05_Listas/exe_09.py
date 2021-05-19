"""
Faça um programa que leia um número indeterminado de valores,
correspondentes a notas, encerrando a entrada de dados quando
for informado um valor igual a -1 (que não deve ser armazenado).
Após esta entrada de dados, faça:

Mostre a quantidade de valores que foram lidos;
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
"""
from time import sleep
notas = []
tot_valores = menores_7 = 0

while True:
    nota = float(input('Digite uma nota ou -1 para encerrar:  '))

    if nota >= 0:
        notas.append(nota)
    else:
        break

# ---------------------- imprimindo ----------------------
print()
print('ANALISANDO NOTAS INSERIDAS'.center(50))

# ---------------------- Quantidade de notas ----------------------
print(f'\nQuantidade de valores lidos: {len(notas)}')

# ---------------------- Exibindo todos os valores ----------------------
print(f'Todos os valores: ', end='')
for valor in notas:
    print(valor, end=' ')

# --------------Exibindo todos os valores na ordem inversa------------------
print('\nTodos os valores em ordem inversa: ')
notas.reverse()
for valor in notas:
    print(valor)

# ---------------------- Somando os valores ----------------------
print(f'Somando os valores: {sum(notas)}')

# ---------------------- Média dos valores ----------------------
print(f'Média dos valores: {sum(notas) / len(notas)}')

# -------------Quantidade de valores acima da média--------------
for valor in notas:
    if valor > (sum(notas) / len(notas)):
        tot_valores += 1
print(f'Quantidade de valores acima da média: {tot_valores}')

# ---------------------- Valores abaixo de 7 ----------------------
for valor in notas:
    if valor < 7:
        menores_7 += 1
print(f'Quantidade de valores abaixo de 7: {menores_7}')

# ---------------------- Mensagem final ----------------------
for ponto in range(50):
    print('.', end='')
    sleep(0.1)
print()
print('\033[32mPROGRAMA ENCERRADO!\033[M'.center(60))


























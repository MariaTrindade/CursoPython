"""
Crie um programa que solicita vários números inteiros ao usuário,
pergunte se ele quer continuar digitando e caso responda não,
informe o total de números digitados, o menor, o maior e a
média entre eles.
"""

total = soma = maior = 0
menor = 9999999999999999
resposta = 'S'

while resposta in 'S':
    num = int(input('Digite um número: '))
    total += 1
    soma += num

    if num > maior: # 30 > 0
        maior = num

    if num < menor: # 30 < 99999999999999
        menor = num

    resposta = str(input('\033[32mQuer continuar? \033[m')).upper().strip()
    if resposta == 'N':
        print('Encerrando o sistema')
    print()

# fora do while ------------------------
print(f'Total de número inseridos: {total}\nSoma dos números inseridos: {soma}\n'
      f'Média dos números inseridos: {soma / total:.1f}\nMaior número inserido: {maior}\n'
      f'Menor número inserido: {menor}')

0
2

0



1000.0
todos = []

while True:
    todos.append(int(input('Digite um número: ')))

    resposta = str(input('Quer continuar: ')).strip().upper()

    if resposta == 'N':
        break

    if 15 in todos:
        print('Achei')

print(f'Total de número inseridos: {todos}\nSoma dos números inseridos: {sum(todos)}\n'
      f'Média dos números inseridos: {sum(todos) / len(todos)}\nMaior número inserido: {max(todos)}\n'
      f'Menor número inserido: {min(todos)}')

















'''
Crie um programa que através de uma tupla, pergunte quanto foi gasto pelo
usuário com almoço em cada dia da semana. Ao final, mostre o total gasto
pelo usuário. Projete o valor que será gasto em 1 mês, caso o usuário
continue gastando o mesmo valor da primeira semana. Considere para o mês,
4 semanas
'''


dias = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
gasto = []

for dia in dias:
    gasto.append(float(input(f'valor gasto | {dia} | R$: ')))
qtd_sem = int(input('\nMês de quantas semanas: '))
print(f'\nValor gasto na primeira semana: R${sum(gasto)}')
print(f'Projetando o valor gasto no mês: R${sum(gasto) * qtd_sem}')

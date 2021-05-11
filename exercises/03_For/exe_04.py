"""
Faça um programa Tabuada,
que permite ao usuário informar o número a ser multiplicado.
"""

numero = int(input('Digite um número: '))
print()
for cont in range(1, 11):
    print(f'{cont:>2} x {numero} = {cont * numero}')





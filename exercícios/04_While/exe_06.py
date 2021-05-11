"""
Crie um programa que receba quatro notas de um único aluno, calcule e mostre a média, a soma das notas,
a maior e menor nota. Sendo o valor mínimo para nota: 0 e máximo: 10 (não deve aceitar valores de
nota fora deste intervalo)
"""
'''
nota = 0
while (nota >= 0) and (nota <= 10):
    nota = float(input('Nota: '))
'''


soma_nota = quant_nota = 0

while True:

    nota = float(input(f'Nota: '))

    if (nota >= 0) and (nota <= 10):
        soma_nota += nota
        quant_nota += 1

    if quant_nota == 4:
        break




# --------------------- fora do laço

print(f'\nQuantidade de notas: {quant_nota}\nSoma das notas: {soma_nota}\nMédia: {soma_nota / quant_nota:.1f}')

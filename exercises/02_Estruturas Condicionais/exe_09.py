"""
Faça um programa que peça a medida de 3 retas, informe ao usuário se,
com estas 3 retas é possível formar um triângulo. Se com estas retas for
possível formar um triangulo, o programa deve informar se este triangulo é:
equilátero, isósceles ou escaleno.
"""

# cada reta deve ser menor que a soma das demais.
# Equilátero >>> 3 medidas iguais
# Isósceles >>> 2 medidas iguais
# Escaleno >>> 3 medidas diferentes


reta1 = float(input('Digite a medida da primera reta: '))
reta2 = float(input('Digite a medida da segunda reta: '))
reta3 = float(input('Digite a medida da terceira reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('\nÉ possível é formar um triangulo com as medidas informadas.')

    if reta1 == reta2 == reta3 == reta1:
        print('Temos um triângulo Equilátero.')
    elif reta1 != reta2 != reta3:
        print('Temos um triângulo Escalêno.')
    else:
        print('Temos um triângulo Isósceles.')
else:
    print('\nNão é possível formar um triangulo com as medidas informadas.')

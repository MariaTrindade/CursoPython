"""
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo,
menor peso e maior peso, para isto você deve fazer um programa que pergunte a cada um dos clientes
da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dado quando
o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informado os
códigos e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro,
além da média das alturas e dos pesos dos clientes.
"""
quant = soma_alt = soma_peso = maior_a = menor_a = maior_p = menor_p = 0
cod_maior_a = cod_menor_a = peso_maior_a = peso_menor_a = alt_menor_p = alt_maior_p = 0
cod_maior_p = cod_menor_p = 0

while True:

    cod = int(input('\nInforme seu código: '))

    if cod == 0:
        break
    else:
        altura = float(input('Altura: '))
        peso = float(input('Peso: '))

        quant += 1
        soma_alt += altura
        soma_peso += peso

        if quant == 1:
            maior_a = altura
            menor_a = altura
            maior_p = peso
            menor_p = peso

        if altura >= maior_a:
            maior_a = altura
            peso_maior_a = peso
            cod_maior_a = cod

        elif altura < menor_a:
            menor_a = altura
            peso_menor_a = peso
            cod_menor_a = cod

        if peso >= maior_p:
            maior_p = peso
            alt_maior_p = altura
            cod_maior_p = cod

        elif peso < menor_p:
            menor_p = peso
            alt_menor_p = altura
            cod_menor_p = cod


print()
print('*' * 30, '\nDADOS GERAIS.')
print(f'Total de clientes: {quant}\nMédia de altura: {soma_alt / quant:.1f}\n'
      f'Média de peso: {soma_peso / quant:.1f}')

print()
print('*' * 30, '\nDADOS DO USUÁRIO MAIS ALTO.')
print(f'Código: {cod_maior_a}\nAltura: {maior_a}\nPeso: {peso_maior_a}')

print()
print('*' * 30, '\nDADOS DO USUÁRIO MAIS BAIXO.')
print(f'Código: {cod_menor_a}\nAltura: {menor_a}\nPeso: {peso_menor_a}')

print()
print('*' * 30, '\nDADOS DO USUÁRIO DE MAIOR PESO.')
print(f'Código: {cod_maior_p}\nAltura: {alt_maior_p}\nPeso: {maior_p}')

print()
print('*' * 30, '\nDADOS DO USÁRIO DE MENOR PESO.')
print(f'Código: {cod_menor_p}\nAltura: {alt_menor_p}\nPeso: {menor_p}')

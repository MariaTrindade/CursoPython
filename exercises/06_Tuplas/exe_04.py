''' Agora, vamos simular o funcionamento de um caixa eletrônico. O usuário deve
informar o valor do saque, em seguida o programa deve calcular quantas e
quais notas serão entregues. Considere que o caixa possui notas de 2, 5,
10, 50, 100 e 200 reais. A escolha das notas deve ser feita considerando
a entrega menor possível. '''

valor = int(input('Digite o valor saque: '))

total = valor
cedula = 200
tot_cedulas = 0

while True:
    if total >= cedula:
        total -= cedula
        tot_cedulas += 1
    else:
        if tot_cedulas > 0:
            print(f'Total de {tot_cedulas} cédulas de R${cedula}')

        if cedula == 200:
            cedula = 100
        elif cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2

        tot_cedulas = 0  # não esquecer de zerar a quantidade de cédulas

        if total == 0:
            break

"""
Faça um programa que solicite o sexo do usuário. O usuário deve digitar apenas:  F, M, N
Caso F, mostre na tela: Feminino
Caso M, mostre na tela: Masculino
Caso N, mostre na tela: Não se aplica
Caso contrário, mostre na tela: Dado inválido

"""

sexo = str(input('Digite seu sexo: ')).upper()

if sexo == 'F':
    print('Feminino!')
elif sexo == 'N':
    print('Não se aplica.')
elif sexo == 'M':
    print('Masculino!')
else:
    print('Dado inválido!')


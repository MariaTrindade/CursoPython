'''
Crie um programa que tenha uma tupla com uma contagem por extenso que vai de 0 a 20.
Permita que o usuário escolha um número qualquer e seu programa deverá mostrar este
número por extenso, fazendo uma busca pelo valor dentro da tupla.
'''
'''
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze/ catorze', 'quinze',
            'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
           )

status = False

while True:
    valor = int(input('Digite um número entre 0 e 20: '))
    if (valor >= 0) and (valor <= 20):
        print(f'\n{valor} por extenso: {extenso[valor]}')
    else:
        print('\033[31Ops, dado inválido,\033[m tente um número entre 0 e 20')

    while True:
        sair = str(input('\nDeseja consultar outro número? [S | N]: ')).upper()[0]
        if sair not in 'SN':
            print('\033[31mOps, dado inválido!\033[m')
        elif sair == 'S':
            break
        else:
            status = True
            break

    if status:
        print('\n\033[32m...legal, volte sempre!\033[m')
        break
'''

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte',)
cont = -1
while cont < 0 or cont > 20:
    cont = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número {numeros[cont]}')






















"""
Crie um programa tabuada que permita ao usuário solicitar quantas vezes ele quiser, encerrando quando
o mesmo responder não querer mais utilizar o programa, então finalize o programa com uma mensagem de
agradecimento.
"""

from time import sleep
resposta = ''

while True:

    num = int(input('Digite um número para iniciar: '))
    print()
    for cont in range(1, 11):
        print(f'{num} x {cont:<2} = {num * cont}')
        sleep(0.5)

    while True:
        resposta = str(input('\nTecle N para criar uma nova ou S para sair: ')).upper().strip()

        if resposta not in 'NS':
            print('...resposta inválida!')

        if resposta == 'S':
            status = True
            break

        if resposta == 'N':
            break

    if resposta == 'S':
        break

print()
print('\033[32mSistema Finalizado\033[m'.center(50))
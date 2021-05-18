"""
While com Break

while True: >>> este laço será executado enquanto não encontrar o Break pelo caminho.

Break >>> Condição de parada de um loop.

"""

while True:
    sair = int(input('Escolha uma opção (Tecle 5 para sair): '))

    if sair == 1:
        print('Seja bem vindo\n')
    elif sair == 2:
        print('Você digitou 2\n')
    elif sair == 3:
        print('Você digitou 3\n')
    elif sair == 4:
        print('Você digitou 4\n')
    elif sair == 5:
        print('Encerrando o sistema...')
        break
    else:
        print('Dado inválido!\n')

'''
nome = ''

while not nome.isnumeric():
    nome = input('Nome: ')

    if not nome.isnumeric():
        print(f'{nome}, muito prazer...')
    else:
        print('Ops, dado inválido! tente novamente...')

    print('Estou continuando')
'''
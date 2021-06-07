"""
Crie um programa cadastro com um dicionário contendo nome,
idade, e telefone de vários usuários. Pergunte se deseja
continuar cadastrando, caso não, encerre. Ao consultar se
o usuário deseja continuar, não deve ser aceito dados inválidos.
Ao final apresente os usuários cadastrados de maneira organizada.
"""

usuario = {}
lista_de_usuarios = list()

while True:
    usuario['nome'] = str(input('Nome: ')).title()
    usuario['idade'] = int(input('Idade: '))
    usuario['media'] = int(input('Telefone: '))
    print()
    lista_de_usuarios.append(usuario.copy())
    usuario.clear()

    while True:
        resp = str(input('Inserir novo usuario: ')).upper()
        if resp in 'SN':
            break
        print('\033[31mDado inválido\033[m, tente S ou N | ', end='')

    if resp == 'N':
        break

# [  {} , {}   ]

print()
print('=' * 40)
print('USUÁRIOS CADASTRADOS'.center(40))
print('=' * 40)

for indice in lista_de_usuarios:
    for c, v in indice.items():

        if c == 'nome':
            c = c.replace('nome', 'Apelido')

        if c == 'telefone':
            print('-' * 40)

        print(f'{c.title():<8} ===> {v}')

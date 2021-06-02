"""
Crie um programa cadastro com um dicionário contendo nome,
idade, e telefone de vários usuários. Pergunte se deseja
continuar cadastrando, caso não, encerre. Ao consultar se
o usuário deseja continuar, não deve ser aceito dados inválidos.
Ao final apresente os usuários cadastrados de maneira organizada.
"""

usuario = {}
usuarios = []

while True:
    usuario.update({'nome': str(input('Nome: ')).title()})
    usuario.update({'idade': int(input('Idade: '))})
    usuario.update({'telefone': int(input('Telefone (Apenas números): '))})
    print()
    usuarios.append(usuario.copy())
    usuario.clear()

    while True:
        saida = str(input('Inserir outro usuário? [S | N]: ')).upper()[0]
        print()
        if saida in 'SN':
            break
        print('\033[31mOps, dado inválido!\033[m\n')

    if saida == 'N':
        break

# imprimindo dados
print()
print('=' * 40)
print('USUÁRIO CADASTRADOS'.center(40))
print('=' * 40)

for u in usuarios:
    for c, v in u.items():
        print(f'{c.title():.<8}: {v}')
        if c == 'telefone':
            print('-' * 40)

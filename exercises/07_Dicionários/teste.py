nome = 'Leonardo'

biscoitos = []
refrigerantes = []

biscoito = {}

biscoito['Fabricante'] = 'Nestle'
biscoito['Nome'] = 'Bonno'
biscoito['Validade'] = '2021-10-06'
biscoito['Sabor'] = 'Chocolate'
biscoito['Preco'] = 3.59
biscoito['Quantidade'] = 400

biscoitos.append(biscoito.copy())

biscoito['Fabricante'] = 'Nestle'
biscoito['Nome'] = 'Bonno'
biscoito['Validade'] = '2021-18-010'
biscoito['Sabor'] = 'Morango'
biscoito['Preco'] = 5.59
biscoito['Quantidade'] = 200

biscoitos.append(biscoito.copy())

print(len(biscoitos))

for produto in biscoitos:
    for c, v in produto.items():
        if c == 'Sabor':
            print(v)

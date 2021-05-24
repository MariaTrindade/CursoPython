"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será
determinado pela média dos cinco saltos. Você deve fazer um programa que receba o nome e as cinco distâncias
alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa
deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m
Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9
"""

saltos = []
registro = list()

while True:
    nome = str(input('Nome: ')).title()
    for s in range(1, 3):
        saltos.append(float(input(f'{s}º salto: ')))

    registro.append([nome, saltos[:], sum(saltos) / len(saltos)])
    saltos.clear()

    while True:
        resposta = str(input('\nInserir um novo atleta? [S | N]: ')).upper().strip()
        if resposta not in 'NS' or resposta == '':
            print('Resposta inválida!')
        elif resposta == 'N':
            break
        else:
            print()
            break

    if resposta == 'N':
        break

# --------------------- imprimindo -------------------------

# registro [ [nome, [5saltos], média]   ,    [nome, [5saltos], média] ]

#for c, a in enumerate(registro):
#    print(f'{c + 1} >>>> {a}')

linha = '-' * 30
print()

for atleta in registro:
    print(f'Nome: {atleta[0]:>5}\nSaltos: {atleta[1]}\nMédia:  {atleta[2]:.2f}\n{linha}\n')

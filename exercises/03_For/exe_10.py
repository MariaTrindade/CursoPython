"""
Faça um programa cadastro. Ele deve solicitar o nome, idade e sexo de 10 pessoas.
Ao final mostre, a média de idade de todos dos homens e das mulheres,
assim como a média geral. O nome do homem mais velho e da mulher mais nova.
Obrigatório utilizar estrutura FOR.
"""

soma_id_h = soma_id_m = quant_h = quant_m = maior_idade = menor_idade = 0
nome_h_velho = nome_m_nova = ''

for cont in range(4):
    nome = str(input('Nome: ')).title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M | F]: ')).upper()
    print('*' * 30)

    if cont == 0:
        maior_idade = idade
        nome_h_velho = nome
        menor_idade = idade
        nome_m_nova = nome

    if sexo == "M":
        soma_id_h += idade
        quant_h += 1

        if idade > maior_idade:
            maior_idade = idade
            nome_h_velho = nome

    elif sexo == "F":
        soma_id_m += idade
        quant_m += 1

        if idade < menor_idade:
            menor_idade = idade
            nome_m_nova = nome

    else:
        print('Dado inválido!')

print(f'\n\nMédia de idade dos homens: {soma_id_h / quant_h:.1f}\n'
      f'Média de idade das mulheres: {soma_id_m / quant_m:.1f}\n'
      f'Média idade geral: {(soma_id_h / quant_h) + (soma_id_m / quant_m):.1f}\n'
      f'Com {maior_idade} anos de idade, o Sr. {nome_h_velho} é o mais velho.\n'
      f'Com {menor_idade} anos de idade, a Srª {nome_m_nova} é a mais nova.')

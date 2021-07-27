"""
**KWARGS
    - Mesma idéia do *args quando ao nome
    - Diferente do args que coloca os valores em uma tupla,
    o kwargs exige que os parâmentros sejam nomeados e os
    transforma em um dicionário.

Ordem geral dos parâmetros na declaração da função
    - parâmetros obrigatórios
    - *args
    - parâmetros default (não obrigatórios)
    - **kwargs

"""

'''
def cores(**kwargs):
    # print(kwargs)
    for pessoa, cor in kwargs.items():
        print(f'{pessoa.title()} gosta mais de {cor}.')


cores(leo='verde', juca='vermelho', ana='branco', maria='roxo')
'''


# Função com todos os parâmetros

def todosParametros(idade, nome, cpf=00000000000, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos.')
    print(f'{nome} tem {idade} anos e seu CPF é: {cpf}')
    print(f'Recebi no args: {args}')

    if solteiro:
        print('Solteiro')
    else:
        print('Casado')

    print(f'Recebi no Kwargs: {kwargs}')


# todosParametros(30, 'leonardo')
# todosParametros(30, 'leonardo', 123456789)
# todosParametros(30, 'leonardo', 123465798, 15, 15, 26, 25, 4, 8)
# todosParametros(30, 'leonardo', 123465798, 15, 15, 26, 25, 4, 8, solteiro=True)
todosParametros(30, 'leonardo', 123465798, 15, 15, 26, 25, 4, 8, solteiro=True, doce='Ninho', suco='Abacaxi')


# desempacotamento

def mostraNome(**kwargs):
    return f'{kwargs["nome"]} {kwargs["sobrenome"]}'


dicionario = dict(nome='Leonardo', sobrenome='Alves')

print(mostraNome(**dicionario))


# Ao desempacotar, vale lembrar que tanto o args quanto o kwargs não precisam
# ser declaro como parâmetros da função, basta apenas o * ou ** quando o argumento
# for passado para a função.

def somaTres(a, b, c):
    print(a + b + c)


lista = [10, 20, 30]
tupla = (10, 20, 30)
conjunto = {10, 20, 30}
dicionario = {'a': 10, 'b': 20, 'c': 30}  # os nomes das chaves devem ser os mesmos dos parâmetros

somaTres(*lista)
somaTres(*tupla)
somaTres(*conjunto)
somaTres(**dicionario)

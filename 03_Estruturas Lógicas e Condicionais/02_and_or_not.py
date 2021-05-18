"""
Operadores unitários >>> Dependem de um único valor >>> not, is
Operadores binários >>> Dependem de mais que 1 valor >>> and, or
"""

'''
AND >>> Ambos os valores precisam ser TRUE
OR >>> Pelo menos um valor precisa ser TRUE
NOT >>> Negação, inverte a expressão
IS >>> Questiona se um dado é...
'''

cpf = input('CPF: ')

if cpf.isnumeric():
    print('continuando o cadastro')
else:

    print('Ops, dado inválido!')
"""
Funções com RETORNO
Return >>> Finaliza a função.
- Retorna qualquer tipo de dado inclusive multiplos.

Sintaxe:
        def nome_da_funcao (parâmetros de entrada):
            bloco da função
            .
            .
            return alguma coisa

Quanto utilizo o print e quanto utilizo return?
-Se quiser utilizar o resultado no restando do código,
será melhor que ele seja retornado. Caso queira apenas
mostrar a saída e qualquer alteração, use o print.

def diz_oi():
    return 'Oi'

nome = str(input('Nome: '))
print(f'{diz_oi()}, {nome}!')
"""

# __________________ exemplo 1 ==> Função que printa a palavra OI
def diz_oi():
    return 'Oi'

print(diz_oi())

# __________________ exemplo 2 ==> Função que canta parabéns
def parabens():
    '''
    Função que mostra o trecho da música parabéns pra você.
    :return: string com a letra da música 'parabéns para você'.
    '''
    return 'Parabens pra você\n' \
           'Nesta data querida!\n' \
           'Viva o aniversariantes!!!'


print(parabens())


# __________________ exemplo 3 ==> Função cabeçalho da nota fiscal
def cabecalho():
    return '''
                ==============================
                        LOJA DO SEU ZÉ
                ==============================
           '''

print(cabecalho())

# __________________ exemplo 4 ==> Função que soma dois valores
def soma():
    return 2 + 2


print(soma())

# __________________ exemplo 5 ==> Função com mais de 1 return
def teste():
    dado = True
    if dado:
        return 10
    elif dado in None:
        return 20
    return 30

# __________________ exemplo 6 ==> Função que retorna mais q 1 dado
def teste1():
    return [1, 2, 3, 4, 5]


n1, n2, n3, n4, n5 = teste1()
print(n1, n2, n3, n4, n5)
print(teste1())

# __________________ exemplo 7 ==> Função com retorno e método built-in
from random import random


def joga_moeda():
    num = random()  # gera um número pseudo-randômico entre 0 e 1
    if num > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())


# __________________ exemplo 8 ==> Função que verifica se é par
def par():
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        return True
    else:
        return False


print(par())

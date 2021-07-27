"""
[SEM PARÂMETROS] Crie uma função que imprima em letras maiúsculas na tela a frase que o usuário digitar.
"""


def caixaAlta():
    frase = str(input('Digite uma frase: ')).upper()
    print(frase)


def caixaAlta1():
    frase = str(input('Digite uma frase: '))
    return frase.upper()


def caixaAlves2(frase):
    print(frase)


def caixaAlta3(frase):
    return frase


# __________ Programa Principal __________

caixaAlta()
print(caixaAlta1())
caixaAlves2(str(input('Digite uma frase: ')).upper())
print(caixaAlta3(str(input('Digite uma frase: ')).upper()))

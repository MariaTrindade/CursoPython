"""
[SEM PARÂMETROS] Crie uma função que imprima na tela a frase: ‘Python é vida!’
"""


def imprimeFrase():
    print('Python é vida!')


def imprimeFrase1():
    return 'Python é vida!'


def imprimeFrase2(frase):
    print(frase)


def imprimeFrase3(frase):
    return frase


# ___________ Programa principal ______________

imprimeFrase()
print(imprimeFrase1())
imprimeFrase2('Python é vida!')
print(imprimeFrase3('Python é vida!'))

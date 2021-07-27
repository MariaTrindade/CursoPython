"""
Função onde a passagem de parâmentro é opcional


"""

# exe01
print('Leonardo')  # informando um argumento
print()  # argumento vazio
print('Alves')


# Função com parâmentro obrigatório
def quadrado(num):
    return num ** 2


print(quadrado(9))


# Função com parâmetro opcional
def quadradoOuMais(num, potencia=2):  # os parâmetros opcionais, sempre após os obrigatórios
    return num ** potencia


print(quadradoOuMais(5, 3))
print(quadradoOuMais(5))


# Função dentro de outra função

def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador += 10

        return contador
    return dentro()


print(fora())

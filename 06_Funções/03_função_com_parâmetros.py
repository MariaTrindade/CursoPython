"""
Funções com Parametros (de entrada)

Vale ressaltar que parâmetros são opcionais.

Parâmetros
    - variáveis declaradas na definição da função

Argumentos
    - Dados passados durante a execução de uma função

"""


# exe01 - Função que retorna um número elevado ao cubo
def cubo(num):  # parâmentro aqui é obrigatório
    return num ** 3


print(cubo(2))  # Ao chamar a função,o paramentro deve ser informado


# exe02 - Função que canta parabéns
def cantarParabens(nome):
    print(f'Parabéns pravocê\nNesta data querida\n'
          f'Muitas felicidades\nMuitos anos de vida'
          f'\nViva a(o) {nome}!')


cantarParabens(str(input('Nome da(o) aniversariante: ')).title())


# exe03 - Funções com n parâmentros
def soma(a, b):
    return a + b


def mult(num1, num2):  # 2 argumentos
    return num1 * num2


def outra(num3, num4, letra):  # 3 parâmentros
    return (num3 + num4) * letra


print(soma(10, 20))  # 2 argumentos
print(mult(5, 10))
print(outra(2, 8, 'J'))  # 3 argumentos

# KEYWORDS
# Quando utilizamos nomes dos parâmetros nos argumentos, a ordem não importa mais...

nome = 'Leonardo'
sobrenome = 'Alves'


def nomeCompleto(nome, sobrenome):
    return f'Nome completo: {nome} {sobrenome}'


print(nomeCompleto(sobrenome='Alves', nome='Leonardo'))
print(nomeCompleto(sobrenome=sobrenome, nome=nome))


# erro comum na utilização do return

def somaImpares(num):
    total = 0
    for n in num:
        if n % 2 != 0:
            total += n
        # return total - Vai encerrar o for na primeira execução
    return total


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(somaImpares(numeros))
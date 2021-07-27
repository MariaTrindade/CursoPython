"""
[SEM PARÂMETROS] Crie uma função que peça 3 números e em seguida imprima o
resultado da soma deles, lembrando que os 3 números que foram
digitados também devem aparecer. Exemplo da impressão esperada:
Números inseridos: n1, n2 e n3
Somando os 3 números, temos: resultado
"""


def primeiraSoma3():
    num = []
    for cont in range(1, 4):
        num.append(int(input(f'Digite o {cont}º número: ')))

    print(f'\nNúmeros inseridos: ', end='')
    for n in num:
        print(n, end='. ')

    print(f'\nSomando os 3 números, temos: {sum(num)}\n')


primeiraSoma3()


def segundaSoma3():
    num = []
    for cont in range(1, 4):
        num.append(int(input(f'Digite o {cont}º número: ')))
    return num


saida = segundaSoma3()
print('\nNúmeros inseridos: ', end='')
for n in saida:
    print(n, end='. ')
print(f'\nSomando os 3 números, temos: {sum(saida)}\n')


def terceiraSoma3(n1, n2, n3):
    print(f'\nNúmeros inseridos: {n1}. {n2}. {n3}.')
    print(f'Somando os 3 números, temos: {n1 + n2 + n3}\n')


terceiraSoma3(
    int(input('Digite o 1º número: ')),
    int(input('Digite o 2º número: ')),
    int(input('Digite o 3º números: '))
)


def quartaSoma3(n1, n2, n3):
    return dict(
        primeiroNumero=n1,
        segundoNumero=n2,
        terceiroNumero=n3,
        somaNumeros=n1 + n2 + n3
    )


num = []
for cont in range(3):
    num.append(int(input('Digite um número: ')))

dados = quartaSoma3(num[0], num[1], num[2])

print(f"\nNúmeros inseridos: {dados['primeiroNumero']}. {dados['segundoNumero']}"
      f" {dados['terceiroNumero']}.\nSomando os 3 números, temos: {dados['somaNumeros']}")

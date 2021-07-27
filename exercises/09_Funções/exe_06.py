"""
[SEM PARÂMETROS] Crie uma função com a tarefa de verificar se um número digitado pelo usuário é par ou ímpar,
em seguida imprima o resultado, mostrando também o número que foi digitado pelo usuário.
Seu programa só deve terminar quando o usuário decidir sair. Faça este Loop como preferir.
"""


def ParesImpares():
    numero = int(input('\nDigite um numero: '))

    if numero % 2 == 0:
        return f'O numero {numero}, é par.\n'
    else:
        return f'O número {numero} é impar.\n'

    # ==========================================================


while True:
    print(ParesImpares())
    saida = str(input('Tecle [ S ] para sair: ')).upper()
    if saida == 'S':
        break

"""
[SEM PARÂMETROS] Crie um programa habilitação, ele deve receber o nome,
data de nascimento e cpf (Se tiver) do usuário. Você deverá ter uma função 
para validar se a idade o usuário permite que ele prossiga no processo para 
obter sua habilitação, por fim, imprima na tela um relatório desta análise. 
Obs: 1 função com a mensagem que será apresentada ao usuário como motivo pelo 
qual ele pode ou não obter a habilitação, também deverá ser criada.
"""


def cnh():
    from datetime import date
    from time import sleep

    anoAtual = date.today().year

    usuario = {
        'nome': str(input('Nome: ')).title(),
        'cpf': int(input('CPF: ')),
        'diaNasc': int(input('Dia [00]: ')),
        'mesNasc': int(input('Mês [00]: ')),
        'anoNasc': int(input('Ano [0000]: '))
    }

    usuario['idade'] = anoAtual - usuario['anoNasc']

    print()
    print('\033[7;33m...carregando DADOS DO USUÁRIO:\033[m')
    sleep(3)

    for c, v in usuario.items():

        if c == 'diaNasc':
            c = c.replace('diaNasc', 'Dia')
        if c == 'mesNasc':
            c = c.replace('mesNasc', 'Mês')
        if c == 'anoNasc':
            c = c.replace('anoNasc', 'Ano')

        print(f'{c.title():<5} ===> {v}')
        sleep(0.4)

    if usuario['idade'] >= 18:
        sleep(1)
        msgOK()
    else:
        sleep(1)
        msgNO()


def msgOK():
    print('\n\033[7;32mLegal! Você está apto para tirar sua CNH\033[m')


def msgNO():
    print('\n\033[7;31mOps! Volte quando tiver 18 ou + anos de idade.\n\033[m')


# ==========================================================

cnh()

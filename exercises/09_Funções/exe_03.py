"""
[SEM PARÂMETROS] Crie uma função que peça nome, idade, cpf e em seguida imprima estes dados na tela.
"""


def cadastro():
    nome = str(input('Nome: ')).title()
    idade = int(input('Idade: '))
    cpf = int(input('CPF: '))

    print(f'\nDados cadastrados:\nNome: {nome}\nIdade: {idade}\nCPF: {cpf}')


def cadastro1():
    nome = str(input('Nome: ')).title()
    idade = int(input('Idade: '))
    cpf = int(input('CPF: '))

    return nome, idade, cpf


def cadastro2(nome, idade, cpf):
    print(f'\nDados cadastrados:\nNome: {nome}\nIdade: {idade}\nCPF: {cpf}')


def cadastro3(nome, idade, cpf):
    return nome, idade, cpf


# ___________Programa Principal __________

cadastro()

dados = cadastro1()
print(f'\nDados cadastrados:\nNome: {dados[0]}\nIdade: {dados[1]}\nCPF: {dados[2]}')

cadastro2(
    str(input('Nome: ')).title(),
    int(input('Idade: ')),
    int(input('CPF: '))
)

dados = cadastro3(
                    str(input('Nome: ')).title(),
                    int(input('Idade: ')),
                    int(input('CPF: '))
                )

print(f'\nDados cadastrados:\nNome: {dados[0]}\nIdade: {dados[1]}\nCPF: {dados[2]}')










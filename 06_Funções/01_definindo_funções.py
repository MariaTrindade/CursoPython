"""
Funções
- Pequenos trechos de código que realizam tarefas específicas.
- Podem ser feitas com ou sempre parâmetros e com ou sem retorno.
- Muito úteis para executar tarefas repetidas vezes sem a necessidade
de reescrever o código.
- Devem ser simples e objetivas.

Algumas funções built-in que já  utilizamos até aqui:
print(), len(), help(), sum(), max(), min()
range(), count(), upper(), title(), lower()...

Sintaxe:
         def nome_da_função (parâmetros de entrada):
            bloco da função

Idealmente o nome precisa ser minusculo e separado por snake case quando
for nome composto.
"""


# __________________ exemplo 1 ==> Função que printa a palavra OI
def diz_oi():
    print('Oi')


diz_oi()

# print(diz_oi())

# __________________ exemplo 2 ==> Função que canta parabéns
def parabens():
    """
    Função que mostra o trecho da música parabéns pra você.
    :return: string com a letra da música 'parabéns para você'.
    """
    print('Parabens pra você\n'
          'Nesta data querida!\n'
          'Viva o aniversariantes!!!')


parabens()

# __________________ exemplo 3 ==> Função cabeçalho da nota fiscal
def cabecalho():
    print('=' * 40, '\n', 'LOJA DO ZÉ'.center(36))
    print('-' * 40)

cabecalho()

# print(cabecalho())

# __________________ exemplo 4 ==> Função que soma dois valores
def soma():
    print(2 + 2)

soma()


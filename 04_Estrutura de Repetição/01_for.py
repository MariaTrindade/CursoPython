"""
ESTRUTURA DE REPETIÇÃO

For >>> Utilizada quando se sabe a quantidade de repetições que serão necessárias,
de forma que é obrigatório determinar o final da execução do laço.

Sintaxe >>> for item in iteravel:
                execução

* Range
    Ex. Contador 10 - 0
                 0 - 10
                  step

* Enumerate
     Ex. for valor in enumerate(frase)

* String (palavra, frase)
* Lista
"""

from time import sleep

print('Contagem regressiva!\n')

for contador in range(11):
    print(contador)
    sleep(1)

print('\nBum! Pah! Bum!')


soma = 0

for cont in range(4):
    nota = float(input(f'{cont + 1}ª Nota: '))
    soma += nota

print(f'\nMédia do aluno: {soma/4:.1f}')



inicio = int(input('Digite o início da contagem: '))
fim = int(input('Digite o fim da contagem: '))
passo = int(input('Digite o passo: '))

for contador in range(inicio, fim, passo):
    print(contador, end=' ')















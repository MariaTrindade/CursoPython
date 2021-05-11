from click._compat import raw_input
from time import sleep

print('#' * 60)
print('PROGRAMA DETETIVE'.center(60))
print('*' * 60)
sleep(1)
print('\n\033[32m', '...por favor, aguarde! Instruções sendo carregadas...'.center(60), '\033[m')
sleep(2)
print('\033[1;31m\n', 'ATENÇÃO'.center(60), '\033[m')
print('''
Responda as perguntas apenas com: S para sim ou N para não.
Qualquer resposta diferente destas citadas acima, anulará 
imediatamente o teste.'''.center(60))
sleep(2)
print('\n\033[34m', '...Carregando perguntas...'.center(60), '\033[m')
print('_' * 60, '\n')
sleep(5)
perguntas = ('Esteve no local do crime? ',
             'Devia para a vítima? ',
             'Mora perto da vitima? ',
             'Já trabalhou com a vitíma? ',
             'Telefonou para a vítima? ',
             'Está tenso? ')

respostas = []
status = ''

for pergunta in perguntas:
    respostas.append(raw_input(pergunta).upper())

cont = 0
for resposta in respostas:
    if resposta == 'S':
        cont += 1

if cont < 2:
    status = 'Inocente, desculpe o transtorno!'
elif cont == 2:
    status = 'Suspeito, não saia da cidade...'
elif cont <= 4:
    status = 'Cumplice, você permanecerá aqui esta noite!'
else:
    status = 'Assassino, por favor, acompanhe o guarda Ebony!'

print('\n\033[32m', '...por favor, aguarde! Respostas sendo analisadas...'.center(60), '\033[m')
print('_' * 60, '\n')
sleep(5)
print(status.center(60))
print('_' * 60, '\n')
print('\n\033[32m', '...por favor, aguarde!Finalizando sistema...'.center(60), '\033[m', '\n')
sleep(3)
print('*' * 60)
print('EBONY SYS'.center(60))
print('*' * 60)

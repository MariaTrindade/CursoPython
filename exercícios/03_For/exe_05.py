"""
Faça um programa que mostre uma contagem regressiva de 10 à 0,
com pausa de 1 segundo. Utilize a função sleep para isto.
"""

from time import sleep

print('\033[1;32mIniciando contagem!!!\033[m \n')
sleep(1)

for cont in range(10, 0, -1):
    print(cont)
    sleep(1)

print('\n\033[32mBum \033[31mPichhhh \033[33mbulfff!!!!\033[m')



"""
Faça um programa que leia 3 número e mostre o maior e o menor.
"""

num_1 = int(input("Digite um número"))
num_2 = int(input("Digite um segundo número"))
num_3 = int(input("Digite um terceiro número"))

'''if num_1 > num_2 and num_1 > num_3:
    print(f"\nO maior número é o número: {num_1}")

elif num_2 > num_1 and num_2 > num_3:
    print(f"\nO maior número é o número: {num_2}")

elif num_3 > num_1 and num_3 > num_2:
    print(f"\nO maior número é o número: {num_3}")
'''


maior = num_1

if num_2 > num_1 and num_2 > num_3:
    maior = num_2
if num_3 > num_1 and num_3 > num_2:
    maior = num_3

print(maior)
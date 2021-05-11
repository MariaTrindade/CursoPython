"""
Faça um programa que verifique se uma letra digitada é vogal ou consoante.
"""

letra = str(input('Digite uma letra: '))

if letra.lower() in 'aeiou':
    print('Esta é uma vogal!')
else:
    print('Esta é uma consoante!')
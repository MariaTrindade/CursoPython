"""
Supondo que a cotação do dólar esteja em R$4.25, salve esse valor em uma variável e utilize-o para
criar um programa onde seja possível cambiar qualquer valor em R$ para Dólar.
"""

dolar = float(input('Informe o valor em dólar: '))
cotacao = 5.78
conversao = dolar / cotacao

print(f'{dolar} em dólar, convertido em reais: R$ {conversao:.2f}')


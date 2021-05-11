"""
Você e os outros integrantes da sua república (Joca, Moacir, Demival e Jackson) foram no
supermercado e compraram alguns itens:

75 latas de cerveja: R$ 2,20 cada (da ruim ainda, pra fazer o dinheiro render)
2 pacotes de macarrão: R$ 8,73 cada
1 pacote de Molho de tomate: R$ 3,45

420g Cebola: R$ 5,40/kg
250g de Alho: R$ 30/kg
450g de pães franceses: R$ 25/kg

Calcule quanto ficou para cada um.
"""

cebola = ((420 * 5.40) / 1000)
alho = (250 * 30) / 1000
paes = (450 * 25) / 1000

carrinho_compra = 75 * 2.20 + 2 * 8.73 + 3.45 + cebola + alho + paes

print(f'\nProdutos:\nCebola: R$ {cebola:.2f}\nAlho: R$ {alho:.2f}\nPães: R$ {paes:.2f}'
      f'\n\nTotal da compra: R$ {carrinho_compra:.2f}\n\nTotal para cada amigo: {carrinho_compra/4:.2f}')


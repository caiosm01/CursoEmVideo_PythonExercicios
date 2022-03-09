tabela = ('Lápis', 'R$0,50', 'Borracha', 'R$2,00', 'Caneta', 'R$1,00', 'Estojo', 'R$5,00', 'Mochila', 'R$100,00', 'Caderno', 'R$25,50', 'Régua', 'R$1,50', 'Tesoura', 'R$3,50', 'Cola', 'R$4,25')
print('-='*30)
print(f'{"TABELA DE PREÇOS":^55}')
print('-='*30)
for c in range(0, len(tabela[::2])):
   print(f'{tabela[::2][c]:.<50}', end='')
   print(f'{tabela[1::2][c]}\n', end='')
print('-='*30)
produto = str(input('Informe qual produto deseja saber o preço:')).strip().title()
print(f'{produto} custa {tabela[tabela.index(produto) + 1]}.')

from emoji import emojize
n=int(input('Informe um número inteiro para verificar se ele é um número primo:'))
cont=0
for c in range(1, n+1):
    if n % c == 0:
        cont +=1
        print('\033[33m', '{}'.format(c).replace('0', emojize(':zero:', use_aliases=True))
      .replace('1',  emojize(':one:', use_aliases=True))
      .replace('2',  emojize(':two:', use_aliases=True))
      .replace('3', emojize(':three:', use_aliases=True))
      .replace('4', emojize(':four:', use_aliases=True))
      .replace('5', emojize(':five:', use_aliases=True))
      .replace('6', emojize(':six:', use_aliases=True))
      .replace('7', emojize(':seven:', use_aliases=True))
      .replace('8', emojize(':eight:', use_aliases=True))
      .replace('9', emojize(':nine:', use_aliases=True)),'\033[m',emojize(':arrow_right:', use_aliases=True), end=' ')
    else:
        print('\033[31m','{}'.format(c).replace('0', emojize(':zero:', use_aliases=True))
      .replace('1',  emojize(':one:', use_aliases=True))
      .replace('2',  emojize(':two:', use_aliases=True))
      .replace('3', emojize(':three:', use_aliases=True))
      .replace('4', emojize(':four:', use_aliases=True))
      .replace('5', emojize(':five:', use_aliases=True))
      .replace('6', emojize(':six:', use_aliases=True))
      .replace('7', emojize(':seven:', use_aliases=True))
      .replace('8', emojize(':eight:', use_aliases=True))
      .replace('9', emojize(':nine:', use_aliases=True)),'\033[m', emojize(':arrow_right:', use_aliases=True) ,end=' ')
print('\nO número {} foi divisível {} vezes.'.format(n, cont))
if cont == 2:
    print('É PRIMO!')
else:
    print('NÃO É PRIMO!')

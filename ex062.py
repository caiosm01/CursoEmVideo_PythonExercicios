from emoji import emojize
a1=int(input('Informe o primeiro termo:'))
r=int(input('Informe a razão:'))
n=1
a=0
mais=1
while n <=10:
    a=a1+(n-1)*r
    print(emojize('{} :arrow_right:', use_aliases=True).format(a).replace('0', emojize(':zero:', use_aliases=True))
          .replace('1', emojize(':one:', use_aliases=True))
          .replace('2', emojize(':two:', use_aliases=True))
          .replace('3', emojize(':three:', use_aliases=True))
          .replace('4', emojize(':four:', use_aliases=True))
          .replace('5', emojize(':five:', use_aliases=True))
          .replace('6', emojize(':six:', use_aliases=True))
          .replace('7', emojize(':seven:', use_aliases=True))
          .replace('8', emojize(':eight:', use_aliases=True))
          .replace('9', emojize(':nine:', use_aliases=True)), end=' ')
    n += 1
print(emojize(':heavy_check_mark:\n', use_aliases=True))
resposta=str(input('Deseja adicionar mais termos?')).strip().upper()[0]
if resposta == 'S':
    while mais != 0:
        mais=int(input('\nQuantos mais?'))
        if mais != 0:
            while n <= mais+10:
                a = a1 + (n - 1) * r
                print(emojize('{} :arrow_right:', use_aliases=True).format(a).replace('0', emojize(':zero:', use_aliases=True))
                      .replace('1', emojize(':one:', use_aliases=True))
                      .replace('2', emojize(':two:', use_aliases=True))
                      .replace('3', emojize(':three:', use_aliases=True))
                      .replace('4', emojize(':four:', use_aliases=True))
                      .replace('5', emojize(':five:', use_aliases=True))
                      .replace('6', emojize(':six:', use_aliases=True))
                      .replace('7', emojize(':seven:', use_aliases=True))
                      .replace('8', emojize(':eight:', use_aliases=True))
                      .replace('9', emojize(':nine:', use_aliases=True)), end=' ')
                n += 1
            print(emojize(':heavy_check_mark:\n', use_aliases=True))
print('Progressão finalizada com {} termos.'.format(n-1))
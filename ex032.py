from datetime import date
ano=int(input('Informe um ano qualquer para descobrir se é um ano bissexto. Ultilize o zero caso queira analisar o ano atual: '))
if ano == 0:
    ano= date.today().year
if ano % 4 != 0:
    print('O ano {} não é bissexto.'.format(ano))
if ano % 4 == 0 and ano % 100 != 0:
    print('O ano {} é bissexto.'.format(ano))
if ano % 4 ==0 and ano % 100 == 0 and ano % 400 == 0:
    print('O ano {} é bissexto.'.format(ano))
if ano % 4 == 0 and ano % 100 == 0 and ano % 400 != 0:
    print('O ano {} não é bissexto.'.format(ano))
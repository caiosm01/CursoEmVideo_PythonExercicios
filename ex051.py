from emoji import emojize
from random import randint
o=randint(31, 37); p=randint(31, 37); q=randint(31, 37); s=randint(31, 37)
print('\033[{}m-='.format(q)*11)
print('\033[{}mPROGRESSÃO ARITMÉTICA'.format(o))
print('\033[{}m-='.format(q)*11)
a1=int(input('\033[{}mInforme o primeiro termo:'.format(o)))
r=int(input('\033[{}mInforme a razão:'.format(p)))
print('\033[{}mEssa prgressão aritmética é:'.format(s))
print(emojize('\033[{}m:heavy_minus_sign:\033[{}m'.format(q, s) * 36, use_aliases=True))
for c in range(1, 11):
    a=a1 + (c-1)*r
    print(emojize('{} :arrow_right:', use_aliases=True).format(a).replace('0', emojize(':zero:', use_aliases=True))
      .replace('1',  emojize(':one:', use_aliases=True))
      .replace('2',  emojize(':two:', use_aliases=True))
      .replace('3', emojize(':three:', use_aliases=True))
      .replace('4', emojize(':four:', use_aliases=True))
      .replace('5', emojize(':five:', use_aliases=True))
      .replace('6', emojize(':six:', use_aliases=True))
      .replace('7', emojize(':seven:', use_aliases=True))
      .replace('8', emojize(':eight:', use_aliases=True))
      .replace('9', emojize(':nine:', use_aliases=True)), end=' ')
print(emojize(':heavy_check_mark:\n', use_aliases=True))
print(emojize('\033[{}m:heavy_minus_sign:\033[{}m'.format(q, s) * 36, use_aliases=True))
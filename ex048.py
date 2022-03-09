from random import randint
a=randint(31, 37)
b=randint(31, 37)
d=randint(31, 37)
e=randint(31, 37)
f=randint(31, 37)
g=randint(31, 37)
h=randint(31, 37)
j=randint(31, 37)
print('\033[{}m{}'.format(a, '-='*43))
print('\033[{}mSOMATÓRIO DE TODOS OS NÚMEROS ÍMPARES E MÚLTIPLOS DE TRÊS ENTRE OS VALORES ESCOLHIDOS!'.format(b))
print('\033[{}m{}'.format(d, '-='*43))
i=int(input('\033[{}minício:'.format(e)))
f=int(input('\033[{}mFim:'.format(f)))
s1=0
s2=0
print('\033[{}mOs números que são ímpares e múltiplos de três entre {} e {} são:'.format(g, i, f))
for c in range(i, f+1):
    if c % 2 != 0 and c % 3 ==0:
        print('\033[{}m{}'.format(h, c), end=' ')
        s1=s1+c
        s2=s2+1
print('\n\033[{}mO somatório de todos os {} números é igual a {}.'.format(j, s2, s1))
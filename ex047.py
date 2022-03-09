from random import randint
o=randint(31, 37)
p=randint(31, 37)
q=randint(31, 37)
r=randint(31, 37)
print('\033[3;4;36m-=\033[m'*31)
print('\033[{}mVAMOS VERIFICAR QUAIS SÃO OS NÚMEROS PARES ENTRE DOIS NÚMEROS'.format(o))
print('\033[3;4;36m-=\033[m'*31)
i=int(input('\033[{}mInício:'.format(p)))
f=int(input('\033[{}mFim:'.format(q)))

for c in range(i, f+1):
    resto = c % 2
    if resto == 0:
        print('\033[{}m{}'.format(r, c), end=' ')
print('\nACABOU!')
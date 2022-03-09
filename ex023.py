'''num=int(input('Informe um número entre 0 e 9999:'))
u=num //1 %10
d=num//10 %10
c=num//100 %10
m=num//1000 %10
print('unidade: {}.'.format(u))
print('dezena: {}.'.format(d))
print('centena: {}.'.format(c))
print('milhar: {}.'.format(m))'''

num= str(input('Informe um número entre 0 e 9999: ')).strip()
if len(num) == 4:
    print('unidade: {}.'.format(num[3]))
    print('dezena: {}.'.format(num[2]))
    print('centena: {}.'.format(num[1]))
    print('milhar: {}.'.format(num[0]))
if len(num) ==3:
    print('unidade: {}.'.format(num[2]))
    print('dezena: {}.'.format(num[1]))
    print('centena: {}.'.format(num[0]))
    print('milhar: 0.')
if len(num) == 2:
    print('unidade: {}.'.format(num[1]))
    print('dezena: {}.'.format(num[0]))
    print('centena: 0.')
    print('milhar: 0.')
if len(num) ==1:
    print('unidade: {}.'.format(num[0]))
    print('dezena: 0.')
    print('centena: 0.')
    print('milhar: 0.')
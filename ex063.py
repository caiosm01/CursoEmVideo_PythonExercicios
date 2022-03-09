'''from emoji import emojize
n=int(input('Informe o número de termos da sequência de Fibonacci desejado:'))
c = 0
anterior1=0
anterior2=1
while c < n/2:
    print(emojize('{} :arrow_right:', use_aliases=True).format(anterior1), end='')
    print(emojize('{} :arrow_right:', use_aliases=True).format(anterior2), end='')
    anterior1 = anterior1 + anterior2
    anterior2= anterior2 + anterior1
    c+=1
print(emojize(':heavy_check_mark:\n', use_aliases=True))'''



print('-'*30)
print('SEQUÊNCIA DE FIBONACCI')
print('-'*30)
n=int(input('Quantos termos você quer mostrar?'))
t1 = 0
t2 = 1
cont = 3
print('~'*30)
print('{} -> {}'.format(t1, t2), end='')
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1=t2
    t2=t3
    cont += 1
print(' -> FIM')

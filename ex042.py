from math import fabs
print('VERIFICANDO A POSSIBILIDADE DE FORMAR TRIÂNGULOS')
a=float(input('Informe a primeira medida:CM'))
b=float(input('Informe a segunda medida:CM'))
c=float(input('Informe a terceira medida:CM'))
if fabs(b - c) < a and b + c > a or fabs(a - c) < b and a + c > b or fabs(a - b) < c and a + b > c:
    if a==b and a!=c or a==c and a!=b or c==b and c!=a:
        print('As medidas {}, {} e {} PODEM FORMAR um triângulo isósceles.'.format(a, b, c))
    elif a==b==c:
        print('As medidas {}, {} e {} PODEM FORMAR um triângulo equilátero.'.format(a, b, c))
    else:
        print('As medidas {}, {} e {} PODEM FORMAR um triângulo escaleno.'.format(a, b, c))
else:
    print('As medidas {}, {} e {} NÃO PODEM FORMAR um triângulo.'.format(a, b, c))

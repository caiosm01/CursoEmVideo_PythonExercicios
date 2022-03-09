'''x=float(input('informe o comprimento, em métros, do cateto adjacente:'))
y=float(input('Informe o comprimento, em métros, do cateto oposto:'))
h=(x**2+y**2)**(1/2)
print('O valor da hipotenusa de um triangulo retangulo cujo o cateto oposto é {} e o cateto adjacente é {}, será {}.'.format(y, x, h))'''

from math import hypot
x=float(input('informe o comprimento, em métros, do cateto adjacente:'))
y=float(input('Informe o comprimento, em métros, do cateto oposto:'))
print('O valor da hipotenusa de um triangulo retangulo cujo o cateto oposto é {} e o cateto adjacente é {}, será {:.2f}.'.format(y, x, hypot(y, x)))

'''from math import sin, cos, tan, radians
A=float(input('Informe um ângulo, em graus:'))
rad=radians(A)
print('O angulo {:.2f} tem seno igual a {:.2f}, cosseno igual a {:.2f} e tangente igual a {:.2f}.'.format(A, sin(rad), cos(rad), tan(rad)))'''

'''import math
angulo=float(input('Informe um ângulo em graus:'))
seno=math.sin(math.radians(angulo))
cosseno=math.cos(math.radians(angulo))
tangente=math.tan(math.radians(angulo))
print('O angulo {:.2f} tem seno igual a {:.2f}, cosseno igual a {:.2f} e tangente igual a {:.2f}.'.format(angulo, seno, cosseno, tangente))'''

from math import sin, cos, tan, radians
angulo=float(input('Informe um ângulo em graus:'))
seno= sin(radians(angulo))
cosseno= cos(radians(angulo))
tangente= tan(radians(angulo))
print('O angulo {:.2f} tem seno igual a {:.2f}, cosseno igual a {:.2f} e tangente igual a {:.2f}.'.format(angulo, seno, cosseno, tangente))
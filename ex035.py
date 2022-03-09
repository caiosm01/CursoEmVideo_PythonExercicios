from math import fabs
print('\033[1;31;40mSabendo que, para três segmentos de reta formarem um triângulo, é necessário que um de seus lados deve ser maior que o valor absoluto (módulo)\033[m\n\033[1;31;40mda diferença dos outros dois lados e menor que a soma dos outros dois lados.\033[m\n\033[1;31;40mInforme três valores de segmento de reta, em métros, para saber se podem formar um triÂngulo.\033[m')
a= float(input('\033[1;31;40mInforme a primeira medida:\033[m'))
b= float(input('\033[1;31;40mInforme a segunda medida:\033[m'))
c= float(input('\033[1;31;40mInforme a terceira medida:\033[m'))

if fabs(b-c) < a and b+c > a or fabs(a-c) < b and a+c > b or fabs(a-b) < c and a+b > c:
    print('\033[1;31;40mAs medidas {}{}{}{}, {}{}{}{} e {}{}{}{} PODER FORMAR um triângulo.\033[m'.format('\033[34m', a, '\033[m','\033[1;31;40m' , '\033[34m', b, '\033[m','\033[1;31;40m' ,'\033[34m', c, '\033[m','\033[1;31;40m' ))
else:
    print('\033[1;31;40mAs medidas {}{}{}{}, {}{}{}{} e {}{}{}{} NÃO PODEM FORMAR um triângulo.\033[m'.format('\033[34m', a, '\033[m','\033[1;31;40m' , '\033[34m', b, '\033[m','\033[1;31;40m' ,'\033[34m', c, '\033[m','\033[1;31;40m'))

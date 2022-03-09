'''from random import randint
from time import sleep
from termcolor import colored
a=randint(0,5)
print(colored('-=-','yellow')*19)
print(colored('Vou pensar em um número de 0 a 5. Tente adivinhar...', 'blue'))
print(colored('-=-','yellow')*19)
escolha=int(input('Informe um número de 0 a 5:'))
print(colored('PROCESSANDO...', 'red'))
sleep(2)
if escolha==a:
    print(colored('O número que o computador escolheu foi {}. Parabéns, você ganhou!','green').format(a))
else:
    print(colored('O número que o computador escolheu foi {}.O computador ganhou.','green').format(a))'''

from random import randrange
a= randrange(6)
numero= int(input('O computador irá pensar em um número entre 0 e 5. Tente adivinhar para ganhar o jogo:\n'))
print('O computador pensou no número {}.'.format(a))
if numero == a:
    print('Parabéns, você ganhou!')
else:
    print('Você perdeu!')
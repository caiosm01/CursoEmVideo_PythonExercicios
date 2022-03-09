from random import randrange
from time import sleep
print('{:=^40}'.format('JO KEN PO'))
print('''Suas opções:
[0]- PEDRA
[1]- PAPEL
[2]- TESOURA''')
escolha=int(input('Sua escolha:'))
pc=randrange(3)
itens=('pedra', 'papel', 'tesoura')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)
print('O computador jogou {}'.format(itens[pc]))
print('O jogador jogou {}'.format(itens[escolha]))
if pc == 0:
    if escolha == 0:
        print('DEU EMPATE!')
    if escolha == 1:
        print('VOCÊ VENCEU!')
    if escolha == 2:
        print('COMPUTADOR VENCEU!')
elif pc == 1:
    if escolha == 0:
        print('COMPUTADOR VENCEU!')
    if escolha == 1:
        print('DEU EMPATE')
    if escolha == 2:
        print('VOCÊ VENCEU!')

elif pc == 2:
    if escolha == 0:
        print('VOCÊ VENCEU!')
    if escolha == 1:
        print('COMPUTADOR VENCEU!')
    if escolha == 2:
        print('DEU EMPATE')
else:
    print('Opção inválida. Tente novamente!')

















'''from random import randrange
from time import sleep
print('{:=^40}'.format('JO KEN PO'))
print('Suas opções:
[0]- PEDRA
[1]- PAPEL
[2]- TESOURA')
escolha=int(input('Sua escolha:'))
pc=randrange(3)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)
if escolha == 0 and pc == 0:
    print('{:=^40}'.format('-'))
    print('Computador escolheu pedra')
    print('Jogador escolheu pedra')
    print('DEU EMPATE!')
elif escolha == 1 and pc == 1:
    print('{:=^40}'.format('-'))
    print('Computador escolheu papel')
    print('Jogador escolheu papel')
    print('DEU EMPATE!')
elif escolha == 2 and pc == 2:
    print('{:=^40}'.format('-'))
    print('Computador escolheu tesoura')
    print('Jogador escolheu tesoura')
    print('DEU EMPATE!')
elif escolha == 0 and pc == 1:
    print('{:=^40}'.format('-'))
    print('Computador escolheu papel')
    print('Jogador escolheu pedra')
    print('COMPUTADOR VENCEU!')
elif escolha == 0 and pc == 2:
    print('{:=^40}'.format('-'))
    print('Computador escolheu tesoura')
    print('Jogador escolheu pedra')
    print('VOCÊ VENCEU!')
elif escolha == 1 and pc == 0:
    print('{:=^40}'.format('-'))
    print('Computador escolheu pedra')
    print('Jogador escolheu papel')
    print('VOCÊ VENCEU!')
elif escolha == 1 and pc == 2:
    print('{:=^40}'.format('-'))
    print('Computador escolheu tesoura')
    print('Jogador escolheu papel')
    print('COMPUTADOR VENCEU!')
elif escolha == 2 and pc == 0:
    print('{:=^40}'.format('-'))
    print('Computador escolheu pedra')
    print('Jogador escolheu tesoura')
    print('COMPUTADOR VENCEU!')
elif escolha == 2 and pc == 1:
    print('{:=^40}'.format('-'))
    print('Computador escolheu papel')
    print('Jogador escolheu tesoura')
    print('VOCÊ VENCEU!')
else:
    print('Opção inválida. Tente novamente.')'''
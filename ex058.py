from random import randint
pc=randint(0, 10)
num = 20
tentativa = 0
computador = -1
print('''\033[7;36mCOMPUTADOR: Olá, vamos jogar?!\033[m
\033[7;36mEu irei pensar em um número entre 0 e 10 e o seu objetivo é tentar advinhar com o menor número de tentativas possível.\033[m
\033[7;36m[1° tentativa]- 10 pontos\033[m
\033[7;36m[2° tentativa]- 9 pontos\033[m
\033[7;36m[3° tentativa]- 8 pontos\033[m
\033[7;36m[4° tentativa]- 7 pontos\033[m
\033[7;36m[5° tentativa]- 6 pontos\033[m
\033[7;36m[6° tentativa]- 5 pontos\033[m
\033[7;36m[7° tentativa]- 4 pontos\033[m
\033[7;36m[8° tentativa]- 3 pontos\033[m
\033[7;36m[9° tentativa]- 2 pontos\033[m
\033[7;36m[10° tentativa]- 1 ponto\033[m
\033[7;36m[11° tentativa]- 0 pontos\033[m
\033[7;36mCaso você acerte, ganhará os pontos da tentativa correspondente. Caso você erre, eu ganho 1 ponto.\033[m
\033[7;36mGANHA QUEM FIZER MAIS PONTOS!!!!!!!\033[m''')
while num != pc:
    num=int(input('Em qual número eu pensei?'))
    if num <= 10:
        if num != pc:
            if num > pc:
                print('MENOS... Tente novamente.', end=' ')
            elif num < pc:
                print('MAIS... Tente novamente.', end=' ')
    else:
        print('Opção inválida. Tente novamente.', end=' ')
    tentativa += 1
    computador += 1
print('Você precisou de {} tentativas para adivinhar.'.format(tentativa))
if tentativa <= 5:
    print('Eu fiz {} pontos e'.format(computador),'você fez {} pontos.'.format(tentativa).replace('1', '10')
          .replace('2', '9').replace('3', '8').replace('4', '7').replace('5', '6')
          .replace('0', '11'))
    print('PARABÉNS!!! VOCÊ GANHOU!!')
elif tentativa == 6:
    print('Eu fiz {} pontos e'.format(computador), 'você fez {} pontos.'.format(tentativa).replace('10', '1')
          .replace('9', '2').replace('8', '3').replace('7', '4').replace('6', '5')
          .replace('11', '0'))
    print('DEU EMPATE!!')
elif tentativa > 6:
    print('Eu fiz {} pontos e'.format(computador), 'você fez {} pontos.'.format(tentativa).replace('10', '1')
          .replace('9', '2').replace('8', '3').replace('7', '4').replace('6', '5')
          .replace('11', '0'))
    print('VOCÊ PERDEU! MAIS SORTE NA PRÓXIMA HAHAHAHA.')

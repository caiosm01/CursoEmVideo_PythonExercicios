n1=float(input('Primeira nota:'))
n2=float(input('Segunda nota:'))
media=(n1+n2)/2
if media < 5:
    print('REPROVADO, com média {:.1f}.'.format(media))
elif media >= 5 and media < 7:
    print('RECUPERAÇÃO, com média {:.1f}.'.format(media))
elif media >= 7:
    print('APROVADO, com média {:.1f}.'.format(media))
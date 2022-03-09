'''num=int(input('Informe o número de pessoas a serem analisadas:'))
nome=[]
idade=[]
sexo=[]
menores=[]
somaidade=0
i=0
velho=0
cont=0
nvelho=' '
for c in range(0, num):
    print('-='*17)
    nome.insert(i, str(input('Informe o nome da {}° pessoa:'.format(c+1)).strip().title()))
    idade.insert(i, int(input('Informe a idade da {}° pessoa:'.format(c+1))))
    sexo.insert(i, str(input('Informe o sexo da {}° pessoa[M/F]:'.format(c+1)).upper()))
    somaidade=somaidade+idade[i]
    if sexo[i] == 'M':
        if idade[i] > velho:
            velho=idade[i]
            nvelho=nome[i]
    elif sexo[i] == 'F':
        if idade[i] < 20:
            cont+=1
            menores.insert(i, nome[i])
    i += 1
media= somaidade/num
print('-=' * 17)
print('A média das idades é {:.2f}.'.format(media))
print('O homem mais velho é o {}, com {} anos.'.format(nvelho, velho))
print('O número de mulheres com menos de 20 anos é {}. Elas são {}'.format(cont, menores))'''




num=int(input('Informe o número de pessoas a serem analisadas:'))
somaidade=0
velho=0
nomevelho=' '
cont=0
menores=[]
i=0
for c in range(0, num):
    print('-=' * 17)
    nome=str(input('Informe o nome da {}° pessoa:'.format(c + 1))).strip().title()
    idade=int(input('Informe a idade da {}° pessoa:'.format(c + 1)))
    sexo=str(input('Informe o sexo da {}° pessoa[M/F]:'.format(c + 1))).upper()
    if sexo == 'M':
        if idade > velho:
            velho=idade
            nomevelho=nome
    elif sexo == 'F':
        if idade < 20:
            cont+=1
            menores.insert(i, nome)
    somaidade = somaidade + idade
    i+=1
media=somaidade/num
print('A média das idades é {:.2f}.'.format(media))
print('O homem mais velho é o {}, com {} anos.'.format(nomevelho, velho))
print('O número de mulheres com menos de 20 anos é {}. Elas são {}'.format(cont, menores))

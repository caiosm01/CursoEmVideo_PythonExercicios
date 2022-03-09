from datetime import date
num= int(input('Informe o número de pessoas para analisar quantas são maiores de idade:'))
nascimento=[]
hoje=date.today().year
maior=0
menor=0
for c in range(1, num+1):
    nascimento.append(int(input('Ano do nascimento do {}°:'.format(c))))
for x in nascimento:
    if hoje-x <= 18:
        menor+=1
    else:
        maior+=1
print('Dos informados foram {} maiores de idade e {} menores de idade.'.format(maior, menor))
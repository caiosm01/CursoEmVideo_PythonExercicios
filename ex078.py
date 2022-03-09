lita = list(int(input(f'Informe o valor da posição {i}:')) for i in range(0, 5))
maior = []
menor = []
print('-='*30)
print(f'Você digitou os valores: {lita}')
for c, v in enumerate(lita):
   if v == max(lita):
       maior.append(c)
   elif v == min(lita):
       menor.append(c)
print(f'O maior valor digitado foi o {max(lita)} na posiçâo: {maior}')
print(f'O menor valor digitado foi o {min(lita)} na posiçâo: {menor}')
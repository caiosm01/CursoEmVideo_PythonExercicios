c = 1
s = cont = 0
while True:
    n= int(input(f'Informe o {c}° número [-1 para parar]:'))
    if n == -1:
        break
    s += n
    cont += 1
    c += 1
print(f'A soma dos {cont} números é {s}.')
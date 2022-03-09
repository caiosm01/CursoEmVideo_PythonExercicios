def leiaDinheiro(v):
    c = str(input(v)).replace(',', '.')
    while c.isalpha() or c.strip() == '':
        print(f'\033[31mERRO: "{c}" é um preço inválido!\033[m')
        c = str(input(v)).strip()
    return float(c)
